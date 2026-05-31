import { useNavigate } from "react-router-dom";

export default function Login() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: "linear-gradient(135deg, #1e1b4b 0%, #312e81 100%)",
        padding: "20px",
      }}
    >
      <div className="card" style={{ width: "100%", maxWidth: "400px" }}>
        <div style={{ textAlign: "center", marginBottom: "32px" }}>
          <h1
            style={{
              fontSize: "32px",
              fontWeight: "800",
              background: "linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)",
              WebkitBackgroundClip: "text",
              WebkitTextFillColor: "transparent",
              marginBottom: "8px",
            }}
          >
            💰 ExpenseTrack
          </h1>
          <p style={{ color: "#64748b" }}>
            Take control of your finances
          </p>
        </div>

        <button
          className="btn btn-primary"
          style={{ width: "100%", padding: "14px" }}
          onClick={() => navigate("/dashboard")}
        >
          Get Started →
        </button>
      </div>
    </div>
  );
}
