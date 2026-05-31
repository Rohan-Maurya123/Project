function StatsCard({ title, value }) {
  return (
    <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-3xl p-6 shadow-xl">
      <h3 className="text-gray-400">{title}</h3>

      <h1 className="text-5xl font-bold mt-4">{value}</h1>
    </div>
  );
}

export default StatsCard;
