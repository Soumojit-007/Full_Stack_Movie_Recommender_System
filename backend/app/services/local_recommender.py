import pickle
import difflib

movies = pickle.load(open("app/models/movies.pkl", "rb"))
similarity = pickle.load(open("app/models/similarity.pkl", "rb"))

movies.reset_index(drop=True, inplace=True)

titles = movies["title"].astype(str).tolist()
titles_lower = [t.lower().strip() for t in titles]


def find_movie_index(query: str):
    q = query.lower().strip()

    if q in titles_lower:
        return titles_lower.index(q)

    close = difflib.get_close_matches(q, titles_lower, n=1, cutoff=0.6)
    if close:
        return titles_lower.index(close[0])

    return None


def recommend_by_person(name: str, top_n=5):
    person = name.lower().strip()

    matches = movies[movies["tags"].str.lower().str.contains(person, na=False)]

    if matches.empty:
        return []

    return [
        {"title": row.title, "score": None}
        for _, row in matches.head(top_n).iterrows()
    ]


def local_recommend(query: str, top_n: int = 5):

    idx = find_movie_index(query)

    # 🎬 Similar movies
    if idx is not None:
        sim_scores = list(enumerate(similarity[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1: top_n + 1]

        results = [
            {"title": movies.iloc[i].title, "score": float(round(score, 3))}
            for i, score in sim_scores
        ]
        print("Query:", query, "Index:", idx)
        return results
        


    # 🎭 Actor / Director via tags
    person_results = recommend_by_person(query, top_n)
    if person_results:
        return person_results

    return []

print("Movies shape:", movies.shape)
print("Similarity shape:", len(similarity), len(similarity[0]))
print("First titles:", movies["title"].head().tolist())

