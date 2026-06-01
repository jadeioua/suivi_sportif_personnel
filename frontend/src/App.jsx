import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import Seances from "./pages/Seances";
import Objectifs from "./pages/Objectifs";
import AjoutSeance from "./pages/AjoutSeance";
import "./App.css";


function App() {
  const [page, setPage] = useState("dashboard");

  return (
    <div>
      <button onClick={() => setPage("dashboard")}>
        Dashboard
      </button>

      <button onClick={() => setPage("seances")}>
        Séances
      </button>

      <button onClick={() => setPage("objectifs")}>
        Objectifs
      </button>

      <button onClick={() => setPage("ajout-seance")}>
        Ajouter séance
      </button>

      {page === "dashboard" && <Dashboard />}
      {page === "seances" && <Seances />}
      {page === "objectifs" && <Objectifs />}
      {page === "ajout-seance" && <AjoutSeance />}
    </div>
  );
}

export default App;