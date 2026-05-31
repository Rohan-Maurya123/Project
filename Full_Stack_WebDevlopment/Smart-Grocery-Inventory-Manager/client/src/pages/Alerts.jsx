function Alerts() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">⚠ Alerts</h1>

      <p className="text-gray-500 dark:text-gray-300">
        Smart notifications for your stock
      </p>

      {/* Alert Cards */}
      <div className="space-y-4 mt-6">
        <div className="p-4 border-l-4 border-red-500 bg-red-50 dark:bg-gray-800 rounded">
          <h2 className="font-bold text-red-600">Low Stock Alert</h2>
          <p className="text-gray-600 dark:text-gray-300">
            Items below minimum threshold will appear here
          </p>
        </div>

        <div className="p-4 border-l-4 border-yellow-500 bg-yellow-50 dark:bg-gray-800 rounded">
          <h2 className="font-bold text-yellow-600">Expiry Alert</h2>
          <p className="text-gray-600 dark:text-gray-300">
            Products expiring within 5 days
          </p>
        </div>

        <div className="p-4 border-l-4 border-green-500 bg-green-50 dark:bg-gray-800 rounded">
          <h2 className="font-bold text-green-600">System Status</h2>
          <p className="text-gray-600 dark:text-gray-300">
            All inventory systems running normally
          </p>
        </div>
      </div>
    </div>
  );
}

export default Alerts;
