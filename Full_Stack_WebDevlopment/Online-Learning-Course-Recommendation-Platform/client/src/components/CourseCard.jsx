import React from "react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { Star, Clock, Users, Bookmark } from "lucide-react";

const CourseCard = ({ course, progress, showProgress = false }) => {
  const navigate = useNavigate();

  // Sample course images
  const courseImages = {
    "Programming": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=400&h=225&fit=crop",
    "Data Science": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=225&fit=crop",
    "Design": "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=400&h=225&fit=crop",
    "Marketing": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400&h=225&fit=crop",
    "Cloud": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400&h=225&fit=crop",
    "AI": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400&h=225&fit=crop"
  };

  const categoryBadges = {
    "Programming": "bg-purple-500/20 text-purple-300 border-purple-500/30",
    "Data Science": "bg-green-500/20 text-green-300 border-green-500/30",
    "Design": "bg-pink-500/20 text-pink-300 border-pink-500/30",
    "Marketing": "bg-amber-500/20 text-amber-300 border-amber-500/30",
    "Cloud": "bg-blue-500/20 text-blue-300 border-blue-500/30",
    "AI": "bg-cyan-500/20 text-cyan-300 border-cyan-500/30"
  };

  return (
    <motion.div
      whileHover={{ y: -8, scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
      className="glass-card cursor-pointer overflow-hidden"
      onClick={() => navigate(`/course/${course._id}`)}
    >
      {/* Course Image */}
      <div className="relative">
        <img
          src={courseImages[course.category] || courseImages["Programming"]}
          alt={course.title}
          className="w-full h-40 object-cover group-hover:scale-110 transition-all duration-300"
        />
        <div className="absolute top-3 right-3 flex items-center gap-2">
          <button className="p-2 bg-white/10 backdrop-blur-md rounded-full hover:bg-white/20 transition-all duration-200">
            <Bookmark className="w-4 h-4 text-white" />
          </button>
        </div>
        {showProgress && (
          <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-white font-semibold text-sm">{progress}% Complete</span>
            </div>
            <div className="h-2 bg-white/20 rounded-full overflow-hidden">
              <div
                className="h-full bg-gradient-to-r from-purple-500 to-blue-500"
                style={{ width: `${progress}%` }}
              />
            </div>
          </div>
        )}
      </div>

      {/* Course Content */}
      <div className="p-5 space-y-3">
        <div className="flex items-center gap-2">
          <span className={`px-2.5 py-0.5 rounded-full text-xs font-medium border ${categoryBadges[course.category] || "bg-purple-500/20 text-purple-300 border-purple-500/30"}`}>
            {course.category}
          </span>
          <span className="text-xs text-slate-400">• {course.level}</span>
        </div>

        <h3 className="font-bold text-white text-base line-clamp-2 group-hover:text-purple-300 transition-all duration-200">
          {course.title}
        </h3>

        {/* Stats */}
        <div className="flex items-center gap-4 text-sm text-slate-400">
          <div className="flex items-center gap-1">
            <Star className="w-4 h-4 fill-yellow-400 text-yellow-400" />
            <span className="text-slate-300 font-semibold">4.8</span>
            <span className="text-slate-500">(12.5k)</span>
          </div>
          <div className="flex items-center gap-1">
            <Clock className="w-4 h-4" />
            <span>12h 30m</span>
          </div>
          <div className="flex items-center gap-1">
            <Users className="w-4 h-4" />
            <span>45.2k</span>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default CourseCard;
