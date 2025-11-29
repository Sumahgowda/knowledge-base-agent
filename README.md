# knowledge-base-agent
Knowledge Base QA Agent (FAISS + HuggingFace + Streamlit)

A smart Question-Answering system that lets you upload PDFs, extracts their content, builds a FAISS vector index, and uses Llama-3.1 (HuggingFace API) to answer questions only from your documents.
 Features
 Upload multiple PDF documents
 Automatic text extraction
 FAISS vector similarity search
 MiniLM sentence embeddings
 Llama-3.1 generated answers
 Modern Streamlit UI
 Secure HuggingFace API key usage
 Fast and lightweight

 knowledge-base-agent/
│
├── app.py
├── requirements.txt
│
├── utils/
│   ├── loader.py
│   ├── embed_store.py
│   ├── qa.py
│   ├── hf_api.py
│
├── data/                 # auto-created when PDFs are uploaded
│   └── .gitkeep
│
└── README.md


