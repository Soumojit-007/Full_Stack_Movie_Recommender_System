import os
import json
import re
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # stable free model
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.4,
    timeout=60,
)

prompt = PromptTemplate(
    input_variables=["query"],
    template="""
User searched for: {query}

Recommend 5 similar MOVIES.
They can be from ANY country or language (Hollywood, Bollywood, Korean, etc).

Return ONLY valid JSON:

[
  {{
    "title": "...",
    "language": "...",
    "reason": "..."
  }},
  {{
    "title": "...",
    "language": "...",
    "reason": "..."
  }}
]
"""
)


def extract_json(text: str):
    match = re.search(r"\[.*\]", text, re.S)
    if match:
        return match.group()
    return None


def genai_recommend(query: str):
    try:
        chain = prompt | llm
        response = chain.invoke({"query": query})

        text = response.content.strip()

        json_text = extract_json(text)
        if json_text:
            return json.loads(json_text)

        # fallback: return empty list instead of breaking UI
        return []

    except Exception as e:
        print("GenAI error:", e)
        return []
