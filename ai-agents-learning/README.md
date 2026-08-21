# AI Agents Learning

A hands-on learning project for understanding **LLMs, LangChain, Tool Calling, AI Agents, RAG, and LangGraph** using **Ollama** and the local **Llama 3.2** model.

## 🚀 Project Goal

The goal of this project is to learn how modern AI agent applications work by building small examples step by step.

The project uses:

* Python
* Ollama
* Llama 3.2
* LangChain
* LangGraph
* RAG
* Tool Calling
* AI Agents

## 📁 Project Structure

```text
ai-agents-learning/
│
├── 01_basic_langchain.py
├── 02_prompts.py
├── 03_tool_calling.py
├── 04_agents.py
├── 05_rag.py
├── 06_langgraph.py
├── knowledge.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## 🧠 Learning Roadmap

### 1. Basic LangChain

File:

```text
01_basic_langchain.py
```

Learn how to connect LangChain with Ollama and run a local LLM.

```text
User
 ↓
LangChain
 ↓
Ollama
 ↓
Llama 3.2
 ↓
Response
```

### 2. Prompt Templates

File:

```text
02_prompts.py
```

Learn how to create reusable prompts using LangChain prompt templates.

```text
User Input
 ↓
Prompt Template
 ↓
Formatted Prompt
 ↓
Llama 3.2
 ↓
Response
```

### 3. Tool Calling

File:

```text
03_tool_calling.py
```

Learn how an LLM can request external tools such as a calculator.

```text
User
 ↓
LLM
 ↓
Tool Call
 ↓
Calculator
```

### 4. AI Agents

File:

```text
04_agents.py
```

Learn how an agent can use an LLM and tools to complete tasks.

```text
User
 ↓
Agent
 ↓
LLM
 ↓
Tool
 ↓
Tool Result
 ↓
Final Answer
```

### 5. RAG

File:

```text
05_rag.py
```

Learn the basics of **Retrieval-Augmented Generation**.

The example uses `knowledge.txt` as a local knowledge source.

```text
Knowledge
   ↓
Context
   ↓
User Question
   ↓
LLM
   ↓
Answer
```

A more advanced RAG system can use document chunking, embeddings, vector databases, and similarity search.

### 6. LangGraph

File:

```text
06_langgraph.py
```

Learn how to create graph-based AI workflows using states, nodes, and edges.

```text
START
  ↓
LLM Node
  ↓
END
```

LangGraph can later be used to build more complex workflows involving agents, tools, decisions, and multiple steps.

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/avanthikodem-prog/ai-agents-learning.git
cd ai-agents-learning
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Install Ollama

Install Ollama on your computer and make sure it is running.

Check the installation:

```powershell
ollama --version
```

### 6. Download Llama 3.2

```powershell
ollama pull llama3.2
```

Check available models:

```powershell
ollama list
```

You should see:

```text
llama3.2
```

## ▶️ Running the Examples

Run each example separately:

```powershell
python 01_basic_langchain.py
```

```powershell
python 02_prompts.py
```

```powershell
python 03_tool_calling.py
```

```powershell
python 04_agents.py
```

```powershell
python 05_rag.py
```

```powershell
python 06_langgraph.py
```

## 🔄 Overall Architecture

The learning path progresses from a simple LLM application to agent-based workflows:

```text
                Llama 3.2
                    │
                    ▼
              ┌───────────┐
              │ LangChain │
              └─────┬─────┘
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
    Prompts      Tools          RAG
       │            │            │
       └────────────┼────────────┘
                    ▼
                 Agents
                    │
                    ▼
               LangGraph
                    │
                    ▼
          AI Agent Workflows
```

## 📚 Concepts Learned

* Large Language Models (LLMs)
* Ollama
* Local AI models
* LangChain
* Prompt Templates
* Tool Calling
* AI Agents
* Retrieval-Augmented Generation (RAG)
* LangGraph
* Graph-based workflows
* State management
* Nodes and edges
* Local AI development

## 🎯 Future Learning

Planned improvements include:

* [ ] Advanced tool calling
* [ ] Multiple tools
* [ ] Proper tool execution loops
* [ ] Document loaders
* [ ] Text splitting
* [ ] Embeddings
* [ ] Vector databases
* [ ] Advanced RAG
* [ ] Agent + RAG
* [ ] LangGraph agent workflows
* [ ] Conditional graph routing
* [ ] Multi-agent systems
* [ ] Memory
* [ ] Final AI agent project

## 💻 Technologies

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Programming language        |
| Ollama     | Run LLMs locally            |
| Llama 3.2  | Local language model        |
| LangChain  | Build LLM applications      |
| LangGraph  | Build stateful AI workflows |

## 📌 Learning Approach

This repository is built as a practical learning project. Each Python file focuses on one concept and gradually increases in complexity.

The objective is to understand **how AI agents work internally**, rather than only using pre-built agent applications.

## 👩‍💻 Author

**Avanthi Kodem**

GitHub: https://github.com/avanthikodem-prog

---

⭐ This repository documents my journey of learning and building AI agents with open-source and locally running AI tools.
