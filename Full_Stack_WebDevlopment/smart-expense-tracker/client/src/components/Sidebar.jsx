import { Link, useLocation } from "react-router-dom";

export default function Sidebar() {
  const location = useLocation();

  const menuItems = [
    { path: "/dashboard", label: "Dashboard", icon: "📊" },
    { path: "/transactions", label: "Transactions", icon: "💰" },
    { path: "/budget", label: "Budget", icon: "🎯" },
    { path: "/analytics", label: "Analytics", icon: "📈" },
  ];

  return (
    <div
      style={{
        width: "260px",
        height: "100vh",
        background: "linear-gradient(180deg, #1e1b4b 0%, #312e81 100%)",
        color: "white",
        padding: "24px 20px",
        display: "flex",
        flexDirection: "column",
        position: "sticky",
        top: 0,
        left: 0,
      }}
    >
      <div style={{ marginBottom: "40px" }}>
        <h2
          style={{
            fontSize: "24px",
            fontWeight: "700",
            background: "linear-gradient(135deg, #a78bfa 0%, #818cf8 100%)",
            WebkitBackgroundClip: "text",
            WebkitTextFillColor: "transparent",
          }}
        >
          💰 ExpenseTrack
        </h2>
        <p style={{ color: "#a5b4fc", fontSize: "13px", marginTop: "4px" }}>
          Manage your finances
        </p>
      </div>

      <nav style={{ flex: 1 }}>
        {menuItems.map((item) => (
          <Link
            key={item.path}
            to={item.path}
            style={{
              display: "flex",
              alignItems: "center",
              gap: "12px",
              padding: "14px 16px",
              borderRadius: "12px",
              marginBottom: "8px",
              color: location.pathname === item.path ? "white" : "#c7d2fe",
              textDecoration: "none",
              fontWeight: location.pathname === item.path ? "600" : "400",
              background:
                location.pathname === item.path
                  ? "rgba(129, 140, 248, 0.2)"
                  : "transparent",
              transition: "all 0.3s ease",
            }}
            onMouseEnter={(e) => {
              if (location.pathname !== item.path) {
                e.target.style.background = "rgba(129, 140, 248, 0.1)";
              }
            }}
            onMouseLeave={(e) => {
              if (location.pathname !== item.path) {
                e.target.style.background = "transparent";
              }
            }}
          >
            <span style={{ fontSize: "20px" }}>{item.icon}</span>
            <span style={{ fontSize: "15px" }}>{item.label}</span>
          </Link>
        ))}
      </nav>
    </div>
  );
}
