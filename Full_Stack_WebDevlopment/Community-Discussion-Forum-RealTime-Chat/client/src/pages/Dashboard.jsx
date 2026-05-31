import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import NotificationPanel from "../components/NotificationPanel";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
} from "recharts";

const growthData = [
  { month: "Jan", users: 1200 },
  { month: "Feb", users: 1800 },
  { month: "Mar", users: 2400 },
  { month: "Apr", users: 3500 },
  { month: "May", users: 4700 },
  { month: "Jun", users: 6200 },
  { month: "Jul", users: 8100 },
  { month: "Aug", users: 9800 },
];

const engagementData = [
  { name: "Posts", value: 4200 },
  { name: "Comments", value: 8600 },
  { name: "Chats", value: 12400 },
  { name: "Likes", value: 19200 },
];

const trendingTopics = [
  {
    title: "Complete MERN Roadmap 2026",
    replies: 421,
    views: "12.4K",
  },
  {
    title: "React Interview Experience",
    replies: 318,
    views: "9.8K",
  },
  {
    title: "Node.js System Design",
    replies: 267,
    views: "7.3K",
  },
  {
    title: "MongoDB Optimization Guide",
    replies: 189,
    views: "5.1K",
  },
];

const onlineMembers = [
  "Aman",
  "Priya",
  "Rahul",
  "Sneha",
  "Ankit",
  "Vikas",
  "Riya",
  "Kunal",
];

const activities = [
  "🔥 MERN Roadmap discussion reached 500 replies",
  "🚀 25 new members joined today",
  "⭐ React Interview thread trending",
  "💬 1,240 chat messages sent today",
  "🏆 Community crossed 10,000 members",
];

const stats = [
  {
    title: "Total Members",
    value: "12,847",
    change: "+18.2%",
  },
  {
    title: "Discussions",
    value: "3,421",
    change: "+12.8%",
  },
  {
    title: "Comments",
    value: "18,955",
    change: "+24.5%",
  },
  {
    title: "Messages",
    value: "92,410",
    change: "+31.6%",
  },
];

function Dashboard() {
  return (
    <div className="flex min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-cyan-950 text-white">
      <Sidebar />

      <div className="flex-1">
        <Navbar />

        <div className="p-8 space-y-8">
          {/* Header */}
          <div>
            <h1 className="text-6xl font-black mb-3">Community Dashboard</h1>

            <p className="text-slate-400 text-lg">
              Monitor discussions, engagement, members and real-time activity.
            </p>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
            {stats.map((item) => (
              <div
                key={item.title}
                className="
                bg-white/5
                backdrop-blur-xl
                border border-white/10
                rounded-3xl
                p-8
                hover:scale-105
                transition-all
                duration-300
                shadow-2xl
              "
              >
                <p className="text-slate-400 text-lg">{item.title}</p>

                <h2 className="text-5xl font-black mt-4">{item.value}</h2>

                <p className="text-green-400 mt-4">{item.change} this month</p>
              </div>
            ))}
          </div>

          <div className="xl:col-span-2">{/* Community Growth Chart */}</div>

          <div>
            <NotificationPanel />
          </div>

          {/* Charts */}
          <div className="grid xl:grid-cols-2 gap-8">
            <div
              className="
              bg-white/5
              backdrop-blur-xl
              border border-white/10
              rounded-3xl
              p-8
            "
            >
              <h2 className="text-3xl font-bold mb-6">Community Growth</h2>

              <ResponsiveContainer width="100%" height={350}>
                <AreaChart data={growthData}>
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Area
                    type="monotone"
                    dataKey="users"
                    stroke="#22d3ee"
                    fill="#0891b2"
                  />
                </AreaChart>
              </ResponsiveContainer>
            </div>

            <div
              className="
              bg-white/5
              backdrop-blur-xl
              border border-white/10
              rounded-3xl
              p-8
            "
            >
              <h2 className="text-3xl font-bold mb-6">Engagement Metrics</h2>

              <ResponsiveContainer width="100%" height={350}>
                <BarChart data={engagementData}>
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="value" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Bottom Grid */}
          <div className="grid xl:grid-cols-3 gap-8">
            {/* Trending */}
            <div
              className="
              bg-white/5
              backdrop-blur-xl
              border border-white/10
              rounded-3xl
              p-8
            "
            >
              <h2 className="text-3xl font-bold mb-6">Trending Discussions</h2>

              <div className="space-y-4">
                {trendingTopics.map((topic) => (
                  <div
                    key={topic.title}
                    className="
                    bg-slate-800/50
                    rounded-2xl
                    p-4
                  "
                  >
                    <h3 className="font-bold text-lg">{topic.title}</h3>

                    <div className="flex justify-between mt-3 text-sm text-slate-400">
                      <span>{topic.replies} Replies</span>

                      <span>{topic.views} Views</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Activity */}
            <div
              className="
              bg-white/5
              backdrop-blur-xl
              border border-white/10
              rounded-3xl
              p-8
            "
            >
              <h2 className="text-3xl font-bold mb-6">Recent Activity</h2>

              <div className="space-y-4">
                {activities.map((item, index) => (
                  <div
                    key={index}
                    className="
                    bg-slate-800/50
                    rounded-2xl
                    p-4
                  "
                  >
                    {item}
                  </div>
                ))}
              </div>
            </div>

            {/* Online Users */}
            <div
              className="
              bg-white/5
              backdrop-blur-xl
              border border-white/10
              rounded-3xl
              p-8
            "
            >
              <h2 className="text-3xl font-bold mb-6">Online Members</h2>

              <div className="space-y-4">
                {onlineMembers.map((user) => (
                  <div key={user} className="flex items-center gap-4">
                    <div
                      className="
                      w-12
                      h-12
                      rounded-full
                      bg-gradient-to-r
                      from-cyan-400
                      to-blue-500
                      flex
                      items-center
                      justify-center
                      font-bold
                    "
                    >
                      {user[0]}
                    </div>

                    <div>
                      <h3>{user}</h3>
                      <p className="text-green-400 text-sm">Online</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Community Table */}
          <div
            className="
            bg-white/5
            backdrop-blur-xl
            border border-white/10
            rounded-3xl
            p-8
          "
          >
            <h2 className="text-3xl font-bold mb-6">Top Contributors</h2>

            <table className="w-full">
              <thead>
                <tr className="border-b border-slate-700">
                  <th className="text-left p-4">Member</th>
                  <th className="text-left p-4">Posts</th>
                  <th className="text-left p-4">Comments</th>
                  <th className="text-left p-4">Reputation</th>
                </tr>
              </thead>

              <tbody>
                <tr>
                  <td className="p-4">Aman Sharma</td>
                  <td className="p-4">142</td>
                  <td className="p-4">621</td>
                  <td className="p-4">⭐ 9,820</td>
                </tr>

                <tr>
                  <td className="p-4">Priya Singh</td>
                  <td className="p-4">121</td>
                  <td className="p-4">542</td>
                  <td className="p-4">⭐ 8,940</td>
                </tr>

                <tr>
                  <td className="p-4">Rahul Verma</td>
                  <td className="p-4">98</td>
                  <td className="p-4">470</td>
                  <td className="p-4">⭐ 7,880</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
