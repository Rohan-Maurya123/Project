import React from "react";
import { Link, useLocation } from "react-router-dom";
import {
  Home,
  BookOpen,
  TrendingUp,
  BarChart3,
  BookmarkCheck,
  User,
  Settings,
  HelpCircle,
  GraduationCap,
} from "lucide-react";

const Sidebar = () => {
  const location = useLocation();

  const navItems = [
    { path: "/dashboard", icon: Home, label: "Dashboard" },
    { path: "/courses", icon: BookOpen, label: "Browse Courses" },
    { path: "/recommendations", icon: TrendingUp, label: "Recommended" },
    { path: "/enrolled", icon: BookmarkCheck, label: "My Learning" },
    { path: "/analytics", icon: BarChart3, label: "Analytics" },
  ];

  return (
    <div className="w-72 glass border-r border-white/10 min-h-screen flex flex-col sticky top-0 left-0 z-30">
      {/* Logo */}
      <div className="p-6 border-b border-white/10">
        <Link to="/dashboard" className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-r from-purple-600 to-pink-600 flex items-center justify-center">
            <GraduationCap className="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-white">LearnerPro</h1>
            <p className="text-xs text-slate-400">Learn Anything, Anytime</p>
          </div>
        </Link>
      </div>

      {/* User Profile */}
      <div className="p-6 border-b border-white/10">
        <div className="flex items-center gap-3 mb-4">
          <div className="w-12 h-12 rounded-full bg-gradient-to-r from-purple-500 to-pink-500 flex items-center justify-center text-xl font-bold text-white">
            R
          </div>
          <div className="flex-1">
            <p className="font-bold text-white">Rohan Kumar</p>
            <p className="text-xs text-slate-400">rohan@gmail.com</p>
          </div>
        </div>
        <button className="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold py-2.5 rounded-xl hover:opacity-90 transition-all duration-300 shadow-lg shadow-purple-500/25">
          Upgrade to Pro
        </button>
      </div>

      {/* Navigation */}
      <nav className="flex-1 p-4 space-y-1">
        {navItems.map((item) => {
          const isActive = location.pathname === item.path;
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`flex items-center gap-3 px-4 py-3.5 rounded-xl transition-all duration-200 ${
                isActive
                  ? "bg-purple-500/20 text-purple-300 font-semibold border border-purple-500/30"
                  : "text-slate-400 hover:bg-white/5 hover:text-white"
              }`}
            >
              <item.icon className="w-5 h-5" />
              <span>{item.label}</span>
            </Link>
          );
        })}
      </nav>

      {/* Bottom Section */}
      <div className="p-4 border-t border-white/10 space-y-1">
        <button className="w-full flex items-center gap-3 px-4 py-3.5 rounded-xl text-slate-400 hover:bg-white/5 hover:text-white transition-all duration-200">
          <User className="w-5 h-5" />
          <span>Profile</span>
        </button>
        <button className="w-full flex items-center gap-3 px-4 py-3.5 rounded-xl text-slate-400 hover:bg-white/5 hover:text-white transition-all duration-200">
          <Settings className="w-5 h-5" />
          <span>Settings</span>
        </button>
        <button className="w-full flex items-center gap-3 px-4 py-3.5 rounded-xl text-slate-400 hover:bg-white/5 hover:text-white transition-all duration-200">
          <HelpCircle className="w-5 h-5" />
          <span>Help Center</span>
        </button>
      </div>
    </div>
  );
};

export default Sidebar;
