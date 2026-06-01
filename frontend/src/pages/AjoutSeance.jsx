import { useState } from "react";

function AjoutSeance() {

  const [date, setDate] = useState("");
  const [duree, setDuree] = useState("");
  const [note, setNote] = useState("");
  const [commentaire, setCommentaire] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const nouvelleSeance = {
      sportif_id: 2,
      date: date,
      duree_minutes: Number(duree),
      note_ressenti: Number(note),
      commentaire: commentaire,
      exercices: []
    };

    const response = await fetch(
      "http://127.0.0.1:5000/seances",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(nouvelleSeance)
      }
    );

    if (response.ok) {
      alert("Séance ajoutée !");
    }
  };

  return (
    <div>
      <h1>Ajouter une séance</h1>

      <form onSubmit={handleSubmit}>

        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />

        <br /><br />

        <input
          type="number"
          placeholder="Durée (minutes)"
          value={duree}
          onChange={(e) => setDuree(e.target.value)}
        />

        <br /><br />

        <input
          type="number"
          min="1"
          max="5"
          placeholder="Note de ressenti"
          value={note}
          onChange={(e) => setNote(e.target.value)}
        />

        <br /><br />

        <textarea
          placeholder="Commentaire"
          value={commentaire}
          onChange={(e) => setCommentaire(e.target.value)}
        />

        <br /><br />

        <button type="submit">
          Ajouter
        </button>

      </form>
    </div>
  );
}

export default AjoutSeance;