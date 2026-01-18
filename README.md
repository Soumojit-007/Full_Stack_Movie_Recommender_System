## 🎬 Movie Recommendation System
A full-stack movie recommendation system that combines content-based machine learning with GenAI fallback to provide recommendations even when the movie/person is not present in the dataset.

The system first tries to recommend using a trained similarity model on the TMDB dataset.
If no relevant match is found, it falls back to Gemini (Google Generative AI) to fetch recommendations dynamically.

## 🚀 Features

🔍 Search by movie name, actor, or director

🎯 Content-based recommendations using cosine similarity

🤖 GenAI fallback using Gemini API for unknown queries

📦 Dockerized backend with MongoDB logging

⚡ FastAPI REST backend

🎨 React + Vite frontend UI

## 🧠 Recommendation Logic

Try dataset-based recommendation using similarity matrix

If no good match is found → use Gemini API for recommendations

All searches are logged in MongoDB

## 🛠 Tech Stack
🧠 Machine Learning

Python

Pandas, NumPy

Scikit-learn (CountVectorizer, Cosine Similarity)

NLTK

⚙ Backend

FastAPI

LangChain

Google Gemini API

PyMongo (MongoDB)

Docker

🎨 Frontend

React (Vite)

Axios

Tailwind CSS

🗄 Database

MongoDB (Docker container)

## 📌 Dataset

Uses TMDB 5000 Movies Dataset:

tmdb_5000_movies.csv

tmdb_5000_credits.csv

Used only for training the ML model.

