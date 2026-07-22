from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_debate_model():
    return ChatOpenAI(
        model="smollm2-135m-instruct",
        temperature=0.7,
        openai_api_base="http://127.0.0.1:1234/v1",
        openai_api_key="not-needed"
    )

def optimist_agent(topic: str, history: str) -> str:
    model = get_debate_model()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an extreme technological optimist. You believe artificial intelligence and decentralized local agents will solve all human bottlenecks, increase abundance, and create a utopia. Defend this stance passionately based on the ongoing debate."),
        ("user", "Topic: {topic}\n\nPrevious Debate History:\n{history}\n\nPresent your argument or rebuttal:")
    ])
    chain = prompt | model | StrOutputParser()
    return chain.invoke({"topic": topic, "history": history})

def pessimist_agent(topic: str, history: str) -> str:
    model = get_debate_model()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a pragmatic, highly skeptical systems architect. You focus on edge-case failures, runaway resource consumption, security vulnerabilities, and existential risks of autonomous systems. Attack the flaws in the previous argument."),
        ("user", "Topic: {topic}\n\nPrevious Debate History:\n{history}\n\nPresent your critique or rebuttal:")
    ])
    chain = prompt | model | StrOutputParser()
    return chain.invoke({"topic": topic, "history": history})

def moderator_summary(topic: str, history: str) -> str:
    model = ChatOpenAI(
        model="smollm2-135m-instruct",
        temperature=0,
        openai_api_base="http://127.0.0.1:1234/v1",
        openai_api_key="not-needed"
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an objective AI moderator. Analyze the debate transcript and provide a balanced synthesis of the core trade-offs discussed."),
        ("user", "Topic: {topic}\n\nFull Debate Transcript:\n{history}\n\nProvide your neutral moderator synthesis:")
    ])
    chain = prompt | model | StrOutputParser()
    return chain.invoke({"topic": topic, "history": history})
