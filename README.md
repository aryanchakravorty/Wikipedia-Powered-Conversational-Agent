# Wikipedia RAG Conversational Agent

## Project Description

This project implements an **LLM-powered conversational assistant** that answers user queries using **Wikipedia as an external knowledge source**. It leverages **Retrieval-Augmented Generation (RAG)** and a **ReAct (Reason + Act)** agent to enable tool-based reasoning, semantic search, and grounded responses through an interactive chat interface.

---

## Features

* Wikipedia page indexing into a **vector store** for semantic retrieval
* **RAG-based question answering** using retrieved factual context
* **ReAct agent** enabling step-by-step reasoning and tool usage
* Interactive **Chainlit UI** with dynamic model and page selection
* Modular and extensible codebase

---

## Prerequisites

* Python 3.8+
* OpenAI API key

---

## Project Structure

```
.
├── chat_agent.py          # ReAct-based agent and Chainlit interface
├── index_wikipages.py     # Wikipedia page extraction and vector indexing
├── utils.py               # API key handling utilities
├── chainlit.md            # Chainlit usage instructions
└── README.md
```

---

## Usage

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Add API key**
   Create an `apikeys.yml` file:

```yaml
openai:
  api_key: YOUR_OPENAI_API_KEY
```

3. **Run the application**

```bash
chainlit run chat_agent.py
```

4. **Configure and chat**

* Select the LLM model from settings
* Enter pages to index, e.g.

  ```
  please index: Paris, London
  ```
* Ask questions related to the indexed Wikipedia pages

---

## Author

Aryan Chakravorty
