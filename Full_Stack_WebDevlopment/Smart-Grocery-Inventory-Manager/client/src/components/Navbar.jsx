import { useContext } from "react";
import { ThemeContext } from "../context/ThemeContext";
import { useNavigate } from "react-router-dom";

function Navbar() {
  const { darkMode, setDarkMode } = useContext(ThemeContext);
  const navigate = useNavigate();

  return (
    <div className="flex justify-between items-center p-4 shadow bg-white dark:bg-gray-800 dark:text-white">
      <h1 className="text-xl font-bold text-green-500">🛒 Smart Grocery</h1>

      <div className="flex gap-3">
        <button
          onClick={() => setDarkMode(!darkMode)}
          className="px-3 py-1 rounded bg-gray-200 dark:bg-gray-700"
        >
          {darkMode ? "☀ Light" : "🌙 Dark"}
        </button>

        <button
          onClick={() => {
            localStorage.removeItem("token");
            navigate("/");
          }}
          className="bg-red-500 text-white px-3 py-1 rounded"
        >
          Logout
        </button>
      </div>
    </div>
  );
}

export default Navbar;
