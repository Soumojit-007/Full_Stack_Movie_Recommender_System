from fastapi import APIRouter, Query
from datetime import datetime
from app.services.recommender import recommend
from app.db.mongo import search_logs

router = APIRouter()


@router.get("/recommend")
def get_recommendations(
    query: str = Query(..., description="Movie / Actor / Director / Series"),
    top_n: int = 5,
    source: str = "auto"
):
    result = recommend(query, top_n, source)

    try:
        search_logs.insert_one({
            "query": query,
            "source": result["source"],
            "timestamp": datetime.utcnow()
        })
    except Exception as e:
        print("Mongo logging failed:", e)

    return result
