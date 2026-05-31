import { useState, useEffect } from "react";
import BudgetCard from "../components/BudgetCard";
import { BudgetService } from "../services/budgetService";

export default function Budget() {
  const [budget, setBudget] = useState(0);
  const [tempBudget, setTempBudget] = useState("");

  useEffect(() => {
    setBudget(BudgetService.get());
    setTempBudget(BudgetService.get().toString());
  }, []);

  const handleSaveBudget = () => {
    const newBudget = Number(tempBudget);
    if (!isNaN(newBudget) && newBudget >= 0) {
      BudgetService.set(newBudget);
      setBudget(newBudget);
    }
  };

  return (
    <div style={{ padding: "32px" }}>
      <h1
        style={{
          fontSize: "28px",
          fontWeight: "800",
          color: "#1e293b",
          marginBottom: "24px",
        }}
      >
        Budget Management
      </h1>

      <div style={{ display: "grid", gap: "24px" }}>
        <div className="card fade-in">
          <h3 style={{ marginBottom: "20px", color: "#1e293b" }}>
            Set Monthly Budget
          </h3>
          <div style={{ display: "flex", gap: "12px" }}>
            <input
              type="number"
              className="input"
              style={{ flex: 1 }}
              placeholder="Enter your budget"
              value={tempBudget}
              onChange={(e) => setTempBudget(e.target.value)}
            />
            <button className="btn btn-primary" onClick={handleSaveBudget}>
              Save Budget
            </button>
          </div>
        </div>

        <BudgetCard budget={budget} />
      </div>
    </div>
  );
}
