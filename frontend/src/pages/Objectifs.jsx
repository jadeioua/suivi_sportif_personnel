import { useEffect, useState } from "react";

function Objectifs() {
  const [objectifs, setObjectifs] = useState([]);
  const [valeurCible, setValeurCible] = useState("");
  const [dateLimite, setDateLimite] = useState("");

  const chargerObjectifs = () => {
    fetch("http://127.0.0.1:5000/objectifs")
      .then((response) => response.json())
      .then((data) => setObjectifs(data));
  };

  useEffect(() => {
    chargerObjectifs();
  }, []);

  const ajouterObjectif = async (e) => {
    e.preventDefault();

    const nouvelObjectif = {
      sportif_id: 2,
      type_exercice_id: 1,
      valeur_cible: Number(valeurCible),
      unite: "km",
      date_limite: dateLimite
    };

    const response = await fetch("http://127.0.0.1:5000/objectifs", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(nouvelObjectif)
    });

    if (response.ok) {
      setValeurCible("");
      setDateLimite("");
      chargerObjectifs();
    }
  };

  const marquerAtteint = async (id) => {
    await fetch(`http://127.0.0.1:5000/objectifs/${id}`, {
      method: "PUT"
    });

    chargerObjectifs();
  };

  return (
    <div>
      <h1>Objectifs</h1>

      <form onSubmit={ajouterObjectif}>
        <input
          type="number"
          placeholder="Valeur cible"
          value={valeurCible}
          onChange={(e) => setValeurCible(e.target.value)}
        />

        <br /><br />

        <input
          type="date"
          value={dateLimite}
          onChange={(e) => setDateLimite(e.target.value)}
        />

        <br /><br />

        <button type="submit">Ajouter objectif</button>
      </form>

      <hr />

      {objectifs.map((objectif) => (
        <div key={objectif.id}>
          <p>Objectif #{objectif.id}</p>
          <p>Valeur cible : {objectif.valeur_cible}</p>
          <p>Unité : {objectif.unite}</p>
          <p>Date limite : {objectif.date_limite}</p>
          <p>Statut : {objectif.atteint ? "Atteint" : "En cours"}</p>

          {!objectif.atteint && (
            <button onClick={() => marquerAtteint(objectif.id)}>
              Marquer comme atteint
            </button>
          )}

          <hr />
        </div>
      ))}
    </div>
  );
}

export default Objectifs;

