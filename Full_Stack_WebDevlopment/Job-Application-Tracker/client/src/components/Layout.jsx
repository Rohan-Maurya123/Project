import { NavLink, Outlet } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import { useState } from "react";
import {
  LayoutDashboard,
  Briefcase,
  BarChart3,
  Settings,
  Sparkles,
  Menu,
  X,
  Bell,
  Search,
} from "lucide-react";
import { RippleEffect } from "./RippleEffect";

const navItems = [
  { to: "/", label: "Dashboard", icon: LayoutDashboard },
  { to: "/jobs", label: "Applications", icon: Briefcase },
  { to: "/analytics", label: "Analytics", icon: BarChart3 },
  { to: "/settings", label: "Settings", icon: Settings },
];

export default function Layout() {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="flex min-h-screen">
      {/* Mobile overlay */}
      <AnimatePresence>
        {sidebarOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSidebarOpen(false)}
            className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 lg:hidden"
          />
        )}
      </AnimatePresence>

      {/* SIDEBAR */}
      <motion.aside
        initial={false}
        animate={{ x: sidebarOpen ? 0 : -300 }}
        className="fixed lg:static z-50 w-72 h-full p-6 bg-white/5 backdrop-blur-2xl border-r border-white/10 flex flex-col"
      >
        {/* BRAND */}
        <div className="flex items-center justify-between mb-10">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
              <Sparkles className="text-white" size={20} />
            </div>
            <h1 className="text-xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
              JobTracker
            </h1>
          </div>
          <RippleEffect>
            <button
              onClick={() => setSidebarOpen(false)}
              className="lg:hidden p-2 hover:bg-white/10 rounded-xl transition-all"
            >
              <X size={20} className="text-gray-300" />
            </button>
          </RippleEffect>
        </div>

        {/* NAV BUTTONS */}
        <nav className="space-y-2 flex-1">
          {navItems.map((item, i) => {
            const Icon = item.icon;

            return (
              <NavLink key={i} to={item.to} onClick={() => setSidebarOpen(false)}>
                {({ isActive }) => (
                  <RippleEffect>
                    <motion.div
                      whileHover={{ scale: 1.02, x: 4 }}
                      whileTap={{ scale: 0.98 }}
                      className={`
                        flex items-center gap-3 px-4 py-3 rounded-2xl cursor-pointer transition-all
                        ${
                          isActive
                            ? "bg-gradient-to-r from-purple-500/20 to-pink-500/20 text-purple-300 border border-purple-500/30 shadow-md"
                            : "bg-white/5 text-gray-300 border border-white/10 hover:bg-white/10 hover:border-white/20"
                        }
                      `}
                    >
                      <Icon size={18} />
                      <span className="font-medium">{item.label}</span>
                    </motion.div>
                  </RippleEffect>
                )}
              </NavLink>
            );
          })}
        </nav>

        {/* bottom card */}
        <div className="mt-10">
          <motion.div
            whileHover={{ y: -2 }}
            className="p-5 rounded-2xl bg-gradient-to-br from-purple-500/15 to-blue-500/10 border border-purple-500/20"
          >
            <div className="flex items-center gap-2 mb-2">
              <Sparkles size={16} className="text-yellow-400" />
              <p className="text-sm font-semibold text-white">AI Insights</p>
            </div>
            <p className="text-xs text-gray-400 mb-3">Your application success rate is up 15% this week!</p>
            <div className="w-full h-2 bg-white/10 rounded-full overflow-hidden">
              <motion.div
                initial={{ width: 0 }}
                animate={{ width: "75%" }}
                transition={{ duration: 1, ease: "easeOut" }}
                className="h-full bg-gradient-to-r from-purple-500 to-pink-500 rounded-full"
              />
            </div>
          </motion.div>
        </div>
      </motion.aside>

      {/* MAIN */}
      <div className="flex-1 flex flex-col min-h-screen">
        {/* Top header */}
        <header className="sticky top-0 z-30 px-8 py-4 bg-white/5 backdrop-blur-xl border-b border-white/10">
          <div className="flex items-center justify-between gap-4">
            <div className="flex items-center gap-4">
              <RippleEffect>
                <button
                  onClick={() => setSidebarOpen(true)}
                  className="lg:hidden p-2.5 hover:bg-white/10 rounded-xl transition-all"
                >
                  <Menu size={20} className="text-gray-300" />
                </button>
              </RippleEffect>
              <div className="relative hidden sm:block">
                <Search size={18} className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-500" />
                <input
                  type="text"
                  placeholder="Search applications..."
                  className="pl-12 pr-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 focus:bg-white/10 transition-all w-96 text-gray-200"
                />
              </div>
            </div>
            <div className="flex items-center gap-3">
              <RippleEffect>
                <button className="relative p-2.5 hover:bg-white/10 rounded-xl transition-all">
                  <Bell size={20} className="text-gray-300" />
                  <span className="absolute top-2 right-2 w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-gray-900" />
                </button>
              </RippleEffect>
              <motion.div
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="flex items-center gap-3 p-2 bg-white/5 rounded-xl border border-white/10 hover:bg-white/10 cursor-pointer transition-all"
              >
                <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-white font-bold">
                  RP
                </div>
                <div className="hidden sm:block">
                  <p className="text-sm font-medium text-white">Rohan Maurya</p>
                  <p className="text-xs text-gray-500">Pro Plan</p>
                </div>
              </motion.div>
            </div>
          </div>
        </header>
        
        <main className="flex-1 p-8 overflow-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
