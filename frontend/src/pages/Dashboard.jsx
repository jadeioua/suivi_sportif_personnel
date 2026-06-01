import { useEffect, useState } from "react";

function Dashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/sportifs/2/stats")
      .then((response) => response.json())
      .then((data) => setStats(data));
  }, []);

  if (!stats) {
    return <h2>Chargement...</h2>;
  }

  return (
    <div>
      <h1>Suivi Sportif Personnel</h1>

      <h2>
        {stats.sportif.prenom} {stats.sportif.nom}
      </h2>

      <p>Total séances : {stats.total_seances}</p>
      <p>Durée totale : {stats.duree_totale} min</p>
      <p>Durée moyenne : {stats.duree_moyenne} min</p>
      <p>Exercices distincts : {stats.exercices_distincts}</p>
    </div>
  );
}

export default Dashboard;