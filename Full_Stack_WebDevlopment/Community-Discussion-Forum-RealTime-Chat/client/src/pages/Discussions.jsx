import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import { FaFire, FaEye, FaCommentDots, FaThumbsUp } from "react-icons/fa";

const discussions = [
  {
    title: "Complete MERN Roadmap 2026",
    category: "Web Development",
    author: "Aman Sharma",
    replies: 421,
    views: "12.4K",
    likes: 1890,
    status: "Trending",
  },
  {
    title: "React Interview Questions Collection",
    category: "React",
    author: "Priya Singh",
    replies: 318,
    views: "9.8K",
    likes: 1520,
    status: "Hot",
  },
  {
    title: "Node.js System Design Guide",
    category: "Backend",
    author: "Rahul Verma",
    replies: 267,
    views: "7.3K",
    likes: 1240,
    status: "Popular",
  },
  {
    title: "MongoDB Optimization Techniques",
    category: "Database",
    author: "Sneha Gupta",
    replies: 189,
    views: "5.2K",
    likes: 890,
    status: "Active",
  },
  {
    title: "Full Stack Developer Career Roadmap",
    category: "Career",
    author: "Vikas Kumar",
    replies: 512,
    views: "18.1K",
    likes: 2640,
    status: "Trending",
  },
  {
    title: "Best Portfolio Projects For Freshers",
    category: "Projects",
    author: "Ankit Yadav",
    replies: 294,
    views: "8.9K",
    likes: 1320,
    status: "Hot",
  },
];

const categories = [
  "React",
  "Node.js",
  "MongoDB",
  "JavaScript",
  "Career",
  "Projects",
  "System Design",
  "AI",
];

function Discussions() {
  return (
    <div className="flex min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-cyan-950 text-white">
      <Sidebar />

      <div className="flex-1">
        <Navbar />

        <div className="p-8">
          {/* Header */}
          <div className="mb-10">
            <h1 className="text-6xl font-black mb-3">Community Discussions</h1>

            <p className="text-slate-400 text-lg">
              Explore trending discussions, ask questions, share knowledge and
              collaborate with developers.
            </p>
          </div>

          {/* Top Stats */}
          <div className="grid md:grid-cols-4 gap-6 mb-10">
            <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-6">
              <p className="text-slate-400">Active Discussions</p>

              <h2 className="text-5xl font-black mt-3">3,421</h2>
            </div>

            <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-6">
              <p className="text-slate-400">Community Members</p>

              <h2 className="text-5xl font-black mt-3">12.8K</h2>
            </div>

            <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-6">
              <p className="text-slate-400">Comments Today</p>

              <h2 className="text-5xl font-black mt-3">1,240</h2>
            </div>

            <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-6">
              <p className="text-slate-400">Messages Sent</p>

              <h2 className="text-5xl font-black mt-3">9.2K</h2>
            </div>
          </div>

          <div className="grid xl:grid-cols-4 gap-8">
            {/* Left Section */}
            <div className="xl:col-span-3 space-y-6">
              {discussions.map((discussion, index) => (
                <div
                  key={index}
                  className="
                    bg-white/5
                    backdrop-blur-xl
                    border border-white/10
                    rounded-3xl
                    p-8
                    hover:scale-[1.01]
                    transition-all
                    duration-300
                    cursor-pointer
                  "
                >
                  <div className="flex justify-between items-center mb-4">
                    <span className="bg-cyan-500/20 text-cyan-300 px-4 py-2 rounded-full">
                      {discussion.category}
                    </span>

                    <span className="bg-orange-500/20 text-orange-300 px-4 py-2 rounded-full">
                      {discussion.status}
                    </span>
                  </div>

                  <h2 className="text-3xl font-bold mb-3">
                    {discussion.title}
                  </h2>

                  <p className="text-slate-400 mb-6">
                    Started by {discussion.author}
                  </p>

                  <div className="flex flex-wrap gap-6 text-slate-300">
                    <div className="flex items-center gap-2">
                      <FaCommentDots />
                      {discussion.replies} Replies
                    </div>

                    <div className="flex items-center gap-2">
                      <FaEye />
                      {discussion.views}
                    </div>

                    <div className="flex items-center gap-2">
                      <FaThumbsUp />
                      {discussion.likes}
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Right Sidebar */}
            <div className="space-y-8">
              {/* Trending Tags */}
              <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-6">
                <h2 className="text-2xl font-bold mb-6">Trending Topics</h2>

                <div className="flex flex-wrap gap-3">
                  {categories.map((category) => (
                    <div
                      key={category}
                      className="
                        bg-slate-800
                        px-4
                        py-2
                        rounded-full
                        hover:bg-cyan-500
                        transition-all
                        cursor-pointer
                      "
                    >
                      #{category}
                    </div>
                  ))}
                </div>
              </div>

              {/* Hot Discussions */}
              <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-6">
                <h2 className="text-2xl font-bold mb-6 flex items-center gap-3">
                  <FaFire className="text-orange-400" />
                  Hot Discussions
                </h2>

                <div className="space-y-4">
                  <div className="bg-slate-800/50 p-4 rounded-2xl">
                    React vs Next.js in 2026
                  </div>

                  <div className="bg-slate-800/50 p-4 rounded-2xl">
                    AI Impact on Developers
                  </div>

                  <div className="bg-slate-800/50 p-4 rounded-2xl">
                    Best Backend Projects
                  </div>

                  <div className="bg-slate-800/50 p-4 rounded-2xl">
                    Freelancing Guide
                  </div>
                </div>
              </div>

              {/* Community Insights */}
              <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-6">
                <h2 className="text-2xl font-bold mb-6">Community Insights</h2>

                <div className="space-y-4">
                  <div>
                    <p className="text-slate-400">New Members</p>

                    <h3 className="text-3xl font-bold">+324</h3>
                  </div>

                  <div>
                    <p className="text-slate-400">Active Today</p>

                    <h3 className="text-3xl font-bold">4,281</h3>
                  </div>

                  <div>
                    <p className="text-slate-400">Discussions Created</p>

                    <h3 className="text-3xl font-bold">128</h3>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Discussions;
