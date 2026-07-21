# Enterprise-Knowledge-Assistant

> A production-ready AI-powered Enterprise Knowledge Assistant built using **LangGraph**, **FastAPI**, **Streamlit**, **Hybrid Retrieval**, **Reranking**, and **Retrieval-Augmented Generation (RAG)**.

---

## 📖 Overview

Enterprise organizations often have thousands of pages of internal documentation such as:

- Employee Handbooks
- HR Policies
- API Documentation
- Engineering Design Documents
- Standard Operating Procedures (SOPs)
- Product Requirement Documents (PRDs)
- Technical Specifications
- User Manuals

Searching through these documents manually is time-consuming.

This project provides an AI-powered assistant that allows users to upload multiple PDF documents and ask natural language questions. The assistant retrieves the most relevant information using a Hybrid Retrieval pipeline and generates grounded answers with citations.

---

# ✨ Features

## Document Processing

- Upload multiple PDFs
- Automatic document parsing
- Intelligent text chunking
- Persistent vector database
- Metadata extraction
- Document indexing

---

## Retrieval Pipeline

- Dense Vector Search
- BM25 Keyword Search
- Hybrid Retrieval
- Duplicate Removal
- Cross-Encoder Reranking
- Context Selection

---

## AI Capabilities

- Retrieval-Augmented Generation (RAG)
- LangGraph Workflow
- Conversation Memory
- Source Citations
- Context-Aware Responses
- Hallucination Reduction

---

## Backend

- FastAPI REST APIs
- Modular Architecture
- Environment Configuration
- Logging
- Error Handling

---

## Frontend

- Streamlit UI
- Chat Interface
- PDF Upload
- Chat History
- Source References

---

## DevOps

- Docker
- Docker Compose
- Environment Variables
- Ready for CI/CD

---

# 🏗 Architecture

```text
                  User
                    │
                    ▼
             Streamlit Frontend
                    │
                    ▼
               FastAPI Backend
                    │
                    ▼
             LangGraph Workflow
                    │
        ┌───────────┴────────────┐
        │                        │
        ▼                        ▼
 Document Upload           Chat Request
        │                        │
        ▼                        ▼
 PDF Loader             Hybrid Retrieval
        │                        │
        ▼                        ▼
 Chunking          Dense + BM25 Retrieval
        │                        │
        ▼                        ▼
 Embeddings             Cross Encoder
        │                        │
        ▼                        ▼
 ChromaDB                 LiteLLM
        │                        │
        └──────────────┬─────────┘
                       ▼
                     LLM
                       │
                 Source Citations
                       │
                       ▼
                  Final Response
```

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| Workflow | LangGraph |
| LLM Framework | LangChain |
| LLM Gateway | LiteLLM |
| Embeddings | OpenAI Embeddings |
| Vector Database | ChromaDB |
| Retrieval | Hybrid Search |
| Sparse Retrieval | BM25 |
| Dense Retrieval | Chroma |
| Reranker | BAAI/bge-reranker-base |
| PDF Loader | PyMuPDF |
| Deployment | Docker |
| Evaluation | RAGAS (Planned) |
| Experiment Tracking | MLflow (Planned) |

---

# 📂 Project Structure

```text
app/
├── api/
├── core/
├── graph/
├── rag/
├── services/
├── schemas/
├── utils/
└── main.py

frontend/

data/

chroma_db/

Dockerfile

docker-compose.yml
```

---

# 🚀 Current Features

- [x] Multi PDF Upload
- [x] PDF Parsing
- [x] Text Chunking
- [x] Embedding Generation
- [x] Chroma Vector Store
- [x] Basic RAG Chat
- [x] FastAPI Backend
- [x] Streamlit UI
- [x] Docker Support

---

# 🔄 Upcoming Features

- [ ] LangGraph Workflow
- [ ] Hybrid Retrieval
- [ ] BM25 Retriever
- [ ] Cross Encoder Reranker
- [ ] Conversation Memory
- [ ] Source Citations
- [ ] Chat History
- [ ] LiteLLM Integration
- [ ] Prompt Caching
- [ ] Guardrails
- [ ] MLflow Tracking
- [ ] RAGAS Evaluation
- [ ] Observability
- [ ] Authentication
- [ ] CI/CD Pipeline

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /upload | Upload one or more PDF documents |
| POST | /chat | Ask questions over uploaded documents |
| GET | /history | Retrieve conversation history |
| DELETE | /history | Clear conversation history |

---

# 🎯 Future Improvements

- Multi-user support
- Redis Chat Memory
- PostgreSQL Metadata Storage
- FAISS Support
- Pinecone Support
- Azure OpenAI
- AWS Bedrock
- Evaluation Dashboard
- Kubernetes Deployment
- Monitoring Dashboard
- Feedback Collection
- Role-Based Access Control

---

# 📸 Screenshots

Coming Soon...

---

# 🤝 Contributing

Contributions are welcome!

Feel free to open issues and submit pull requests.

---

# 📜 License

MIT License
