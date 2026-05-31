import { FaSearch, FaBell } from "react-icons/fa";

function Navbar() {
  return (
    <div className="h-20 bg-slate-900 border-b border-slate-800 flex items-center justify-between px-8">
      <div className="flex items-center bg-slate-800 rounded-xl px-4 py-3 w-96">
        <FaSearch />

        <input
          placeholder="Search discussions..."
          className="bg-transparent outline-none ml-3 w-full"
        />
      </div>

      <div className="flex items-center gap-6">
        <FaBell size={22} className="cursor-pointer" />

        <div className="w-12 h-12 rounded-full bg-cyan-500"></div>
      </div>
    </div>
  );
}

export default Navbar;
