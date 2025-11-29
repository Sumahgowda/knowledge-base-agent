import streamlit as st #type:ignore
import os
from utils.loader import load_pdfs_from_paths
from utils.embed_store import build_index
from utils.qa import answer_query

st.set_page_config(page_title="Knowledge Base Agent", layout="wide")

st.title("📚 Knowledge Base QA Agent (FAISS + HuggingFace)")

tab1, tab2 = st.tabs(["📤 Upload & Index Documents", "❓ Ask Questions"])

# ----------------------- UPLOAD SECTION -----------------------
with tab1:
    st.header("Upload PDFs to build knowledge base")

    uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

    if st.button("Build Index"):
        if not uploaded_files:
            st.error("Upload at least one PDF.")
        else:
            os.makedirs("data", exist_ok=True)
            file_paths = []

            for f in uploaded_files:
                path = os.path.join("data", f.name)
                with open(path, "wb") as out:
                    out.write(f.read())
                file_paths.append(path)

            docs = load_pdfs_from_paths(file_paths)
            if docs:
                build_index(docs)
                st.success("FAISS index created successfully!")
            else:
                st.error("Could not extract text.")

# ----------------------- QUERY SECTION ------------------------
with tab2:
    st.header("Ask a question from your Knowledge Base")

    if not os.path.exists("vector.index"):
        st.warning("⚠️ Please upload documents and build the index first.")
    else:
        query = st.text_input("Enter your question")

        if st.button("Get Answer"):
            if not query.strip():
                st.error("Please enter a question.")
            else:
                with st.spinner("Searching and answering..."):
                    answer = answer_query(query)
                st.subheader("📌 Answer")
                st.write(answer)
