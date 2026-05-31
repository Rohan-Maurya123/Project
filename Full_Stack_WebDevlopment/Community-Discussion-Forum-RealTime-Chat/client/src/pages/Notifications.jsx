import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

const notifications = [
  {
    title: "Discussion Trending",
    message: "MERN Roadmap 2026 is trending.",
    time: "2 min ago",
    icon: "🔥",
  },
  {
    title: "New Comment",
    message: "Priya Singh replied to your discussion.",
    time: "15 min ago",
    icon: "💬",
  },
  {
    title: "New Like",
    message: "Your discussion received 84 likes.",
    time: "1 hour ago",
    icon: "👍",
  },
  {
    title: "Community Growth",
    message: "42 new members joined today.",
    time: "2 hours ago",
    icon: "🚀",
  },
  {
    title: "Achievement Unlocked",
    message: "Top Contributor Badge earned.",
    time: "Today",
    icon: "🏆",
  },
];

function Notifications() {
  return (
    <div className="flex min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-cyan-950 text-white">
      <Sidebar />

      <div className="flex-1">
        <Navbar />

        <div className="p-8">
          <h1 className="text-6xl font-black mb-3">Notifications</h1>

          <p className="text-slate-400 text-lg mb-8">
            Community updates, mentions and activity.
          </p>

          {/* Stats */}
          <div className="grid md:grid-cols-4 gap-6 mb-8">
            {[
              ["Unread", "18"],
              ["Mentions", "52"],
              ["Comments", "124"],
              ["Alerts", "248"],
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

          <div className="grid xl:grid-cols-3 gap-8">
            {/* Notification Feed */}
            <div className="xl:col-span-2 space-y-6">
              {notifications.map((item, index) => (
                <div
                  key={index}
                  className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-6 hover:scale-[1.01] transition-all"
                >
                  <div className="flex gap-5">
                    <div className="text-4xl">{item.icon}</div>

                    <div>
                      <h2 className="text-2xl font-bold">{item.title}</h2>

                      <p className="text-slate-400 mt-2">{item.message}</p>

                      <p className="text-cyan-400 mt-3 text-sm">{item.time}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Sidebar */}
            <div className="space-y-8">
              <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8">
                <h2 className="text-3xl font-bold mb-6">Activity Summary</h2>

                <div className="space-y-4">
                  <div className="bg-slate-800/50 p-4 rounded-2xl">
                    🔥 18 Unread Notifications
                  </div>

                  <div className="bg-slate-800/50 p-4 rounded-2xl">
                    🚀 324 New Members
                  </div>

                  <div className="bg-slate-800/50 p-4 rounded-2xl">
                    💬 1240 Comments Today
                  </div>

                  <div className="bg-slate-800/50 p-4 rounded-2xl">
                    ⭐ Community Milestone
                  </div>
                </div>
              </div>

              <div className="bg-gradient-to-r from-cyan-500 to-blue-600 rounded-3xl p-8">
                <h2 className="text-3xl font-black">Stay Connected</h2>

                <p className="mt-4">
                  Never miss important community updates and discussions.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Notifications;
