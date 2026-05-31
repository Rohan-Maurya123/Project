export default function Navbar() {
  return (
    <div
      style={{
        background: "white",
        padding: "16px 32px",
        boxShadow: "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        borderBottom: "1px solid #e2e8f0",
      }}
    >
      <div>
        <h2 style={{ fontSize: "20px", fontWeight: "700", color: "#1e293b" }}>
          Welcome back! 👋
        </h2>
        <p style={{ fontSize: "13px", color: "#64748b", marginTop: "2px" }}>
          {new Date().toLocaleDateString("en-US", {
            weekday: "long",
            year: "numeric",
            month: "long",
            day: "numeric",
          })}
        </p>
      </div>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "12px",
        }}
      >
        <div
          style={{
            width: "40px",
            height: "40px",
            borderRadius: "50%",
            background: "linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "white",
            fontWeight: "700",
            fontSize: "16px",
          }}
        >
          U
        </div>
      </div>
    </div>
  );
}
