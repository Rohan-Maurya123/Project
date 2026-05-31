import { calculateExpense } from "../utils/helpers";
import { TransactionService } from "../services/transactionService";

export default function BudgetCard({ budget }) {
  const transactions = TransactionService.getAll();
  const spent = calculateExpense(transactions);
  const remaining = budget - spent;
  const percentage = budget > 0 ? Math.min((spent / budget) * 100, 100) : 0;
  const progressColor = percentage > 90 ? "#ef4444" : percentage > 70 ? "#f59e0b" : "#10b981";

  return (
    <div className="card fade-in">
      <h3 style={{ marginBottom: "20px", color: "#1e293b" }}>Budget Overview</h3>
      
      <div style={{ marginBottom: "20px" }}>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginBottom: "12px",
          }}
        >
          <span style={{ color: "#64748b", fontSize: "14px" }}>Spent</span>
          <span style={{ fontWeight: "700", color: "#1e293b" }}>
            ${spent.toLocaleString()} / ${budget.toLocaleString()}
          </span>
        </div>
        <div
          style={{
            height: "12px",
            background: "#e2e8f0",
            borderRadius: "6px",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              width: `${percentage}%`,
              height: "100%",
              background: `linear-gradient(90deg, ${progressColor} 0%, ${progressColor}aa 100%)`,
              borderRadius: "6px",
              transition: "width 0.5s ease",
            }}
          />
        </div>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "16px",
        }}
      >
        <div
          style={{
            padding: "16px",
            background: "rgba(239, 68, 68, 0.1)",
            borderRadius: "12px",
            textAlign: "center",
          }}
        >
          <p style={{ fontSize: "13px", color: "#64748b", marginBottom: "4px" }}>
            Spent
          </p>
          <p
            style={{
              fontSize: "20px",
              fontWeight: "800",
              color: "#dc2626",
            }}
          >
            ${spent.toLocaleString()}
          </p>
        </div>
        <div
          style={{
            padding: "16px",
            background: "rgba(16, 185, 129, 0.1)",
            borderRadius: "12px",
            textAlign: "center",
          }}
        >
          <p style={{ fontSize: "13px", color: "#64748b", marginBottom: "4px" }}>
            Remaining
          </p>
          <p
            style={{
              fontSize: "20px",
              fontWeight: "800",
              color: "#059669",
            }}
          >
            ${remaining.toLocaleString()}
          </p>
        </div>
      </div>
    </div>
  );
}
