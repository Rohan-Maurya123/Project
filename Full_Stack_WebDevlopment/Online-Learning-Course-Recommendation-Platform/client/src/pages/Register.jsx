import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { motion } from "framer-motion";
import { 
  Mail, 
  Lock, 
  UserPlus, 
  User, 
  BookOpen, 
  Eye, 
  EyeOff,
  Check,
  ArrowRight,
  Sparkles,
  Zap,
  TrendingUp,
  Award
} from "lucide-react";
import axios from "axios";

const Register = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ name: "", email: "", password: "" });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [interests, setInterests] = useState(["Programming", "Data Science"]);
  
  const allInterests = [
    { id: "Programming", color: "from-blue-500 to-cyan-500" },
    { id: "Data Science", color: "from-emerald-500 to-teal-500" },
    { id: "Design", color: "from-pink-500 to-rose-500" },
    { id: "Marketing", color: "from-amber-500 to-orange-500" },
    { id: "Cloud", color: "from-indigo-500 to-violet-500" },
    { id: "AI", color: "from-purple-500 to-fuchsia-500" }
  ];

  const toggleInterest = (interest) => {
    setInterests(prev => 
      prev.includes(interest) 
        ? prev.filter(i => i !== interest)
        : [...prev, interest]
    );
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      const res = await axios.post("http://localhost:5000/api/auth/register", {
        ...formData,
        interests
      });
      localStorage.setItem("user", JSON.stringify(res.data));
      navigate("/dashboard");
    } catch (err) {
      setError(err.response?.data || "Registration failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.12
      }
    }
  };

  const itemVariants = {
    hidden: { y: 40, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1,
      transition: { duration: 0.7, ease: "easeOut", type: "spring" }
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4 py-8 overflow-hidden relative bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950">
      {/* Background Gradient Orbs */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <motion.div
          animate={{
            x: [0, 150, 0],
            y: [0, 80, 0],
            scale: [1, 1.3, 1],
            rotate: [0, 90, 0],
          }}
          transition={{
            duration: 25,
            repeat: Infinity,
            ease: "easeInOut"
          }}
          className="absolute -top-60 -right-60 w-[500px] h-[500px] bg-gradient-to-br from-purple-500/30 via-pink-500/20 to-cyan-500/30 rounded-full blur-3xl"
        />
        <motion.div
          animate={{
            x: [0, -150, 0],
            y: [0, -80, 0],
            scale: [1, 1.4, 1],
            rotate: [0, -90, 0],
          }}
          transition={{
            duration: 30,
            repeat: Infinity,
            ease: "easeInOut"
          }}
          className="absolute -bottom-60 -left-60 w-[500px] h-[500px] bg-gradient-to-br from-cyan-500/30 via-blue-500/20 to-purple-500/30 rounded-full blur-3xl"
        />
        {/* Grid Pattern Overlay */}
        <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMSIgY3k9IjEiIHI9IjEiIGZpbGw9InJnYmEoMjU1LDI1NSwyNTUsMC4wMykiLz48L3N2Zz4=')] opacity-50" />
      </div>

      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="visible"
        className="w-full max-w-3xl relative z-10"
      >
        {/* Main Card */}
        <motion.div
          variants={itemVariants}
          className="relative"
        >
          {/* Glow Border */}
          <div className="absolute -inset-1 bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 rounded-[3rem] blur-lg opacity-75 group-hover:opacity-100 transition duration-1000" />
          
          {/* Glass Card */}
          <div className="relative bg-white/5 backdrop-blur-3xl border border-white/20 rounded-[3rem] p-10 md:p-14 shadow-2xl">
            {/* Logo Section */}
            <motion.div className="text-center mb-12">
              <div className="inline-flex items-center justify-center w-28 h-28 rounded-3xl bg-gradient-to-br from-purple-500 via-pink-500 to-cyan-500 mb-8 shadow-[0_0_60px_rgba(168,85,247,0.5)]">
                <BookOpen className="w-14 h-14 text-white" />
              </div>
              <h1 className="text-5xl md:text-6xl font-black bg-gradient-to-r from-white via-purple-200 to-pink-200 bg-clip-text text-transparent mb-4">
                Join Learners Hub
              </h1>
              <p className="text-xl text-slate-300 font-medium">
                Start your personalized learning journey today
              </p>
            </motion.div>

            {/* Features */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
              {[
                { icon: Sparkles, label: "Personalized", color: "text-yellow-400" },
                { icon: Zap, label: "Fast", color: "text-cyan-400" },
                { icon: TrendingUp, label: "Effective", color: "text-green-400" },
                { icon: Award, label: "Premium", color: "text-purple-400" }
              ].map((feature, i) => (
                <motion.div
                  key={i}
                  variants={itemVariants}
                  className="text-center p-4 rounded-2xl bg-white/5 border border-white/10"
                >
                  <feature.icon className={`w-8 h-8 mx-auto mb-2 ${feature.color}`} />
                  <p className="text-sm font-semibold text-slate-200">{feature.label}</p>
                </motion.div>
              ))}
            </div>

            {/* Error Message */}
            {error && (
              <motion.div
                variants={itemVariants}
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: "auto" }}
                className="mb-8 p-5 rounded-2xl bg-red-500/10 border border-red-500/20 text-red-200 flex items-center gap-3"
              >
                <svg className="w-6 h-6 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
                <span className="font-medium">{error}</span>
              </motion.div>
            )}

            <form onSubmit={handleRegister} className="space-y-6">
              {/* Name */}
              <motion.div variants={itemVariants} className="space-y-3">
                <label className="text-sm font-bold text-slate-200 flex items-center gap-2 ml-1 tracking-wide">
                  <User className="w-5 h-5 text-pink-400" /> 
                  Full Name
                </label>
                <div className="relative group">
                  <div className="absolute inset-0 bg-gradient-to-r from-pink-500/20 to-purple-500/20 rounded-2xl blur opacity-0 group-focus-within:opacity-100 transition duration-500" />
                  <input
                    type="text"
                    required
                    className="relative w-full px-6 py-5 rounded-2xl bg-white/10 border-2 border-white/20 text-white placeholder-slate-400 focus:outline-none focus:border-pink-400 focus:bg-white/15 transition-all duration-300 text-lg font-medium"
                    placeholder="John Doe"
                    value={formData.name}
                    onChange={(e) => setFormData({...formData, name: e.target.value})}
                  />
                </div>
              </motion.div>

              {/* Email */}
              <motion.div variants={itemVariants} className="space-y-3">
                <label className="text-sm font-bold text-slate-200 flex items-center gap-2 ml-1 tracking-wide">
                  <Mail className="w-5 h-5 text-purple-400" /> 
                  Email Address
                </label>
                <div className="relative group">
                  <div className="absolute inset-0 bg-gradient-to-r from-purple-500/20 to-cyan-500/20 rounded-2xl blur opacity-0 group-focus-within:opacity-100 transition duration-500" />
                  <input
                    type="email"
                    required
                    className="relative w-full px-6 py-5 rounded-2xl bg-white/10 border-2 border-white/20 text-white placeholder-slate-400 focus:outline-none focus:border-purple-400 focus:bg-white/15 transition-all duration-300 text-lg font-medium"
                    placeholder="you@example.com"
                    value={formData.email}
                    onChange={(e) => setFormData({...formData, email: e.target.value})}
                  />
                </div>
              </motion.div>

              {/* Password */}
              <motion.div variants={itemVariants} className="space-y-3">
                <label className="text-sm font-bold text-slate-200 flex items-center gap-2 ml-1 tracking-wide">
                  <Lock className="w-5 h-5 text-cyan-400" /> 
                  Password
                </label>
                <div className="relative group">
                  <div className="absolute inset-0 bg-gradient-to-r from-cyan-500/20 to-blue-500/20 rounded-2xl blur opacity-0 group-focus-within:opacity-100 transition duration-500" />
                  <input
                    type={showPassword ? "text" : "password"}
                    required
                    className="relative w-full px-6 py-5 pr-16 rounded-2xl bg-white/10 border-2 border-white/20 text-white placeholder-slate-400 focus:outline-none focus:border-cyan-400 focus:bg-white/15 transition-all duration-300 text-lg font-medium"
                    placeholder="••••••••"
                    value={formData.password}
                    onChange={(e) => setFormData({...formData, password: e.target.value})}
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white transition-colors"
                  >
                    {showPassword ? <EyeOff className="w-6 h-6" /> : <Eye className="w-6 h-6" />}
                  </button>
                </div>
              </motion.div>

              {/* Interests */}
              <motion.div variants={itemVariants} className="space-y-5">
                <label className="text-sm font-bold text-slate-200 flex items-center gap-2 ml-1 tracking-wide">
                  What are you interested in? (For personalized recommendations)
                </label>
                <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                  {allInterests.map((interest) => (
                    <motion.button
                      key={interest.id}
                      type="button"
                      whileHover={{ scale: 1.05 }}
                      whileTap={{ scale: 0.95 }}
                      onClick={() => toggleInterest(interest.id)}
                      className={`px-5 py-4 rounded-2xl text-base font-black transition-all duration-300 flex items-center justify-center gap-3 border-2 ${
                        interests.includes(interest.id)
                          ? `bg-gradient-to-r ${interest.color} text-white border-transparent shadow-[0_10px_40px_rgba(0,0,0,0.3)]`
                          : "bg-white/5 border-white/20 text-slate-300 hover:border-purple-400/50 hover:bg-white/10"
                      }`}
                    >
                      {interests.includes(interest.id) && <Check className="w-5 h-5" />}
                      {interest.id}
                    </motion.button>
                  ))}
                </div>
              </motion.div>

              {/* Submit Button */}
              <motion.button
                variants={itemVariants}
                whileHover={{ scale: 1.03, boxShadow: "0 0 40px rgba(168,85,247,0.4)" }}
                whileTap={{ scale: 0.98 }}
                type="submit"
                disabled={loading}
                className="w-full bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 text-white font-black py-5 px-8 rounded-2xl shadow-[0_20px_60px_rgba(168,85,247,0.3)] hover:shadow-[0_20px_80px_rgba(168,85,247,0.5)] transition-all duration-300 flex items-center justify-center gap-4 text-xl"
              >
                {loading ? (
                  <div className="w-7 h-7 border-4 border-white/30 border-t-white rounded-full animate-spin" />
                ) : (
                  <>
                    <UserPlus className="w-7 h-7" />
                    Create Account
                  </>
                )}
              </motion.button>
            </form>

            {/* Footer Link */}
            <motion.div variants={itemVariants} className="mt-12 text-center">
              <p className="text-lg text-slate-300">
                Already have an account?{" "}
                <Link 
                  to="/login" 
                  className="text-purple-300 hover:text-purple-200 font-black transition-colors inline-flex items-center gap-2 text-xl"
                >
                  Sign in 
                  <ArrowRight className="w-6 h-6" />
                </Link>
              </p>
            </motion.div>
          </div>
        </motion.div>

        {/* Animated Bottom Dots */}
        <motion.div variants={itemVariants} className="mt-14 flex justify-center gap-6">
          {[1, 2, 3, 4, 5].map((i) => (
            <motion.div
              key={i}
              animate={{
                y: [0, -15, 0],
                opacity: [0.3, 1, 0.3],
              }}
              transition={{
                duration: 2.5,
                repeat: Infinity,
                delay: i * 0.25,
                ease: "easeInOut"
              }}
              className="w-3 h-3 rounded-full bg-gradient-to-r from-purple-400 to-pink-400 shadow-[0_0_20px_rgba(168,85,247,0.5)]"
            />
          ))}
        </motion.div>
      </motion.div>
    </div>
  );
};

export default Register;
