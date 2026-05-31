import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function Profile() {
  return (
    <div className="flex min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-cyan-950 text-white">
      <Sidebar />

      <div className="flex-1">
        <Navbar />

        <div className="p-8">
          <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8">
            <div className="flex flex-col lg:flex-row gap-8 items-center">
              <div className="w-40 h-40 rounded-full bg-gradient-to-r from-cyan-400 to-blue-500 flex items-center justify-center text-6xl font-black">
                R
              </div>

              <div className="flex-1">
                <h1 className="text-6xl font-black">Rohan</h1>

                <p className="text-slate-400 text-xl mt-3">
                  Full Stack Developer • MERN Stack Enthusiast
                </p>

                <div className="flex gap-4 mt-6 flex-wrap">
                  <span className="px-4 py-2 rounded-full bg-cyan-500/20">
                    React
                  </span>

                  <span className="px-4 py-2 rounded-full bg-blue-500/20">
                    Node.js
                  </span>

                  <span className="px-4 py-2 rounded-full bg-purple-500/20">
                    MongoDB
                  </span>

                  <span className="px-4 py-2 rounded-full bg-green-500/20">
                    Socket.IO
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* Stats */}
          <div className="grid md:grid-cols-4 gap-6 mt-8">
            {[
              ["Discussions", "142"],
              ["Comments", "621"],
              ["Reputation", "9,820"],
              ["Followers", "1,240"],
            ].map((item) => (
              <div
                key={item[0]}
                className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8"
              >
                <p className="text-slate-400">{item[0]}</p>
                <h2 className="text-5xl font-black mt-3">{item[1]}</h2>
              </div>
            ))}
          </div>

          <div className="grid xl:grid-cols-3 gap-8 mt-8">
            {/* Achievements */}
            <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8">
              <h2 className="text-3xl font-bold mb-6">Achievements</h2>

              <div className="space-y-4">
                <div className="bg-slate-800/50 p-4 rounded-2xl">
                  🏆 Top Contributor
                </div>

                <div className="bg-slate-800/50 p-4 rounded-2xl">
                  ⭐ 500+ Helpful Answers
                </div>

                <div className="bg-slate-800/50 p-4 rounded-2xl">
                  🚀 Community Builder
                </div>

                <div className="bg-slate-800/50 p-4 rounded-2xl">
                  💬 1000+ Messages Sent
                </div>
              </div>
            </div>

            {/* Activity */}
            <div className="xl:col-span-2 bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8">
              <h2 className="text-3xl font-bold mb-6">Recent Activity</h2>

              <div className="space-y-4">
                <div className="bg-slate-800/50 p-5 rounded-2xl">
                  Created discussion:
                  <span className="text-cyan-400 ml-2">
                    Complete MERN Roadmap 2026
                  </span>
                </div>

                <div className="bg-slate-800/50 p-5 rounded-2xl">
                  Replied to React Interview Thread
                </div>

                <div className="bg-slate-800/50 p-5 rounded-2xl">
                  Received 120 new upvotes
                </div>

                <div className="bg-slate-800/50 p-5 rounded-2xl">
                  Earned Top Contributor Badge
                </div>

                <div className="bg-slate-800/50 p-5 rounded-2xl">
                  Joined Node.js Community Group
                </div>
              </div>
            </div>
          </div>

          {/* Portfolio Section */}
          <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8 mt-8">
            <h2 className="text-3xl font-bold mb-6">Community Impact</h2>

            <div className="grid md:grid-cols-3 gap-6">
              <div className="bg-slate-800/50 p-6 rounded-2xl">
                <h3 className="text-xl font-bold">Total Views</h3>
                <p className="text-5xl font-black mt-3">128K</p>
              </div>

              <div className="bg-slate-800/50 p-6 rounded-2xl">
                <h3 className="text-xl font-bold">Engagement Rate</h3>
                <p className="text-5xl font-black mt-3">87%</p>
              </div>

              <div className="bg-slate-800/50 p-6 rounded-2xl">
                <h3 className="text-xl font-bold">Community Rank</h3>
                <p className="text-5xl font-black mt-3">#12</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Profile;
