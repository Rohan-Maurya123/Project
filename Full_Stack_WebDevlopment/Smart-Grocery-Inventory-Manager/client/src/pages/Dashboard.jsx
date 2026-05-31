import { useEffect, useState } from "react";
import API from "../services/api";
import Navbar from "../components/Navbar";
import AddItem from "../components/AddItem";
import Sidebar from "../components/Sidebar";
import StatsChart from "../components/StatsChart";

function Dashboard() {
  const [items, setItems] = useState([]);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");

  const [darkMode, setDarkMode] = useState(false);

  const [editItem, setEditItem] = useState(null);
  const [editQuantity, setEditQuantity] = useState("");

  const fetchItems = async () => {
    try {
      const res = await API.get("/items");
      setItems(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    fetchItems();
  }, []);

  const isLowStock = (item) => item.quantity <= item.minStock;

  const handleUpdate = async (id) => {
    try {
      await API.put(`/items/${id}`, {
        quantity: editQuantity,
      });

      setEditItem(null);
      setEditQuantity("");
      fetchItems();
    } catch (err) {
      console.log(err);
    }
  };

  const handleDelete = async (id) => {
    try {
      await API.delete(`/items/${id}`);
      fetchItems();
    } catch (err) {
      console.log(err);
    }
  };

  const filteredItems = items.filter((item) => {
    const matchSearch = item.name.toLowerCase().includes(search.toLowerCase());

    const matchCategory = category === "All" || item.category === category;

    return matchSearch && matchCategory;
  });

  const expiringItems = items.filter((item) => {
    if (!item.expiryDate) return false;
    const today = new Date();
    const expiry = new Date(item.expiryDate);
    const diff = (expiry - today) / (1000 * 60 * 60 * 24);
    return diff <= 5;
  });

  // THEME SYSTEM (FIXED)
  const bgMain = darkMode ? "bg-gray-900 text-white" : "bg-gray-100 text-black";

  const card = darkMode ? "bg-gray-800 text-white" : "bg-white text-black";

  const tableBg = darkMode ? "bg-gray-800 text-white" : "bg-white text-black";

  const headerBg = darkMode
    ? "bg-gray-700 text-white"
    : "bg-gray-200 text-black";

  return (
    <div className={`${bgMain} min-h-screen flex`}>
      <Sidebar darkMode={darkMode} />

      <div className="flex-1 ml-64">
        <Navbar darkMode={darkMode} setDarkMode={setDarkMode} />

        <div className="p-6">
          {/* EXPIRY ALERT */}
          {expiringItems.length > 0 && (
            <div className="bg-yellow-100 border-l-4 border-yellow-500 p-4 mb-4 rounded text-black">
              <h2 className="font-bold text-yellow-700">
                ⚠ Expiring Soon Items
              </h2>

              {expiringItems.map((item) => (
                <p key={item._id}>
                  {item.name} → expires on {item.expiryDate.split("T")[0]}
                </p>
              ))}
            </div>
          )}

          {/* STATS */}
          <div className="grid grid-cols-3 gap-4 mb-6">
            <div className={`${card} p-5 rounded-xl shadow`}>
              <h2 className="text-gray-400">Total Items</h2>
              <p className="text-2xl font-bold">{items.length}</p>
            </div>

            <div className={`${card} p-5 rounded-xl shadow`}>
              <h2 className="text-gray-400">Low Stock</h2>
              <p className="text-2xl font-bold text-red-500">
                {items.filter(isLowStock).length}
              </p>
            </div>

            <div className={`${card} p-5 rounded-xl shadow`}>
              <h2 className="text-gray-400">Categories</h2>
              <p className="text-2xl font-bold">
                {new Set(items.map((i) => i.category)).size}
              </p>
            </div>
          </div>

          {/* CHART */}
          <StatsChart items={items} />

          {/* ADD ITEM */}
          <AddItem refresh={fetchItems} darkMode={darkMode} />

          {/* FILTERS */}
          <div className="flex gap-4 mb-4">
            <select
              value={category}
              onChange={(e) => setCategory(e.target.value)}
              className={`p-2 border rounded 
              ${darkMode ? "bg-gray-700 text-white" : "bg-white text-black"}`}
            >
              <option value="All">All</option>
              {[...new Set(items.map((i) => i.category))].map((cat) => (
                <option key={cat} value={cat}>
                  {cat}
                </option>
              ))}
            </select>

            <input
              type="text"
              placeholder="Search items..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className={`w-full p-2 border rounded
              ${darkMode ? "bg-gray-700 text-white" : "bg-white text-black"}`}
            />
          </div>

          {/* TABLE */}
          <div className={`${tableBg} rounded-xl shadow overflow-hidden`}>
            <table className="w-full">
              <thead className={headerBg}>
                <tr>
                  <th className="p-3">Name</th>
                  <th className="p-3">Category</th>
                  <th className="p-3">Quantity</th>
                  <th className="p-3">Status</th>
                  <th className="p-3">Actions</th>
                </tr>
              </thead>

              <tbody>
                {filteredItems.map((item) => (
                  <tr key={item._id} className="border-b">
                    <td className="p-3">{item.name}</td>

                    <td className="p-3">{item.category}</td>

                    <td className="p-3">
                      {editItem === item._id ? (
                        <input
                          type="number"
                          value={editQuantity}
                          onChange={(e) => setEditQuantity(e.target.value)}
                          className={`border p-1 w-20
                          ${darkMode ? "bg-gray-700 text-white" : "bg-white text-black"}`}
                        />
                      ) : (
                        item.quantity
                      )}
                    </td>

                    <td className="p-3">
                      {isLowStock(item) ? (
                        <span className="bg-red-100 text-red-600 px-2 py-1 rounded">
                          Low Stock
                        </span>
                      ) : (
                        <span className="bg-green-100 text-green-600 px-2 py-1 rounded">
                          OK
                        </span>
                      )}
                    </td>

                    <td className="p-3 flex gap-2">
                      {editItem === item._id ? (
                        <>
                          <button
                            onClick={() => handleUpdate(item._id)}
                            className="bg-green-500 text-white px-2 py-1 rounded"
                          >
                            Save
                          </button>

                          <button
                            onClick={() => setEditItem(null)}
                            className="bg-gray-400 text-white px-2 py-1 rounded"
                          >
                            Cancel
                          </button>
                        </>
                      ) : (
                        <>
                          <button
                            onClick={() => {
                              setEditItem(item._id);
                              setEditQuantity(item.quantity);
                            }}
                            className="bg-blue-500 text-white px-2 py-1 rounded"
                          >
                            Edit
                          </button>

                          <button
                            onClick={() => handleDelete(item._id)}
                            className="bg-red-500 text-white px-2 py-1 rounded"
                          >
                            Delete
                          </button>
                        </>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
