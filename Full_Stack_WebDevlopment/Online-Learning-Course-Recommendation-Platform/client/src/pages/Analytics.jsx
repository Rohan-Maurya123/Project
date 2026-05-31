import React from "react";
import {
  LineChart,
  Line,
  AreaChart,
  Area,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

const Analytics = () => {
  const weeklyProgress = [
    { day: "Mon", hours: 2 },
    { day: "Tue", hours: 3.5 },
    { day: "Wed", hours: 2.8 },
    { day: "Thu", hours: 4.2 },
    { day: "Fri", hours: 3.1 },
    { day: "Sat", hours: 5.4 },
    { day: "Sun", hours: 4.6 },
  ];

  const courseCompletion = [
    { name: "React", completion: 72 },
    { name: "Node", completion: 45 },
    { name: "AI", completion: 88 },
    { name: "DSA", completion: 35 },
    { name: "Cloud", completion: 20 },
  ];

  const skills = [
    { skill: "React", value: 90 },
    { skill: "JavaScript", value: 85 },
    { skill: "Node.js", value: 70 },
    { skill: "System Design", value: 50 },
    { skill: "AI", value: 65 },
  ];

  return (
    <div className="max-w-7xl mx-auto px-6 py-8">
      {/* Header */}
      <div className="mb-10">
        <h1 className="text-5xl font-extrabold bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent mb-3">
          Learning Analytics
        </h1>

        <p className="text-slate-400 text-lg">
          Monitor progress, learning habits, skill growth and course
          performance.
        </p>
      </div>

      {/* KPI Cards */}
      <div className="grid md:grid-cols-4 gap-6 mb-10">
        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">
          <p className="text-slate-400">Courses Enrolled</p>
          <h2 className="text-4xl font-bold text-white mt-2">12</h2>
        </div>

        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">
          <p className="text-slate-400">Courses Completed</p>
          <h2 className="text-4xl font-bold text-green-400 mt-2">5</h2>
        </div>

        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">
          <p className="text-slate-400">Learning Hours</p>
          <h2 className="text-4xl font-bold text-indigo-400 mt-2">148h</h2>
        </div>

        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">
          <p className="text-slate-400">Certificates</p>
          <h2 className="text-4xl font-bold text-yellow-400 mt-2">7</h2>
        </div>
      </div>

      {/* Charts */}
      <div className="grid lg:grid-cols-2 gap-8 mb-10">
        {/* Weekly Learning */}
        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">
          <h2 className="text-xl font-bold text-white mb-6">
            Weekly Learning Activity
          </h2>

          <ResponsiveContainer width="100%" height={300}>
            <AreaChart data={weeklyProgress}>
              <defs>
                <linearGradient id="hoursGradient" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stopColor="#6366f1" stopOpacity={0.8} />
                  <stop offset="100%" stopColor="#6366f1" stopOpacity={0.1} />
                </linearGradient>
              </defs>

              <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
              <XAxis dataKey="day" stroke="#94a3b8" />
              <YAxis stroke="#94a3b8" />
              <Tooltip />

              <Area
                type="monotone"
                dataKey="hours"
                stroke="#6366f1"
                fill="url(#hoursGradient)"
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        {/* Completion */}
        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">
          <h2 className="text-xl font-bold text-white mb-6">
            Course Completion
          </h2>

          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={courseCompletion}>
              <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
              <XAxis dataKey="name" stroke="#94a3b8" />
              <YAxis stroke="#94a3b8" />
              <Tooltip />

              <Bar dataKey="completion" fill="#8b5cf6" radius={[8, 8, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Progress Trend */}
      <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800 mb-10">
        <h2 className="text-xl font-bold text-white mb-6">
          Monthly Progress Trend
        </h2>

        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={weeklyProgress}>
            <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
            <XAxis dataKey="day" stroke="#94a3b8" />
            <YAxis stroke="#94a3b8" />
            <Tooltip />

            <Line
              type="monotone"
              dataKey="hours"
              stroke="#22c55e"
              strokeWidth={4}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* Skills */}
      <div className="grid lg:grid-cols-2 gap-8 mb-10">
        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">
          <h2 className="text-xl font-bold text-white mb-6">
            Skill Proficiency
          </h2>

          {skills.map((item) => (
            <div key={item.skill} className="mb-5">
              <div className="flex justify-between mb-2">
                <span className="text-slate-300">{item.skill}</span>
                <span className="text-indigo-400">{item.value}%</span>
              </div>

              <div className="w-full bg-slate-700 h-3 rounded-full">
                <div
                  className="bg-gradient-to-r from-indigo-500 to-purple-500 h-3 rounded-full"
                  style={{ width: `${item.value}%` }}
                />
              </div>
            </div>
          ))}
        </div>

        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">
          <h2 className="text-xl font-bold text-white mb-6">
            Learning Insights
          </h2>

          <div className="space-y-5">
            <div className="bg-slate-800 rounded-2xl p-5">
              <h3 className="text-white font-semibold">
                🔥 15 Day Learning Streak
              </h3>
              <p className="text-slate-400 mt-2">
                Keep learning daily to maintain momentum.
              </p>
            </div>

            <div className="bg-slate-800 rounded-2xl p-5">
              <h3 className="text-white font-semibold">🚀 Strongest Skill</h3>
              <p className="text-slate-400 mt-2">React Development (90%)</p>
            </div>

            <div className="bg-slate-800 rounded-2xl p-5">
              <h3 className="text-white font-semibold">
                📈 Growth Opportunity
              </h3>
              <p className="text-slate-400 mt-2">
                Improve System Design and Cloud Computing.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Recent Performance Table */}
      <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">
        <h2 className="text-xl font-bold text-white mb-6">
          Recent Course Performance
        </h2>

        <div className="overflow-x-auto">
          <table className="w-full text-left">
            <thead>
              <tr className="border-b border-slate-700">
                <th className="pb-4 text-slate-400">Course</th>
                <th className="pb-4 text-slate-400">Progress</th>
                <th className="pb-4 text-slate-400">Score</th>
                <th className="pb-4 text-slate-400">Status</th>
              </tr>
            </thead>

            <tbody>
              <tr className="border-b border-slate-800">
                <td className="py-4 text-white">React Mastery</td>
                <td className="text-indigo-400">72%</td>
                <td className="text-green-400">89%</td>
                <td className="text-green-400">Active</td>
              </tr>

              <tr className="border-b border-slate-800">
                <td className="py-4 text-white">Node.js Backend</td>
                <td className="text-indigo-400">45%</td>
                <td className="text-green-400">82%</td>
                <td className="text-yellow-400">In Progress</td>
              </tr>

              <tr>
                <td className="py-4 text-white">Generative AI</td>
                <td className="text-indigo-400">88%</td>
                <td className="text-green-400">95%</td>
                <td className="text-green-400">Excellent</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Analytics;
