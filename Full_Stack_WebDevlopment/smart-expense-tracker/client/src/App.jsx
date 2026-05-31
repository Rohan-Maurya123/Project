import AppRoutes from "./routes";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import { useLocation } from "react-router-dom";

export default function App() {
  const location = useLocation();
  const isAuthPage = location.pathname === "/" || location.pathname === "/register";

  return (
    <div style={{ display: "flex" }}>
      {!isAuthPage && <Sidebar />}
      <div style={{ flex: 1, minHeight: "100vh" }}>
        {!isAuthPage && <Navbar />}
        <AppRoutes />
      </div>
    </div>
  );
}
