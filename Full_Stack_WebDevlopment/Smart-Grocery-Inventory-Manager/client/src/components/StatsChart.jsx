import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function StatsChart({ items }) {
  const data = Object.values(
    items.reduce((acc, item) => {
      if (!acc[item.category]) {
        acc[item.category] = { category: item.category, count: 0 };
      }
      acc[item.category].count += 1;
      return acc;
    }, {}),
  );

  return (
    <div className="bg-white p-4 rounded-xl shadow mb-6 text-black">
      <h2 className="text-lg font-bold mb-4">📊 Category Analytics</h2>

      <ResponsiveContainer width="100%" height={250}>
        <BarChart data={data}>
          <XAxis dataKey="category" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="count" fill="#22c55e" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default StatsChart;
