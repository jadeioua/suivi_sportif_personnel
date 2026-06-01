import { useEffect, useState } from "react";

function Objectifs() {
  const [objectifs, setObjectifs] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/objectifs")
      .then((response) => response.json())
      .then((data) => setObjectifs(data));
  }, []);

  return (
    <div>
      <h1>Objectifs</h1>

      {objectifs.map((objectif) => (
        <div key={objectif.id}>
          <p>Objectif #{objectif.id}</p>
          <p>Valeur cible : {objectif.valeur_cible}</p>
          <p>Unité : {objectif.unite}</p>
          <p>Date limite : {objectif.date_limite}</p>

          <p>
            Statut :
            {objectif.atteint ? " Atteint" : " En cours"}
          </p>

          <hr />
        </div>
      ))}
    </div>
  );
}

export default Objectifs;