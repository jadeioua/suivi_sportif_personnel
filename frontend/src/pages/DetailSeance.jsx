import { useEffect, useState } from "react";

function DetailSeance({ seanceId }) {
  const [seance, setSeance] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/seances/${seanceId}`)
      .then((response) => response.json())
      .then((data) => setSeance(data));
  }, [seanceId]);

  if (!seance) {
    return <h2>Chargement...</h2>;
  }

  return (
    <div>
      <h1>Détail de la séance</h1>

      <p>Date : {seance.date}</p>
      <p>Durée : {seance.duree_minutes} min</p>
      <p>Note : {seance.note_ressenti}/5</p>
      <p>Commentaire : {seance.commentaire}</p>

      <h2>Exercices réalisés</h2>

      {seance.exercices.length === 0 ? (
        <p>Aucun exercice enregistré.</p>
      ) : (
        seance.exercices.map((exercice) => (
          <div key={exercice.id}>
            <p>Type exercice ID : {exercice.type_exercice_id}</p>
            <p>Distance : {exercice.distance_km} km</p>
            <p>Répétitions : {exercice.repetitions}</p>
            <p>Séries : {exercice.series}</p>
            <p>Durée : {exercice.duree_secondes} secondes</p>
            <hr />
          </div>
        ))
      )}
    </div>
  );
}

export default DetailSeance;