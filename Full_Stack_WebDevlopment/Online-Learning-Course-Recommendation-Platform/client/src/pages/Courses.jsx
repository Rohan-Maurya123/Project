import React, { useState, useEffect } from "react";
import { Search, Star } from "lucide-react";
import CourseCard from "../components/CourseCard";

const mockCourses = [
  { _id: 1, title: "Complete Web Development Bootcamp", category: "Programming", level: "Beginner", tags: ["JavaScript", "React", "Node"] },
  { _id: 2, title: "Advanced React Patterns", category: "Programming", level: "Advanced", tags: ["React", "TypeScript"] },
  { _id: 3, title: "Data Science Fundamentals", category: "Data Science", level: "Intermediate", tags: ["Python", "Pandas", "ML"] },
  { _id: 4, title: "UI/UX Design Masterclass", category: "Design", level: "Beginner", tags: ["Figma", "Design"] },
  { _id: 5, title: "AWS Cloud Practitioner", category: "Cloud", level: "Beginner", tags: ["AWS", "Cloud"] },
  { _id: 6, title: "Machine Learning Essentials", category: "Data Science", level: "Advanced", tags: ["ML", "Python"] },
  { _id: 7, title: "Digital Marketing 101", category: "Marketing", level: "Beginner", tags: ["Marketing", "SEO"] },
  { _id: 8, title: "React Native Development", category: "Programming", level: "Intermediate", tags: ["React Native", "Mobile"] },
];

const categories = [
  { name: "All", courses: "15,234" },
  { name: "Programming", courses: "3,456" },
  { name: "Data Science", courses: "2,123" },
  { name: "Design", courses: "1,876" },
  { name: "Marketing", courses: "1,543" },
  { name: "Cloud", courses: "1,123" },
  { name: "AI", courses: "876" }
];

const levels = ["All", "Beginner", "Intermediate", "Advanced"];

export default function Courses() {
  const [filteredCourses, setFilteredCourses] = useState(mockCourses);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [level, setLevel] = useState("All");
  const [sortBy, setSortBy] = useState("popular");

  useEffect(() => {
    let filtered = [...mockCourses];

    if (search) {
      filtered = filtered.filter(course =>
        course.title.toLowerCase().includes(search.toLowerCase())
      );
    }

    if (category !== "All") {
      filtered = filtered.filter(course => course.category === category);
    }

    if (level !== "All") {
      filtered = filtered.filter(course => course.level === level);
    }

    setFilteredCourses(filtered);
  }, [search, category, level]);

  return (
    <div className="max-w-7xl mx-auto px-6">
      {/* Header */}
      <div className="mb-10">
        <h1 className="text-4xl font-bold text-gradient mb-2">Browse Courses</h1>
        <p className="text-lg text-slate-400">Find the perfect course for your learning journey</p>
      </div>

      <div className="flex flex-col lg:flex-row gap-8">
        {/* Filters Sidebar */}
        <div className="lg:w-72 flex-shrink-0">
          <div className="glass-card p-6 sticky top-24">
            <h3 className="font-bold text-white mb-6 text-lg">Filters</h3>

            {/* Search */}
            <div className="mb-8">
              <label className="block text-sm font-semibold text-slate-300 mb-3">Search</label>
              <div className="relative">
                <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" />
                <input
                  type="text"
                  placeholder="Search courses..."
                  className="w-full pl-12 pr-4 py-3.5 rounded-xl border border-white/10 bg-white/5 text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-300"
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                />
              </div>
            </div>

            {/* Categories */}
            <div className="mb-8">
              <label className="block text-sm font-semibold text-slate-300 mb-3">Category</label>
              <div className="space-y-2">
                {categories.map((cat) => (
                  <button
                    key={cat.name}
                    onClick={() => setCategory(cat.name)}
                    className={`w-full flex items-center justify-between px-4 py-2.5 rounded-xl text-left transition-all duration-200 ${
                      category === cat.name
                        ? "bg-purple-500/20 text-purple-300 font-semibold border border-purple-500/30"
                        : "text-slate-400 hover:bg-white/5 hover:text-white"
                    }`}
                  >
                    <span>{cat.name}</span>
                    <span className="text-xs text-slate-500">{cat.courses}</span>
                  </button>
                ))}
              </div>
            </div>

            {/* Level */}
            <div className="mb-8">
              <label className="block text-sm font-semibold text-slate-300 mb-3">Level</label>
              <div className="space-y-2">
                {levels.map((lvl) => (
                  <button
                    key={lvl}
                    onClick={() => setLevel(lvl)}
                    className={`w-full flex items-center justify-between px-4 py-2.5 rounded-xl text-left transition-all duration-200 ${
                      level === lvl
                        ? "bg-purple-500/20 text-purple-300 font-semibold border border-purple-500/30"
                        : "text-slate-400 hover:bg-white/5 hover:text-white"
                    }`}
                  >
                    <span>{lvl}</span>
                  </button>
                ))}
              </div>
            </div>

            {/* Reset */}
            <button
              onClick={() => {
                setSearch("");
                setCategory("All");
                setLevel("All");
              }}
              className="w-full bg-white/5 border border-white/10 text-slate-300 font-semibold py-2.5 rounded-xl hover:bg-white/10 hover:text-white transition-all duration-300"
            >
              Reset Filters
            </button>
          </div>
        </div>

        {/* Course Grid */}
        <div className="flex-1">
          {/* Sort Bar */}
          <div className="glass-card p-5 mb-6 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <p className="text-slate-400 font-medium">
                Showing <span className="text-purple-300 font-bold">{filteredCourses.length}</span> courses
              </p>
            </div>
            <div className="flex items-center gap-3">
              <select
                value={sortBy}
                onChange={(e) => setSortBy(e.target.value)}
                className="px-4 py-2.5 rounded-xl border border-white/10 bg-white/5 text-white focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-300"
              >
                <option value="popular">Most Popular</option>
                <option value="newest">Newest</option>
                <option value="rating">Highest Rated</option>
                <option value="price-low">Price: Low to High</option>
                <option value="price-high">Price: High to Low</option>
              </select>
            </div>
          </div>

          {/* Course Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
            {filteredCourses.map((course, i) => (
              <CourseCard key={course._id} course={course} />
            ))}
          </div>

          {filteredCourses.length === 0 && (
            <div className="glass-card p-12 text-center">
              <h3 className="text-xl font-bold text-white mb-2">No courses found</h3>
              <p className="text-slate-400">Try adjusting your filters or search terms</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
