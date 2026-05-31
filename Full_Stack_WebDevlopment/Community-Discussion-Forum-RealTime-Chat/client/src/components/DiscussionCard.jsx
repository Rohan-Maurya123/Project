function DiscussionCard({ title, description }) {
  return (
    <div className="bg-slate-900 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300 cursor-pointer">
      <h2 className="text-2xl font-bold">{title}</h2>

      <p className="text-gray-400 mt-3">{description}</p>

      <div className="mt-4 flex gap-3">
        <span className="bg-cyan-500 px-3 py-1 rounded-full">Discussion</span>
      </div>
    </div>
  );
}

export default DiscussionCard;
