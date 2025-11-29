import requests #type:ignore
import os
from dotenv import load_dotenv #type:ignore
import os

env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(env_path)

HF_API_KEY = os.getenv("HF_API_KEY")

def query_hf(prompt: str) -> str:
    """Send prompt to HuggingFace Chat Completion API."""
    
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.2
    }

    response = requests.post(
        "https://router.huggingface.co/v1/chat/completions",
        json=payload,
        headers=headers,
        timeout=60
    )

    if response.status_code != 200:
        raise Exception(f"HF API Error {response.status_code}: {response.text}")

    return response.json()["choices"][0]["message"]["content"]