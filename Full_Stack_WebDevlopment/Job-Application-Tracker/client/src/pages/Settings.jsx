import { useState } from "react";
import {
  User,
  Bell,
  Shield,
  Palette,
  Key,
  Database,
  Globe,
  Trash2,
  Save,
  CheckCircle2,
  ChevronRight,
} from "lucide-react";

export default function Settings() {
  const [activeTab, setActiveTab] = useState("profile");
  const [notifications, setNotifications] = useState({
    email: true,
    push: true,
    interviewReminders: true,
    applicationUpdates: true,
  });
  const [darkMode, setDarkMode] = useState(true);

  const tabs = [
    { id: "profile", label: "Profile", icon: User },
    { id: "notifications", label: "Notifications", icon: Bell },
    { id: "appearance", label: "Appearance", icon: Palette },
    { id: "security", label: "Security", icon: Shield },
    { id: "data", label: "Data & Privacy", icon: Database },
  ];

  return (
    <div className="space-y-6">
      {/* HEADER */}
      <div>
        <h1 className="text-3xl font-bold">⚙ Settings</h1>
        <p className="text-gray-400 mt-1">Manage your account preferences</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* SIDEBAR */}
        <div className="lg:col-span-1">
          <div className="p-4 rounded-2xl bg-white/5 border border-white/10 space-y-1">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                    activeTab === tab.id
                      ? "bg-purple-500/20 text-purple-300 border border-purple-500/30"
                      : "text-gray-300 hover:bg-white/10"
                  }`}
                >
                  <Icon size={18} />
                  <span className="font-medium">{tab.label}</span>
                  {activeTab === tab.id && <ChevronRight size={16} className="ml-auto" />}
                </button>
              );
            })}
          </div>
        </div>

        {/* CONTENT */}
        <div className="lg:col-span-3 space-y-6">
          {activeTab === "profile" && (
            <div className="p-6 rounded-2xl bg-white/5 border border-white/10">
              <h2 className="text-xl font-semibold mb-6">Profile Settings</h2>
              
              <div className="flex items-center gap-6 mb-8">
                <div className="w-24 h-24 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-3xl font-bold">
                  RP
                </div>
                <div className="space-y-2">
                  <button className="px-4 py-2 bg-white/10 border border-white/20 rounded-xl hover:bg-white/20 transition font-medium">
                    Change Photo
                  </button>
                  <p className="text-sm text-gray-500">JPG, PNG or GIF. Max 2MB.</p>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">First Name</label>
                  <input
                    type="text"
                    defaultValue="Rohan"
                    className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Last Name</label>
                  <input
                    type="text"
                    defaultValue="Ptk"
                    className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50"
                  />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-gray-300 mb-2">Email Address</label>
                  <input
                    type="email"
                    defaultValue="rohan@example.com"
                    className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50"
                  />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-gray-300 mb-2">Job Title</label>
                  <input
                    type="text"
                    defaultValue="Full Stack Developer"
                    className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50"
                  />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-gray-300 mb-2">Bio</label>
                  <textarea
                    rows={4}
                    defaultValue="Passionate developer looking for new opportunities..."
                    className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 resize-none"
                  />
                </div>
              </div>

              <div className="flex justify-end mt-8">
                <button className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl hover:opacity-90 transition font-medium">
                  <Save size={18} />
                  Save Changes
                </button>
              </div>
            </div>
          )}

          {activeTab === "notifications" && (
            <div className="p-6 rounded-2xl bg-white/5 border border-white/10 space-y-6">
              <h2 className="text-xl font-semibold">Notification Preferences</h2>
              
              <div className="space-y-4">
                {[
                  { key: "email", label: "Email Notifications", desc: "Receive updates via email" },
                  { key: "push", label: "Push Notifications", desc: "Receive browser notifications" },
                  { key: "interviewReminders", label: "Interview Reminders", desc: "Get reminded before interviews" },
                  { key: "applicationUpdates", label: "Application Updates", desc: "Status changes for your applications" },
                ].map((item) => (
                  <div key={item.key} className="flex items-center justify-between p-4 bg-white/5 rounded-xl border border-white/10">
                    <div>
                      <p className="font-medium">{item.label}</p>
                      <p className="text-sm text-gray-400">{item.desc}</p>
                    </div>
                    <button
                      onClick={() => setNotifications({ ...notifications, [item.key]: !notifications[item.key] })}
                      className={`w-14 h-7 rounded-full transition relative ${
                        notifications[item.key] ? "bg-purple-500" : "bg-white/20"
                      }`}
                    >
                      <div className={`absolute top-1 w-5 h-5 bg-white rounded-full transition-all ${
                        notifications[item.key] ? "left-8" : "left-1"
                      }`} />
                    </button>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeTab === "appearance" && (
            <div className="p-6 rounded-2xl bg-white/5 border border-white/10 space-y-6">
              <h2 className="text-xl font-semibold">Appearance</h2>
              
              <div className="space-y-4">
                <div className="flex items-center justify-between p-4 bg-white/5 rounded-xl border border-white/10">
                  <div>
                    <p className="font-medium">Dark Mode</p>
                    <p className="text-sm text-gray-400">Toggle dark/light theme</p>
                  </div>
                  <button
                    onClick={() => setDarkMode(!darkMode)}
                    className={`w-14 h-7 rounded-full transition relative ${
                      darkMode ? "bg-purple-500" : "bg-white/20"
                    }`}
                  >
                    <div className={`absolute top-1 w-5 h-5 bg-white rounded-full transition-all ${
                      darkMode ? "left-8" : "left-1"
                    }`} />
                  </button>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-4">Accent Color</label>
                  <div className="flex gap-4">
                    {["#8b5cf6", "#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#ec4899"].map((color) => (
                      <button
                        key={color}
                        style={{ backgroundColor: color }}
                        className={`w-10 h-10 rounded-full border-2 ${color === "#8b5cf6" ? "border-white" : "border-transparent"}`}
                      />
                    ))}
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === "security" && (
            <div className="space-y-6">
              <div className="p-6 rounded-2xl bg-white/5 border border-white/10">
                <h2 className="text-xl font-semibold mb-6">Change Password</h2>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Current Password</label>
                    <input
                      type="password"
                      className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">New Password</label>
                    <input
                      type="password"
                      className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Confirm New Password</label>
                    <input
                      type="password"
                      className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50"
                    />
                  </div>
                  <button className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl hover:opacity-90 transition font-medium">
                    <Key size={18} />
                    Update Password
                  </button>
                </div>
              </div>

              <div className="p-6 rounded-2xl bg-white/5 border border-white/10">
                <h2 className="text-xl font-semibold mb-6">Two-Factor Authentication</h2>
                <div className="flex items-center justify-between p-4 bg-white/5 rounded-xl border border-white/10">
                  <div className="flex items-center gap-3">
                    <Shield className="text-green-400" size={24} />
                    <div>
                      <p className="font-medium">2FA is Enabled</p>
                      <p className="text-sm text-gray-400">Your account is protected</p>
                    </div>
                  </div>
                  <CheckCircle2 className="text-green-400" size={24} />
                </div>
              </div>
            </div>
          )}

          {activeTab === "data" && (
            <div className="space-y-6">
              <div className="p-6 rounded-2xl bg-white/5 border border-white/10">
                <h2 className="text-xl font-semibold mb-6">Data Management</h2>
                <div className="space-y-4">
                  <button className="w-full flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-xl hover:bg-white/10 transition">
                    <Database size={20} className="text-blue-400" />
                    <div className="text-left">
                      <p className="font-medium">Export All Data</p>
                      <p className="text-sm text-gray-400">Download your applications as JSON</p>
                    </div>
                  </button>
                  <button className="w-full flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-xl hover:bg-white/10 transition">
                    <Globe size={20} className="text-green-400" />
                    <div className="text-left">
                      <p className="font-medium">Import Data</p>
                      <p className="text-sm text-gray-400">Import applications from a file</p>
                    </div>
                  </button>
                </div>
              </div>

              <div className="p-6 rounded-2xl bg-red-500/10 border border-red-500/30">
                <h2 className="text-xl font-semibold mb-4 text-red-400">Danger Zone</h2>
                <p className="text-gray-300 mb-4">Once you delete your account, there is no going back.</p>
                <button className="flex items-center gap-2 px-6 py-3 bg-red-500/20 text-red-400 border border-red-500/30 rounded-xl hover:bg-red-500/30 transition font-medium">
                  <Trash2 size={18} />
                  Delete Account
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
