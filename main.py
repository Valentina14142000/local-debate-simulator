from graph import create_debate_graph

def run():
    print("Initializing Autonomous AI Debate Simulator...")
    app = create_debate_graph()

    topic = "Fully autonomous local AI agents running without human supervision in critical enterprise infrastructure."
    print(f"\nDebate Topic: \"{topic}\"\n")

    initial_state = {
        "topic": topic,
        "transcript": "--- Debate Begins ---",
        "round_count": 0
    }

    result = app.invoke(initial_state)
    
    print("=== Final Debate Transcript & Synthesis ===")
    print(result["transcript"])
    print("===========================================")

if __name__ == "__main__":
    run()
