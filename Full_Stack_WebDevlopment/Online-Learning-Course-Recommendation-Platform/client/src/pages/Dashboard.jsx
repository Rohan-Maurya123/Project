import React from "react";
import { motion } from "framer-motion";
import {
  TrendingUp,
  TrendingDown,
  ArrowRight,
  Plus,
  Filter,
  MoreVertical,
  CheckCircle2,
  XCircle,
  MessageSquare,
  Star,
  BookOpen,
  Award,
  Clock,
  Calendar
} from "lucide-react";
import {
  AreaChart,
  Area,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";
import CourseCard from "../components/CourseCard";

const weeklyData = [
  { name: "Mon", courses: 3, hours: 4.5 },
  { name: "Tue", courses: 5, hours: 7.2 },
  { name: "Wed", courses: 2, hours: 3.1 },
  { name: "Thu", courses: 6, hours: 8.4 },
  { name: "Fri", courses: 4, hours: 5.3 },
  { name: "Sat", courses: 7, hours: 9.8 },
  { name: "Sun", courses: 3, hours: 4.0 },
];

const statusData = [
  { name: "In Progress", value: 42, color: "#8b5cf6" },
  { name: "Completed", value: 18, color: "#10b981" },
  { name: "Enrolled", value: 26, color: "#3b82f6" },
];

const mockCourses = [
  { _id: 1, title: "Complete Web Development Bootcamp", category: "Programming", level: "Beginner", tags: ["JavaScript", "React", "Node"] },
  { _id: 2, title: "Advanced React Patterns", category: "Programming", level: "Advanced", tags: ["React", "TypeScript"] },
  { _id: 3, title: "Data Science Fundamentals", category: "Data Science", level: "Intermediate", tags: ["Python", "Pandas", "ML"] },
  { _id: 4, title: "UI/UX Design Masterclass", category: "Design", level: "Beginner", tags: ["Figma", "Design"] },
];

const courses = [
  { id: 1, title: "Full Stack Web Development", category: "Programming", progress: 75, duration: "12h 30m", level: "Beginner", rating: 4.8, students: "15.2k" },
  { id: 2, title: "React Masterclass", category: "Programming", progress: 45, duration: "18h 45m", level: "Intermediate", rating: 4.9, students: "8.5k" },
  { id: 3, title: "Data Science 101", category: "Data Science", progress: 90, duration: "24h 15m", level: "Beginner", rating: 4.7, students: "12.8k" },
  { id: 4, title: "UI/UX Design Complete", category: "Design", progress: 20, duration: "16h 00m", level: "Beginner", rating: 4.6, students: "9.2k" },
  { id: 5, title: "AWS Cloud Practitioner", category: "Cloud", progress: 60, duration: "14h 30m", level: "Beginner", rating: 4.5, students: "7.8k" },
];

const activities = [
  { id: 1, type: "completed", title: "Completed 'JavaScript Basics'", time: "Today at 2:30 PM", icon: CheckCircle2, color: "green" },
  { id: 2, type: "started", title: "Started 'React Masterclass'", time: "Yesterday", icon: Plus, color: "purple" },
  { id: 3, type: "enrolled", title: "Enrolled in 'AWS Cloud Practitioner'", time: "2 days ago", icon: BookOpen, color: "blue" },
  { id: 4, type: "certified", title: "Earned 'Full Stack' certificate!", time: "1 week ago", icon: Award, color: "yellow" },
];

function StatCard({ label, value, change, trend, color, icon: Icon }) {
  const colors = {
    purple: "from-purple-500/20 to-purple-600/10 border-purple-500/30",
    blue: "from-blue-500/20 to-blue-600/10 border-blue-500/30",
    green: "from-green-500/20 to-green-600/10 border-green-500/30",
    yellow: "from-amber-500/20 to-amber-600/10 border-amber-500/30",
  };

  const iconColors = {
    purple: "text-purple-400",
    blue: "text-blue-400",
    green: "text-green-400",
    yellow: "text-amber-400",
  };

  return (
    <motion.div
      whileHover={{ y: -4 }}
      className={`p-6 rounded-2xl bg-gradient-to-br ${colors[color]} border border-white/10`}
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
      <p className="text-sm text-slate-400">{label}</p>
    </motion.div>
  );
}

export default function Dashboard() {
  return (
    <div className="max-w-7xl mx-auto px-6 space-y-8">
      {/* HEADER */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-4xl font-bold text-gradient">Welcome back, Rohan! 👋</h1>
          <p className="text-slate-400 mt-1">Your learning journey is looking strong today. Keep it up!</p>
        </div>
        <div className="flex items-center gap-3">
          <button className="flex items-center gap-2 px-4 py-2.5 glass-card hover:bg-white/10 transition border border-white/10 rounded-xl">
            <Filter size={18} />
            <span>Filter</span>
          </button>
          <button className="flex items-center gap-2 px-4 py-2.5 bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl hover:opacity-90 transition font-medium shadow-lg shadow-purple-500/25">
            <Plus size={18} />
            <span>Enroll New</span>
          </button>
        </div>
      </div>

      {/* STATS GRID */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <StatCard label="Courses Enrolled" value="42" change="+12%" trend="up" color="purple" icon={BookOpen} />
        <StatCard label="In Progress" value="15" change="+3%" trend="up" color="blue" icon={Clock} />
        <StatCard label="Completed" value="18" change="+5" trend="up" color="green" icon={Award} />
        <StatCard label="Certificates" value="6" change="+1" trend="up" color="yellow" icon={Star} />
      </div>

      {/* CHARTS ROW */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* MAIN CHART */}
        <div className="lg:col-span-2 glass-card">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-lg font-semibold text-white">Learning Activity</h2>
              <p className="text-sm text-slate-400">Last 7 days</p>
            </div>
            <div className="flex gap-2">
              <button className="px-3 py-1 text-sm bg-purple-500/20 text-purple-300 rounded-lg">Week</button>
              <button className="px-3 py-1 text-sm text-slate-400 hover:bg-white/10 rounded-lg">Month</button>
              <button className="px-3 py-1 text-sm text-slate-400 hover:bg-white/10 rounded-lg">Year</button>
            </div>
          </div>
          <ResponsiveContainer width="100%" height={300}>
            <AreaChart data={weeklyData}>
              <defs>
                <linearGradient id="colorCourses" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#8b5cf6" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0} />
                </linearGradient>
                <linearGradient id="colorHours" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#3b82f6" stopOpacity={0} />
                </linearGradient>
              </defs>
              <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fill: "#9ca3af", fontSize: 12 }} />
              <YAxis axisLine={false} tickLine={false} tick={{ fill: "#9ca3af", fontSize: 12 }} />
              <Tooltip
                contentStyle={{ background: "rgba(23, 23, 23, 0.95)", border: "1px solid rgba(255,255,255,0.1)", borderRadius: "12px" }}
                itemStyle={{ color: "#fff" }}
              />
              <Area type="monotone" dataKey="courses" stroke="#8b5cf6" strokeWidth={3} fillOpacity={1} fill="url(#colorCourses)" />
              <Area type="monotone" dataKey="hours" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorHours)" />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        {/* PIE CHART */}
        <div className="glass-card">
          <h2 className="text-lg font-semibold text-white mb-6">Status Breakdown</h2>
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
                  contentStyle={{ background: "rgba(23, 23, 23, 0.95)", border: "1px solid rgba(255,255,255,0.1)", borderRadius: "12px" }}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>
          <div className="grid grid-cols-2 gap-3 mt-4">
            {statusData.map((item, i) => (
              <div key={i} className="flex items-center gap-2">
                <div className="w-3 h-3 rounded-full" style={{ backgroundColor: item.color }} />
                <span className="text-sm text-slate-300">{item.name}</span>
                <span className="ml-auto text-sm font-semibold text-white">{item.value}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* BOTTOM SECTION */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* RECENT COURSES */}
        <div className="lg:col-span-2 glass-card">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-lg font-semibold text-white">Recent Courses</h2>
              <p className="text-sm text-slate-400">Your active courses</p>
            </div>
            <button className="text-purple-400 hover:text-purple-300 text-sm font-medium flex items-center gap-1">
              View all <ArrowRight size={16} />
            </button>
          </div>
          <div className="space-y-3">
            {courses.map((course, i) => (
              <motion.div
                key={course.id}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.05 }}
                className="flex items-center gap-4 p-4 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 hover:border-white/20 transition"
              >
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center font-bold text-lg">
                  {course.title[0]}
                </div>
                <div className="flex-1">
                  <div className="flex items-center gap-2">
                    <h3 className="font-semibold text-white">{course.title}</h3>
                    <span className="px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-500/20 text-purple-300 border border-purple-500/30">
                      {course.category}
                    </span>
                  </div>
                  <p className="text-sm text-slate-400">{course.level}</p>
                  <div className="flex items-center gap-4 mt-1">
                    <div className="flex items-center gap-1">
                      <Star className="w-4 h-4 fill-yellow-400 text-yellow-400" />
                      <span className="text-xs text-slate-300 font-semibold">{course.rating}</span>
                      <span className="text-xs text-slate-500">({course.students})</span>
                    </div>
                    <span className="text-xs text-slate-400 flex items-center gap-1"><Clock size={12}/> {course.duration}</span>
                  </div>
                  <div className="mt-2 w-1/2">
                    <div className="h-1.5 bg-white/10 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-gradient-to-r from-purple-500 to-blue-500"
                        style={{ width: `${course.progress}%` }}
                      />
                    </div>
                    <span className="text-xs text-slate-400">{course.progress}% complete</span>
                  </div>
                </div>
                <div className="text-right">
                  <button className="mt-2 p-2 hover:bg-white/10 rounded-lg">
                    <MoreVertical size={16} className="text-slate-400" />
                  </button>
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        {/* ACTIVITY FEED */}
        <div className="glass-card">
          <h2 className="text-lg font-semibold text-white mb-6">Recent Activity</h2>
          <div className="space-y-4">
            {activities.map((activity, i) => {
              const IconComponent = activity.icon;
              return (
                <div key={activity.id} className="flex gap-3">
                  <div className={`w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 ${
                    activity.color === 'blue' ? 'bg-blue-500/20 text-blue-400' :
                    activity.color === 'green' ? 'bg-green-500/20 text-green-400' :
                    activity.color === 'yellow' ? 'bg-amber-500/20 text-amber-400' :
                    'bg-purple-500/20 text-purple-400'
                  }`}>
                    <IconComponent size={18} />
                  </div>
                  <div className="flex-1">
                    <p className="text-sm font-medium text-white">{activity.title}</p>
                    <p className="text-xs text-slate-400">{activity.time}</p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* RECOMMENDED COURSES */}
      <div className="mt-8">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-2xl font-bold text-gradient">Recommended for You</h2>
            <p className="text-slate-400">Based on your interests</p>
          </div>
          <button className="text-purple-400 hover:text-purple-300 text-sm font-medium flex items-center gap-1">
            View all <ArrowRight size={16} />
          </button>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {mockCourses.map((course) => (
            <CourseCard key={course._id} course={course} />
          ))}
        </div>
      </div>
    </div>
  );
}
