export default function TransactionTable({ data, onDelete }) {
  return (
    <div className="card fade-in" style={{ overflowX: "auto" }}>
      <h3 style={{ marginBottom: "20px", color: "#1e293b" }}>
        Recent Transactions
      </h3>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr style={{ borderBottom: "2px solid #e2e8f0" }}>
            <th
              style={{
                textAlign: "left",
                padding: "14px 16px",
                color: "#64748b",
                fontSize: "13px",
                fontWeight: "600",
                textTransform: "uppercase",
              }}
            >
              Type
            </th>
            <th
              style={{
                textAlign: "left",
                padding: "14px 16px",
                color: "#64748b",
                fontSize: "13px",
                fontWeight: "600",
                textTransform: "uppercase",
              }}
            >
              Amount
            </th>
            <th
              style={{
                textAlign: "left",
                padding: "14px 16px",
                color: "#64748b",
                fontSize: "13px",
                fontWeight: "600",
                textTransform: "uppercase",
              }}
            >
              Category
            </th>
            <th
              style={{
                textAlign: "left",
                padding: "14px 16px",
                color: "#64748b",
                fontSize: "13px",
                fontWeight: "600",
                textTransform: "uppercase",
              }}
            >
              Action
            </th>
          </tr>
        </thead>
        <tbody>
          {data.map((t, index) => (
            <tr
              key={t.id}
              style={{
                borderBottom: "1px solid #f1f5f9",
                transition: "background 0.2s ease",
              }}
              onMouseEnter={(e) => (e.currentTarget.style.background = "#f8fafc")}
              onMouseLeave={(e) => (e.currentTarget.style.background = "transparent")}
            >
              <td style={{ padding: "14px 16px" }}>
                <span
                  style={{
                    padding: "6px 12px",
                    borderRadius: "20px",
                    fontSize: "12px",
                    fontWeight: "600",
                    textTransform: "uppercase",
                    background:
                      t.type === "income"
                        ? "rgba(16, 185, 129, 0.1)"
                        : "rgba(239, 68, 68, 0.1)",
                    color:
                      t.type === "income" ? "#059669" : "#dc2626",
                  }}
                >
                  {t.type}
                </span>
              </td>
              <td
                style={{
                  padding: "14px 16px",
                  fontSize: "16px",
                  fontWeight: "600",
                  color: t.type === "income" ? "#059669" : "#dc2626",
                }}
              >
                {t.type === "income" ? "+" : "-"}${Number(t.amount).toLocaleString()}
              </td>
              <td style={{ padding: "14px 16px", color: "#64748b" }}>
                {t.category}
              </td>
              <td style={{ padding: "14px 16px" }}>
                <button
                  className="btn btn-danger"
                  style={{ padding: "6px 12px", fontSize: "12px" }}
                  onClick={() => onDelete(t.id)}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
