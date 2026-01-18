import MovieCard from "./MovieCard.jsx";

export default function MovieGrid({ results }) {

  if (!results || results.length === 0) {
    return <p className="text-center mt-4">No recommendations yet.</p>;
  }

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mt-6">
      {results.map((item, i) => (
        <MovieCard key={i} item={item} />
      ))}
    </div>
  );
}
