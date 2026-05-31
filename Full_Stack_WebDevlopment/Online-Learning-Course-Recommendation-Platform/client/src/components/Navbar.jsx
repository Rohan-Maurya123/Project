import React, { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { motion } from "framer-motion";
import {
  Home,
  BookOpen,
  TrendingUp,
  BarChart3,
  BookmarkCheck,
  User,
  GraduationCap
} from "lucide-react";

const Navbar = () => {
  const location = useLocation();
  const [isHovered, setIsHovered] = useState(-1);

  const navItems = [
    { path: "/dashboard", icon: Home, label: "Dashboard" },
    { path: "/courses", icon: BookOpen, label: "Browse Courses" },
    { path: "/recommendations", icon: TrendingUp, label: "Recommended" },
    { path: "/enrolled", icon: BookmarkCheck, label: "My Learning" },
    { path: "/analytics", icon: BarChart3, label: "Analytics" },
  ];

  return (
    <motion.nav
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, type: "spring" }}
      className="fixed top-0 left-0 right-0 z-50 border-b border-white/10 bg-slate-950/80 backdrop-blur-3xl"
    >
      <div className="max-w-7xl mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          {/* Logo */}
          <Link
            to="/dashboard"
            className="flex items-center gap-3 group"
          >
            <motion.div
              whileHover={{ scale: 1.1, rotate: 5 }}
              transition={{ type: "spring", stiffness: 400 }}
              className="w-12 h-12 rounded-2xl bg-gradient-to-br from-purple-600 via-pink-500 to-cyan-500 flex items-center justify-center shadow-2xl shadow-purple-500/40"
            >
              <GraduationCap className="w-7 h-7 text-white" />
            </motion.div>
            <div>
              <h1 className="text-2xl font-bold bg-gradient-to-r from-white via-purple-200 to-pink-200 bg-clip-text text-transparent">
                LearnerPro
              </h1>
              <p className="text-xs text-slate-400">Learn Anything, Anytime</p>
            </div>
          </Link>

          {/* Centered Navigation */}
          <div className="flex items-center gap-1">
            {navItems.map((item, index) => {
              const isActive = location.pathname === item.path;
              const IconComponent = item.icon;

              return (
                <Link
                  key={item.path}
                  to={item.path}
                  onMouseEnter={() => setIsHovered(index)}
                  onMouseLeave={() => setIsHovered(-1)}
                >
                  <motion.div
                    whileHover={{ scale: 1.08, y: -2 }}
                    whileTap={{ scale: 0.95 }}
                    transition={{ type: "spring", stiffness: 400 }}
                    className={`relative px-6 py-3 rounded-2xl transition-all duration-400 ${
                      isActive
                        ? "bg-gradient-to-r from-purple-600/20 to-pink-600/20 border border-purple-500/30"
                        : "hover:bg-white/5 border border-transparent"
                    }`}
                  >
                    <div className="flex flex-col items-center gap-1">
                      <IconComponent
                        className={`w-5 h-5 transition-colors duration-300 ${
                          isActive ? "text-purple-300" : "text-slate-400 hover:text-white"
                        }`}
                      />
                      <span
                        className={`text-sm font-medium transition-colors duration-300 ${
                          isActive
                            ? "text-gradient"
                            : "text-slate-400 hover:text-white"
                        }`}
                        style={{
                          background: isActive ? "linear-gradient(90deg, #fff, #a78bfa, #f472b6)" : "none",
                          WebkitBackgroundClip: isActive ? "text" : "none",
                          WebkitTextFillColor: isActive ? "transparent" : "inherit"
                        }}
                      >
                        {item.label}
                      </span>
                    </div>

                    {/* Active indicator */}
                    {isActive && (
                      <motion.div
                        layoutId="activeNavIndicator"
                        className="absolute bottom-0 left-1/2 -translate-x-1/2 w-1/3 h-1 bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 rounded-full"
                        initial={{ opacity: 0, scale: 0 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ type: "spring", stiffness: 300, damping: 20 }}
                      />
                    )}
                  </motion.div>
                </Link>
              );
            })}
          </div>

          {/* User Profile */}
          <div className="flex items-center gap-4">
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="px-6 py-2.5 bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold rounded-xl shadow-2xl shadow-purple-500/40 hover:shadow-purple-500/60 transition-all duration-300"
            >
              Get Pro
            </motion.button>

            <motion.div
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.95 }}
              className="w-12 h-12 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-xl font-bold text-white shadow-xl"
            >
              <User className="w-6 h-6" />
            </motion.div>
          </div>
        </div>
      </div>
    </motion.nav>
  );
};

export default Navbar;
