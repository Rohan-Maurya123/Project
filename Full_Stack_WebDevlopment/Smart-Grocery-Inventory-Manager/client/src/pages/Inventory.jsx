function Inventory() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">📦 Inventory</h1>

      <p className="text-gray-500 dark:text-gray-300">
        Manage your stock items efficiently
      </p>

      {/* Feature Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
        <div className="p-5 rounded-xl shadow bg-white dark:bg-gray-800 hover:scale-105 transition">
          <h2 className="text-xl font-bold">➕ Add Items</h2>
          <p className="text-gray-500 mt-2">
            Add new grocery items to your inventory
          </p>
        </div>

        <div className="p-5 rounded-xl shadow bg-white dark:bg-gray-800 hover:scale-105 transition">
          <h2 className="text-xl font-bold">✏ Edit Stock</h2>
          <p className="text-gray-500 mt-2">
            Update quantity, category, and expiry
          </p>
        </div>

        <div className="p-5 rounded-xl shadow bg-white dark:bg-gray-800 hover:scale-105 transition">
          <h2 className="text-xl font-bold">📊 Track Usage</h2>
          <p className="text-gray-500 mt-2">Monitor consumption patterns</p>
        </div>
      </div>

      {/* Empty State Style */}
      <div className="mt-10 p-6 border rounded-xl bg-gray-50 dark:bg-gray-900 text-center">
        <p className="text-gray-500">
          📦 Your inventory data is managed from the Dashboard
        </p>
      </div>
    </div>
  );
}

export default Inventory;
