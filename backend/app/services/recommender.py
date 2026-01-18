from app.services.local_recommender import local_recommend
from app.services.genai_recommender import genai_recommend


def recommend(query: str, top_n: int = 5, source: str = "auto"):

    # 🔥 Force dataset only
    if source == "dataset":
        data = local_recommend(query, top_n)
        return {
            "source": "dataset",
            "recommendations": data
        }

    # 🤖 Force GenAI only
    if source == "genai":
        data = genai_recommend(query)
        return {
            "source": "genai",
            "recommendations": data
        }

    # ⚡ AUTO MODE: try dataset first
    data = local_recommend(query, top_n)

    if data and len(data) > 0:
        return {
            "source": "dataset",
            "recommendations": data
        }

    # 🤖 Fallback to GenAI
    data = genai_recommend(query)
    return {
        "source": "genai",
        "recommendations": data
    }
