import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function CreateDiscussion() {
  return (
    <div className="flex min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-cyan-950 text-white">
      <Sidebar />

      <div className="flex-1">
        <Navbar />

        <div className="p-8 max-w-5xl mx-auto">
          <h1 className="text-6xl font-black mb-3">Create Discussion</h1>

          <p className="text-slate-400 mb-10">
            Start a new conversation with the community.
          </p>

          <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8">
            <div className="space-y-6">
              <div>
                <label className="block mb-3 text-lg">Discussion Title</label>

                <input
                  type="text"
                  placeholder="e.g. Complete MERN Roadmap 2026"
                  className="w-full p-4 rounded-2xl bg-slate-800 border border-slate-700 outline-none"
                />
              </div>

              <div>
                <label className="block mb-3 text-lg">Category</label>

                <select className="w-full p-4 rounded-2xl bg-slate-800 border border-slate-700">
                  <option>React</option>
                  <option>Node.js</option>
                  <option>MongoDB</option>
                  <option>JavaScript</option>
                  <option>Career</option>
                </select>
              </div>

              <div>
                <label className="block mb-3 text-lg">Description</label>

                <textarea
                  rows="8"
                  placeholder="Describe your discussion..."
                  className="w-full p-4 rounded-2xl bg-slate-800 border border-slate-700 outline-none"
                />
              </div>

              <div className="grid md:grid-cols-3 gap-4">
                <div className="bg-slate-800 p-5 rounded-2xl">
                  👥 Expected Reach
                  <h3 className="text-3xl font-bold mt-2">12K+</h3>
                </div>

                <div className="bg-slate-800 p-5 rounded-2xl">
                  💬 Avg Replies
                  <h3 className="text-3xl font-bold mt-2">320</h3>
                </div>

                <div className="bg-slate-800 p-5 rounded-2xl">
                  🔥 Trending Score
                  <h3 className="text-3xl font-bold mt-2">94%</h3>
                </div>
              </div>

              <button className="w-full bg-cyan-500 hover:bg-cyan-600 transition-all py-4 rounded-2xl text-xl font-bold">
                Publish Discussion
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default CreateDiscussion;
