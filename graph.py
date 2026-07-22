from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from debaters import optimist_agent, pessimist_agent, moderator_summary

class DebateState(TypedDict):
    topic: str
    transcript: str
    round_count: int

def create_debate_graph():
    def optimist_node(state: DebateState):
        arg = optimist_agent(state["topic"], state["transcript"])
        new_transcript = f"{state['transcript']}\n\n[Optimist]: {arg}"
        return {"transcript": new_transcript, "round_count": state["round_count"] + 1}

    def pessimist_node(state: DebateState):
        arg = pessimist_agent(state["topic"], state["transcript"])
        new_transcript = f"{state['transcript']}\n\n[Skeptic]: {arg}"
        return {"transcript": new_transcript}

    def moderator_node(state: DebateState):
        summary = moderator_summary(state["topic"], state["transcript"])
        new_transcript = f"{state['transcript']}\n\n[Moderator Synthesis]: {summary}"
        return {"transcript": new_transcript}

    # Conditional router to limit debate rounds
    def should_continue(state: DebateState):
        if state["round_count"] < 2:
            return "pessimist"
        return "moderator"

    workflow = StateGraph(DebateState)
    workflow.add_node("optimist", optimist_node)
    workflow.add_node("pessimist", pessimist_node)
    workflow.add_node("moderator", moderator_node)

    workflow.add_edge(START, "optimist")
    workflow.add_conditional_edges("optimist", should_continue, {
        "pessimist": "pessimist",
        "moderator": "moderator"
    })
    workflow.add_conditional_edges("pessimist", should_continue, {
        "pessimist": "optimist",
        "moderator": "moderator"
    })
    workflow.add_edge("moderator", END)

    return workflow.compile()
