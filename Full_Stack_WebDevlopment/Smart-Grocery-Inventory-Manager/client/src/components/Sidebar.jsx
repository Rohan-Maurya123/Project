import { useNavigate } from "react-router-dom";

function Sidebar() {
  const navigate = useNavigate();

  return (
    <div className="w-64 h-screen fixed left-0 top-0 p-6 shadow-lg bg-white dark:bg-gray-800 dark:text-white">
      <h1 className="text-2xl font-bold text-green-500 mb-8">
        🛒 Grocery SaaS
      </h1>

      <ul className="space-y-4 font-medium">
        <li
          onClick={() => navigate("/dashboard")}
          className="hover:text-green-500 cursor-pointer"
        >
          📊 Dashboard
        </li>

        <li
          onClick={() => navigate("/inventory")}
          className="hover:text-green-500 cursor-pointer"
        >
          📦 Inventory
        </li>

        <li
          onClick={() => navigate("/alerts")}
          className="hover:text-green-500 cursor-pointer"
        >
          ⚠ Alerts
        </li>
      </ul>
    </div>
  );
}

export default Sidebar;
