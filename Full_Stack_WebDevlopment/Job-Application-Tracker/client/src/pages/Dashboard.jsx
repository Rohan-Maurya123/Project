import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  LineChart,
  Line,
  AreaChart,
  Area,
  Cell,
  PieChart,
  Pie,
} from "recharts";
import { motion } from "framer-motion";
import {
  TrendingUp,
  TrendingDown,
  Calendar,
  Clock,
  ArrowRight,
  Plus,
  Filter,
  MoreVertical,
  CheckCircle2,
  XCircle,
  MessageSquare,
  Star,
} from "lucide-react";

const weeklyData = [
  { name: "Mon", applied: 5, interviews: 2, offers: 0 },
  { name: "Tue", applied: 8, interviews: 3, offers: 1 },
  { name: "Wed", applied: 3, interviews: 1, offers: 0 },
  { name: "Thu", applied: 10, interviews: 4, offers: 2 },
  { name: "Fri", applied: 6, interviews: 2, offers: 0 },
  { name: "Sat", applied: 2, interviews: 0, offers: 0 },
  { name: "Sun", applied: 4, interviews: 1, offers: 0 },
];

const statusData = [
  { name: "Applied", value: 42, color: "#8b5cf6" },
  { name: "Interview", value: 18, color: "#3b82f6" },
  { name: "Offer", value: 6, color: "#10b981" },
  { name: "Rejected", value: 12, color: "#ef4444" },
];

const jobs = [
  { id: 1, company: "Google", role: "Senior Frontend Dev", status: "Interview", date: "2 days ago", salary: "$150k-$180k", logo: "G" },
  { id: 2, company: "Amazon", role: "Backend Engineer", status: "Offer", date: "1 week ago", salary: "$140k-$170k", logo: "A" },
  { id: 3, company: "Microsoft", role: "Full Stack Developer", status: "Applied", date: "3 days ago", salary: "$130k-$160k", logo: "M" },
  { id: 4, company: "Meta", role: "React Developer", status: "Rejected", date: "2 weeks ago", salary: "$160k-$200k", logo: "Me" },
  { id: 5, company: "Stripe", role: "Software Engineer", status: "Interview", date: "Yesterday", salary: "$170k-$210k", logo: "S" },
];

const activities = [
  { id: 1, type: "interview", title: "Interview scheduled with Google", time: "Today at 2:00 PM", icon: Calendar, color: "blue" },
  { id: 2, type: "offer", title: "Offer received from Amazon", time: "Yesterday", icon: CheckCircle2, color: "green" },
  { id: 3, type: "reject", title: "Application rejected by Meta", time: "2 days ago", icon: XCircle, color: "red" },
  { id: 4, type: "apply", title: "Applied to Stripe", time: "3 days ago", icon: Plus, color: "purple" },
];

export default function Dashboard() {
  return (
    <div className="space-y-8">
      {/* HEADER */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-4xl font-bold">Welcome back, Rohan! 👋</h1>
          <p className="text-gray-400 mt-1">Your job search is looking strong today. Keep it up!</p>
        </div>
        <div className="flex items-center gap-3">
          <button className="flex items-center gap-2 px-4 py-2.5 bg-white/5 border border-white/10 rounded-xl hover:bg-white/10 transition">
            <Filter size={18} />
            <span>Filter</span>
          </button>
          <button className="flex items-center gap-2 px-4 py-2.5 bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl hover:opacity-90 transition font-medium shadow-lg shadow-purple-500/25">
            <Plus size={18} />
            <span>Add Application</span>
          </button>
        </div>
      </div>

      {/* STATS GRID */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <StatCard label="Total Applied" value="78" change="+12%" trend="up" color="purple" icon={Plus} />
        <StatCard label="Interviews" value="24" change="+5%" trend="up" color="blue" icon={MessageSquare} />
        <StatCard label="Offers" value="7" change="+2" trend="up" color="green" icon={Star} />
        <StatCard label="Rejected" value="15" change="-3%" trend="down" color="red" icon={XCircle} />
      </div>

      {/* CHARTS ROW */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* MAIN CHART */}
        <div className="lg:col-span-2 p-6 rounded-2xl bg-white/5 border border-white/10">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-lg font-semibold">Application Activity</h2>
              <p className="text-sm text-gray-400">Last 7 days</p>
            </div>
            <div className="flex gap-2">
              <button className="px-3 py-1 text-sm bg-purple-500/20 text-purple-300 rounded-lg">Week</button>
              <button className="px-3 py-1 text-sm text-gray-400 hover:bg-white/10 rounded-lg">Month</button>
              <button className="px-3 py-1 text-sm text-gray-400 hover:bg-white/10 rounded-lg">Year</button>
            </div>
          </div>
          <ResponsiveContainer width="100%" height={300}>
            <AreaChart data={weeklyData}>
              <defs>
                <linearGradient id="colorApplied" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#8b5cf6" stopOpacity={0.3}/>
                  <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0}/>
                </linearGradient>
                <linearGradient id="colorInterviews" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                  <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                </linearGradient>
              </defs>
              <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#9ca3af', fontSize: 12}} />
              <YAxis axisLine={false} tickLine={false} tick={{fill: '#9ca3af', fontSize: 12}} />
              <Tooltip 
                contentStyle={{background: 'rgba(23, 23, 23, 0.95)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '12px'}}
                itemStyle={{color: '#fff'}}
              />
              <Area type="monotone" dataKey="applied" stroke="#8b5cf6" strokeWidth={3} fillOpacity={1} fill="url(#colorApplied)" />
              <Area type="monotone" dataKey="interviews" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorInterviews)" />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        {/* PIE CHART */}
        <div className="p-6 rounded-2xl bg-white/5 border border-white/10">
          <h2 className="text-lg font-semibold mb-6">Status Breakdown</h2>
          <div className="flex items-center justify-center">
            <ResponsiveContainer width="100%" height={200}>
              <PieChart>
                <Pie
                  data={statusData}
                  cx="50%"
                  cy="50%"
                  innerRadius={50}
                  outerRadius={70}
                  paddingAngle={5}
                  dataKey="value"
                >
                  {statusData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip 
                  contentStyle={{background: 'rgba(23, 23, 23, 0.95)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '12px'}}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>
          <div className="grid grid-cols-2 gap-3 mt-4">
            {statusData.map((item, i) => (
              <div key={i} className="flex items-center gap-2">
                <div className="w-3 h-3 rounded-full" style={{backgroundColor: item.color}} />
                <span className="text-sm text-gray-300">{item.name}</span>
                <span className="ml-auto text-sm font-semibold">{item.value}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* BOTTOM SECTION */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* RECENT APPLICATIONS */}
        <div className="lg:col-span-2 p-6 rounded-2xl bg-white/5 border border-white/10">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-lg font-semibold">Recent Applications</h2>
              <p className="text-sm text-gray-400">Your latest job applications</p>
            </div>
            <button className="text-purple-400 hover:text-purple-300 text-sm font-medium flex items-center gap-1">
              View all <ArrowRight size={16} />
            </button>
          </div>
          <div className="space-y-3">
            {jobs.map((job, i) => (
              <motion.div
                key={job.id}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.05 }}
                className="flex items-center gap-4 p-4 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 hover:border-white/20 transition"
              >
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center font-bold text-lg">
                  {job.logo}
                </div>
                <div className="flex-1">
                  <div className="flex items-center gap-2">
                    <h3 className="font-semibold">{job.company}</h3>
                    <StatusBadge status={job.status} />
                  </div>
                  <p className="text-sm text-gray-400">{job.role}</p>
                  <p className="text-xs text-gray-500">{job.salary}</p>
                </div>
                <div className="text-right">
                  <p className="text-sm text-gray-400 flex items-center gap-1 justify-end">
                    <Clock size={14} /> {job.date}
                  </p>
                  <button className="mt-2 p-2 hover:bg-white/10 rounded-lg">
                    <MoreVertical size={16} className="text-gray-400" />
                  </button>
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        {/* ACTIVITY FEED */}
        <div className="p-6 rounded-2xl bg-white/5 border border-white/10">
          <h2 className="text-lg font-semibold mb-6">Recent Activity</h2>
          <div className="space-y-4">
            {activities.map((activity, i) => (
              <div key={activity.id} className="flex gap-3">
                <div className={`w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 ${
                  activity.color === 'blue' ? 'bg-blue-500/20 text-blue-400' :
                  activity.color === 'green' ? 'bg-green-500/20 text-green-400' :
                  activity.color === 'red' ? 'bg-red-500/20 text-red-400' :
                  'bg-purple-500/20 text-purple-400'
                }`}>
                  <activity.icon size={18} />
                </div>
                <div className="flex-1">
                  <p className="text-sm font-medium">{activity.title}</p>
                  <p className="text-xs text-gray-400">{activity.time}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function StatCard({ label, value, change, trend, color, icon: Icon }) {
  const colors = {
    purple: "from-purple-500/20 to-purple-600/10 border-purple-500/30",
    blue: "from-blue-500/20 to-blue-600/10 border-blue-500/30",
    green: "from-green-500/20 to-green-600/10 border-green-500/30",
    red: "from-red-500/20 to-red-600/10 border-red-500/30",
  };

  const iconColors = {
    purple: "text-purple-400",
    blue: "text-blue-400",
    green: "text-green-400",
    red: "text-red-400",
  };

  return (
    <motion.div
      whileHover={{ y: -4 }}
      className={`p-6 rounded-2xl bg-gradient-to-br ${colors[color]} border ${colors[color].split(' ')[2]}`}
    >
      <div className="flex items-center justify-between mb-4">
        <div className={`w-11 h-11 rounded-xl bg-white/10 flex items-center justify-center ${iconColors[color]}`}>
          <Icon size={22} />
        </div>
        <div className={`flex items-center gap-1 text-sm font-medium ${
          trend === 'up' ? 'text-green-400' : 'text-red-400'
        }`}>
          {trend === 'up' ? <TrendingUp size={16} /> : <TrendingDown size={16} />}
          {change}
        </div>
      </div>
      <h3 className="text-3xl font-bold mb-1">{value}</h3>
      <p className="text-sm text-gray-400">{label}</p>
    </motion.div>
  );
}

function StatusBadge({ status }) {
  const badges = {
    Applied: "bg-purple-500/20 text-purple-300 border-purple-500/30",
    Interview: "bg-blue-500/20 text-blue-300 border-blue-500/30",
    Offer: "bg-green-500/20 text-green-300 border-green-500/30",
    Rejected: "bg-red-500/20 text-red-300 border-red-500/30",
  };

  return (
    <span className={`px-2.5 py-0.5 rounded-full text-xs font-medium border ${badges[status]}`}>
      {status}
    </span>
  );
}
