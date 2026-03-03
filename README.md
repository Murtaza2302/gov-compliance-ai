
# 🏛 Government Procurement Compliance AI System

A multi-agent, domain-aligned AI system for automated compliance analysis and drafting based on Indian Government procurement policies.

This system demonstrates production-style AI orchestration using:

- Multi-agent architecture
- Hybrid RAG retrieval
- Clause-level grounding
- Local LLM inference (Ollama)
- Iterative compliance validation
- Structured JSON output enforcement

---

# 📌 Objective

To design a production-grade, multi-agent AI system capable of:

- Extracting clauses and deadlines from procurement manuals
- Identifying approving authorities
- Detecting contradictions across policy documents
- Drafting structured compliance notes
- Performing iterative compliance validation
- Handling ambiguity explicitly
- Producing structured and auditable outputs

---

# 🧠 System Architecture

## High-Level Flow

User Query  
↓  
Planner Agent  
↓  
Ambiguity Agent  
↓  
Iterative Loop:  
 Analysis Agent (Hybrid RAG + Clause Extraction)  
 ↓  
 Contradiction Agent  
 ↓  
 Drafting Agent (LLM via Ollama)  
 ↓  
 Critic Agent (Compliance Validation)  
↓  
Final Formatter  
↓  
Structured JSON Output  

---

# 🏗 Architecture Components

## 1️⃣ Orchestration Layer (workflow.py)

- Maintains shared state object  
- Controls execution order of agents  
- Manages iterative refinement loop  
- Ensures structured final output  

---

## 2️⃣ Multi-Agent Layer

### 🧩 Planner Agent
Decomposes user query into structured tasks.

### ❓ Ambiguity Agent
Detects missing information and adds explicit assumptions.

### 📚 Analysis Agent (Hybrid RAG)
- FAISS vector search  
- SentenceTransformer embeddings  
- Keyword-based filtering  
- Clause ID extraction (Rule/Section detection)  

### ⚖ Contradiction Agent
Detects conflicting monetary thresholds across documents.

### ✍ Drafting Agent
- Uses Ollama local LLM  
- Model: llama3:8b-instruct-q4_0  
- Generates structured compliance notes  

### 🛡 Critic Agent
Validates:
- Clause presence  
- Source references  
- Draft completeness  
Controls refinement loop.

---

# 📄 Government Documents Used

- Manual for Procurement of Goods (2024)  
- Manual for Procurement of Non-Consultancy Services (2025)  
- General Financial Rules (GFR) 2017 (Updated)  

---

# ⚙️ Technical Stack

| Component | Technology |
|------------|------------|
| Orchestration | Python |
| Vector Search | FAISS |
| Embeddings | SentenceTransformers |
| LLM Serving | Ollama |
| Model | llama3:8b-instruct-q4_0 |
| Interface | CLI |

---

# 🔁 Iterative Refinement

If compliance validation fails:

Analysis → Draft → Critic loop is repeated  
(Max iterations configurable; CPU demo version uses 1 iteration)

---

# 📦 Output Format

```json
{
  "human_draft": "...",
  "structured_summary": {
      "query": "...",
      "total_clauses_used": 3
  },
  "clause_references": [
      {
          "source": "Manual_Goods_2024.pdf",
          "clause_id": "2.3",
          "snippet": "..."
      }
  ],
  "compliance_status": "PASS",
  "violations": [],
  "confidence_score": 0.9
}
```

---

# 🚀 How To Run

## 1️⃣ Install Dependencies

pip install -r requirements.txt

## 2️⃣ Install Ollama

Download from https://ollama.com

Pull model:

ollama pull llama3:8b-instruct-q4_0

## 3️⃣ Run System

python -m orchestration.workflow

---

# 🖥 Hardware Assumptions

- 16GB RAM  
- CPU compatible  
- Optional GPU support  

---

# 🎯 Design Philosophy

- Modular multi-agent orchestration  
- Domain-grounded hybrid RAG  
- Clause-level explainability  
- Structured JSON enforcement  
- Local deployability  

---
