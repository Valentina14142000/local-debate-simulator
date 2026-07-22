# Local AI Debate Simulator 🗣️🤖⚖️

An autonomous multi-agent debate and synthesis simulator built using **LangGraph**, **LangChain**, and **LM Studio**. It pits opposing AI personas (an extreme technological optimist and a skeptical systems architect) against each other in automated turn-taking rounds, followed by an objective moderator synthesis—all running 100% offline and locally.

---

## Features

* **100% Offline & Private:** Operates entirely locally via LM Studio without external API leakage.
* **Multi-Agent State Routing:** Utilizes LangGraph conditional edges and circular workflows to manage conversational turn-taking between opposing personas.
* **Automated Moderator Synthesis:** Concludes the debate by summarizing core trade-offs and arguments.

---

## Tech Stack

* **Orchestration:** LangGraph / LangChain (`langgraph`, `langchain`, `langchain-openai`)
* **Runtime:** Python 3.9+ / Virtual Environment (`venv`)
* **Local Inference:** LM Studio (compatible with OpenAI-spec local endpoints)

---

