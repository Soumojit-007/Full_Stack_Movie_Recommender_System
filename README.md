## 🎬 Movie Recommendation System
A full-stack movie recommendation system that combines content-based machine learning with GenAI fallback to provide recommendations even when the movie/person is not present in the dataset.

The system first tries to recommend using a trained similarity model on the TMDB dataset.
If no relevant match is found, it falls back to Gemini (Google Generative AI) to fetch recommendations dynamically.

