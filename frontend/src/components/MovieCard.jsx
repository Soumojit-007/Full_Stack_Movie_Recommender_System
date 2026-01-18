export default function MovieCard({item}){
    return(
        <div className="card">
            <h3>🎬{item.title || item.name}</h3>
            {item.language && <p>Language : {item.language}</p>}
            {item.reason && <p>item.reason</p>}
            {item.score && <p>Similarity:{item.score}</p>}
        </div>
    )
}