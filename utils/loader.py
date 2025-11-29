# utils/loader.py
from pypdf import PdfReader #type:ignore

def load_pdfs_from_paths(paths):
    documents = []
    for path in paths:
        try:
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            if text.strip():
                documents.append(text)
        except Exception as e:
            print(f"Error reading {path}: {e}")
    return documents

