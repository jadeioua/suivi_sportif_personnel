import { useEffect, useState } from "react";

function Seances() {
  const [seances, setSeances] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/seances")
      .then((response) => response.json())
      .then((data) => setSeances(data));
  }, []);

  return (
    <div>
      <h1>Liste des séances</h1>

      {seances.map((seance) => (
        <div key={seance.id}>
          <h3>Séance #{seance.id}</h3>

          <p>Date : {seance.date}</p>
          <p>Durée : {seance.duree_minutes} min</p>
          <p>Note : {seance.note_ressenti}/5</p>
          <p>Commentaire : {seance.commentaire}</p>

          <hr />
        </div>
      ))}
    </div>
  );
}

export default Seances;