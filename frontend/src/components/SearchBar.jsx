import { useState } from "react";

export default function SearchBar({ onSearch }) {
  const [query, setQuery] = useState("");
  const [source, setSource] = useState("auto");

  const submit = (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    onSearch(query, source);
  };

  return (
    <form className="search-box" onSubmit={submit}>
      <input
        placeholder="Movie / Actor / Director / Series..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button>Search</button>
    </form>
  );
}
