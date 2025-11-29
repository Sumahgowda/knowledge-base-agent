# knowledge-base-agent
Knowledge Base QA Agent

(FAISS Vector Search + HuggingFace LLM + Streamlit UI)

📘 1. Overview

This project is an AI-powered Question Answering Agent that can read and understand PDF documents uploaded by the user. It extracts text, converts it into vector embeddings using MiniLM, stores them in a FAISS vector index, and finally answers user questions using Llama-3.1 (HuggingFace Inference API).

The agent answers only from the uploaded documents, making it useful for:

Academic notes summarization

Company knowledge bases

Research paper assistance

Policy / legal document querying

Personal document search

⭐ 2. Features
✅ PDF Upload & Text Extraction

Upload multiple PDF files

Automatic text extraction using PyPDF

✅ Vector Embedding & Indexing

Converts text into embeddings using Sentence-Transformers (all-MiniLM-L6-v2)

FAISS used to build efficient similarity search index

✅ Question Answering

Retrieves most relevant document chunks

Uses Llama-3.1 (8B Instruct) via HuggingFace API to generate the final answer

✅ Modern Streamlit UI

Clean tab-based interface

“Upload & Index” and “Ask Questions” workflow

✅ Secure API Handling

HuggingFace key stored in Streamlit Secrets or .env

⚠️ 3. Limitations
Limitation	Description
❌ Token Restrictions	HF API limits context size and max tokens
❌ Not Suitable for Very Large PDFs	Long PDFs increase embedding size & memory load
❌ Simple Retrieval	No chunking, only whole-PDF embeddings unless modified
🧰 4. Tech Stack & APIs Used
🔹 Frontend / UI

Streamlit (1.31)

🔹 Embeddings

Sentence-Transformers (all-MiniLM-L6-v2)

torch

🔹 Vector Database

FAISS-CPU
Used for fast similarity search

🔹 Large Language Model (LLM)

Llama-3.1-8B-Instruct
via HuggingFace Inference Chat Completions API
Endpoint:
https://router.huggingface.co/v1/chat/completions

🔹 PDF Reader

PyPDF

🔹 Supporting Libraries

numpy

pandas

scikit-learn

requests

tqdm

python-dotenv

🛠️ 5. Setup & Run Instructions (LOCAL)
Step 1: Clone the repository
git clone https://github.com/Sumahgowda/knowledge-base-agent
cd knowledge-base-agent

Step 2: Create a virtual environment
Windows:
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Add your HuggingFace API key

Create .env file:

HF_API_KEY=your_api_key_here

Step 5: Run the app
streamlit run app.py

🌐 6. Deployment Instructions (Streamlit Cloud)

Push your project to GitHub

Go to https://share.streamlit.io

Select your repository

Add secrets:

Settings → Secrets

HF_API_KEY="your_key_here"


Deploy
Your app will run at a public URL like:
https://<your-app-name>.streamlit.app

🚀 7. Potential Improvements
Area	Enhancement Idea
📄 PDF Chunking	Split PDFs into smaller text chunks for better retrieval
🧠 Better Embeddings	Use BERT-base or E5-large for improved accuracy
🔎 Metadata Search	Add keyword search + semantic hybrid search
🧰 Multi-file Support	Add document titles and per-file context
🗂️ Persistent Storage	Use a database (SQLite, Supabase, Pinecone)
🔒 Authentication	Add login for private document use
🎤 Multimodal Input	Support audio and image documents
📊 UI Improvements	Add history, citations, and confidence scores
📝 8. Conclusion

This project showcases a full end-to-end Retrieval-Augmented QA system (RAG) built with modern tools like FAISS, Sentence-Transformers, and Llama-3.1.
It is lightweight, practical, and easily extendable for academic or enterprise use.
