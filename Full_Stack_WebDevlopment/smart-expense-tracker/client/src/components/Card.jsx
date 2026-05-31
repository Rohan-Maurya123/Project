export default function Card({ title, value, icon, color = "primary" }) {
  const colors = {
    primary: "linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)",
    success: "linear-gradient(135deg, #10b981 0%, #059669 100%)",
    danger: "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)",
    warning: "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)",
  };

  return (
    <div className="card fade-in" style={{ flex: 1 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
        <div>
          <p style={{ fontSize: "14px", color: "#64748b", marginBottom: "8px" }}>
            {title}
          </p>
          <h2
            style={{
              fontSize: "32px",
              fontWeight: "800",
              color: "#1e293b",
            }}
          >
            ${value.toLocaleString()}
          </h2>
        </div>
        {icon && (
          <div
            style={{
              width: "56px",
              height: "56px",
              borderRadius: "12px",
              background: colors[color],
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: "28px",
            }}
          >
            {icon}
          </div>
        )}
      </div>
    </div>
  );
}
