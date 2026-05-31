import { useState, useEffect } from "react";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Doughnut } from "react-chartjs-2";
import { TransactionService } from "../services/transactionService";

ChartJS.register(ArcElement, Tooltip, Legend);

export default function Analytics() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    setTransactions(TransactionService.getAll());
  }, []);

  const expensesByCategory = transactions
    .filter(t => t.type === "expense")
    .reduce((acc, t) => {
      acc[t.category] = (acc[t.category] || 0) + Number(t.amount);
      return acc;
    }, {});

  const data = {
    labels: Object.keys(expensesByCategory),
    datasets: [
      {
        data: Object.values(expensesByCategory),
        backgroundColor: [
          "#6366f1",
          "#10b981",
          "#f59e0b",
          "#ef4444",
          "#8b5cf6",
          "#ec4899",
        ],
        borderWidth: 2,
        borderColor: "#fff",
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: "bottom",
      },
    },
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
        Analytics
      </h1>

      <div style={{ display: "grid", gap: "24px" }}>
        <div className="card fade-in" style={{ height: "400px" }}>
          <h3 style={{ marginBottom: "16px", color: "#1e293b" }}>
            Expenses by Category
          </h3>
          <div style={{ height: "340px" }}>
            {Object.keys(expensesByCategory).length > 0 ? (
              <Doughnut data={data} options={options} />
            ) : (
              <div
                style={{
                  height: "100%",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  color: "#64748b",
                }}
              >
                No expenses yet! Add some transactions to see analytics.
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
