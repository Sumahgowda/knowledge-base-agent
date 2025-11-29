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


Installation & Running Locally
Follow these steps to test and run the project on your machine.
1️⃣ Clone the Repository
git clone https://github.com/Sumahgowda/knowledge-base-agent
cd knowledge-base-agent
2️⃣ Create and Activate Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Mac/Linux
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add Environment Variables
Create a .env file in the project root:
HF_API_KEY=your_huggingface_api_key
You can get the API key from:
🔗 https://huggingface.co/settings/tokens
5️⃣ Run the App
streamlit run app.py

