import { useState } from "react";
import SearchBar from "../components/SearchBar";
import MovieGrid from "../components/MovieGrid";
import Loader from "../components/Loader";
import { getRecommendations } from "../api/client";

export default function Home() {
  const [results, setResults] = useState([]);
  const [source, setSource] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async (query, src) => {
    try {
      setLoading(true);
      setResults([]);
      const res = await getRecommendations(query, src);

      setSource(res.data.source);
      setResults(res.data.recommendations);
    } catch (err) {
      alert("Error fetching recommendations");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <SearchBar onSearch={handleSearch} />

      {loading && <Loader />}

      {source && !loading && (
        <div className="source">Source: {source}</div>
      )}

      <MovieGrid results={results} />
    </>
  );
}
