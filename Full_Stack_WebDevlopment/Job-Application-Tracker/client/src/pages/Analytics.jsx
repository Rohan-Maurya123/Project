import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  AreaChart,
  Area,
  PieChart,
  Pie,
  Cell,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
} from "recharts";
import {
  TrendingUp,
  Target,
  Calendar,
  CheckCircle2,
  XCircle,
  Award,
  Clock,
} from "lucide-react";

// Sample data for analytics
const monthlyData = [
  { month: "Aug", applied: 8, interviews: 3, offers: 1 },
  { month: "Sep", applied: 12, interviews: 5, offers: 1 },
  { month: "Oct", applied: 15, interviews: 6, offers: 2 },
  { month: "Nov", applied: 10, interviews: 4, offers: 1 },
  { month: "Dec", applied: 18, interviews: 7, offers: 2 },
  { month: "Jan", applied: 22, interviews: 9, offers: 3 },
];

const statusDistribution = [
  { name: "Applied", value: 45, color: "#8b5cf6" },
  { name: "Interview", value: 18, color: "#3b82f6" },
  { name: "Offer", value: 7, color: "#10b981" },
  { name: "Rejected", value: 15, color: "#ef4444" },
];

const applicationSource = [
  { name: "LinkedIn", value: 30, color: "#0077b5" },
  { name: "Referral", value: 20, color: "#10b981" },
  { name: "Company Website", value: 15, color: "#f59e0b" },
  { name: "Indeed", value: 12, color: "#2563eb" },
  { name: "Other", value: 8, color: "#6b7280" },
];

const radarData = [
  { subject: "Resume", A: 85, fullMark: 100 },
  { subject: "Cover Letter", A: 70, fullMark: 100 },
  { subject: "Interview", A: 80, fullMark: 100 },
  { subject: "Technical", A: 90, fullMark: 100 },
  { subject: "Networking", A: 65, fullMark: 100 },
];

const stats = [
  {
    title: "Success Rate",
    value: "12.7%",
    change: "+3.2%",
    icon: TrendingUp,
    color: "text-green-400",
    bg: "bg-green-500/20",
    description: "Offer to application ratio"
  },
  {
    title: "Interview Rate",
    value: "28.6%",
    change: "+5.1%",
    icon: Target,
    color: "text-blue-400",
    bg: "bg-blue-500/20",
    description: "Interview to application ratio"
  },
  {
    title: "Avg. Response Time",
    value: "5.2 days",
    change: "-1.3 days",
    icon: Clock,
    color: "text-purple-400",
    bg: "bg-purple-500/20",
    description: "Time to first response"
  },
  {
    title: "Active Applications",
    value: "18",
    change: "+4",
    icon: Calendar,
    color: "text-pink-400",
    bg: "bg-pink-500/20",
    description: "Currently in process"
  },
];

export default function Analytics() {
  const totalApplications = statusDistribution.reduce((sum, item) => sum + item.value, 0);

  return (
    <div className="space-y-6">
      {/* HEADER */}
      <div>
        <h1 className="text-3xl font-bold">📈 Analytics</h1>
        <p className="text-gray-400 mt-1">Insights into your job search performance</p>
      </div>

      {/* STATS */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        {stats.map((stat, i) => (
          <div key={i} className="p-6 rounded-2xl bg-white/5 border border-white/10">
            <div className="flex items-center justify-between mb-4">
              <div className={`w-12 h-12 rounded-xl ${stat.bg} flex items-center justify-center ${stat.color}`}>
                <stat.icon size={24} />
              </div>
              <span className={`text-sm font-medium ${stat.color}`}>{stat.change}</span>
            </div>
            <h3 className="text-3xl font-bold mb-1">{stat.value}</h3>
            <p className="text-sm text-gray-300 mb-1">{stat.title}</p>
            <p className="text-xs text-gray-500">{stat.description}</p>
          </div>
        ))}
      </div>

      {/* CHARTS ROW 1 */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* MONTHLY TREND */}
        <div className="lg:col-span-2 p-6 rounded-2xl bg-white/5 border border-white/10">
          <h2 className="text-lg font-semibold mb-6">Application Trend</h2>
          <ResponsiveContainer width="100%" height={300}>
            <AreaChart data={monthlyData}>
              <defs>
                <linearGradient id="colorApplied" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#8b5cf6" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0} />
                </linearGradient>
                <linearGradient id="colorInterview" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#3b82f6" stopOpacity={0} />
                </linearGradient>
              </defs>
              <XAxis dataKey="month" axisLine={false} tickLine={false} tick={{ fill: '#9ca3af', fontSize: 12 }} />
              <YAxis axisLine={false} tickLine={false} tick={{ fill: '#9ca3af', fontSize: 12 }} />
              <Tooltip
                contentStyle={{ background: 'rgba(23, 23, 23, 0.95)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '12px' }}
                itemStyle={{ color: '#fff' }}
              />
              <Area type="monotone" dataKey="applied" stroke="#8b5cf6" strokeWidth={3} fillOpacity={1} fill="url(#colorApplied)" name="Applied" />
              <Area type="monotone" dataKey="interviews" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorInterview)" name="Interviews" />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        {/* STATUS DISTRIBUTION */}
        <div className="p-6 rounded-2xl bg-white/5 border border-white/10">
          <h2 className="text-lg font-semibold mb-6">Status Distribution</h2>
          <div className="flex items-center justify-center">
            <ResponsiveContainer width="100%" height={200}>
              <PieChart>
                <Pie
                  data={statusDistribution}
                  cx="50%"
                  cy="50%"
                  innerRadius={50}
                  outerRadius={70}
                  paddingAngle={5}
                  dataKey="value"
                >
                  {statusDistribution.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{ background: 'rgba(23, 23, 23, 0.95)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '12px' }}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>
          <div className="mt-4 space-y-2">
            {statusDistribution.map((item, i) => (
              <div key={i} className="flex items-center justify-between text-sm">
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 rounded-full" style={{ backgroundColor: item.color }} />
                  <span className="text-gray-300">{item.name}</span>
                </div>
                <span className="font-medium">{item.value} <span className="text-gray-500 text-xs">({Math.round((item.value / totalApplications) * 100)}%)</span></span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* CHARTS ROW 2 */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* APPLICATION SOURCE */}
        <div className="p-6 rounded-2xl bg-white/5 border border-white/10">
          <h2 className="text-lg font-semibold mb-6">Application Sources</h2>
          <ResponsiveContainer width="100%" height={280}>
            <BarChart data={applicationSource} layout="vertical">
              <XAxis type="number" axisLine={false} tickLine={false} tick={{ fill: '#9ca3af', fontSize: 12 }} />
              <YAxis dataKey="name" type="category" axisLine={false} tickLine={false} tick={{ fill: '#9ca3af', fontSize: 12 }} width={120} />
              <Tooltip
                contentStyle={{ background: 'rgba(23, 23, 23, 0.95)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '12px' }}
              />
              <Bar dataKey="value" radius={[0, 8, 8, 0]}>
                {applicationSource.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>

        {/* SKILLS RADAR */}
        <div className="p-6 rounded-2xl bg-white/5 border border-white/10">
          <h2 className="text-lg font-semibold mb-6">Performance Radar</h2>
          <ResponsiveContainer width="100%" height={280}>
            <RadarChart data={radarData}>
              <PolarGrid stroke="rgba(255,255,255,0.1)" />
              <PolarAngleAxis dataKey="subject" tick={{ fill: '#9ca3af', fontSize: 12 }} />
              <PolarRadiusAxis angle={90} domain={[0, 100]} tick={false} axisLine={false} />
              <Radar name="Performance" dataKey="A" stroke="#8b5cf6" fill="#8b5cf6" fillOpacity={0.4} />
              <Tooltip
                contentStyle={{ background: 'rgba(23, 23, 23, 0.95)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '12px' }}
              />
            </RadarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* KEY INSIGHTS */}
      <div className="p-6 rounded-2xl bg-gradient-to-r from-purple-500/10 to-blue-500/10 border border-purple-500/20">
        <div className="flex items-center gap-2 mb-4">
          <Award className="text-yellow-400" size={20} />
          <h2 className="text-lg font-semibold">Key Insights</h2>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="flex gap-3">
            <CheckCircle2 className="text-green-400 mt-1 flex-shrink-0" size={18} />
            <div>
              <p className="font-medium">Strong performance in technical interviews</p>
              <p className="text-sm text-gray-400">Your technical skills are a standout - 90% rating!</p>
            </div>
          </div>
          <div className="flex gap-3">
            <TrendingUp className="text-blue-400 mt-1 flex-shrink-0" size={18} />
            <div>
              <p className="font-medium">Applications trending upward</p>
              <p className="text-sm text-gray-400">22 applications in January - your highest month yet!</p>
            </div>
          </div>
          <div className="flex gap-3">
            <Target className="text-purple-400 mt-1 flex-shrink-0" size={18} />
            <div>
              <p className="font-medium">Referrals work best for you</p>
              <p className="text-sm text-gray-400">35% interview rate from referrals - prioritize this channel!</p>
            </div>
          </div>
          <div className="flex gap-3">
            <XCircle className="text-orange-400 mt-1 flex-shrink-0" size={18} />
            <div>
              <p className="font-medium">Networking needs improvement</p>
              <p className="text-sm text-gray-400">Focus on building professional connections</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
