import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Plus,
  Edit,
  Trash2,
  Search,
  X,
  CheckCircle2,
  XCircle,
  Calendar,
  Link2,
  MapPin,
  DollarSign,
} from "lucide-react";
import { RippleEffect } from "../components/RippleEffect";

const initialJobs = [
  {
    id: 1,
    company: "Google",
    role: "Senior Frontend Developer",
    status: "Interview",
    date: "2024-01-15",
    salary: "$150k - $180k",
    location: "Remote",
    url: "https://google.com/careers",
    notes: "Had the first interview, waiting for second round",
    logo: "G"
  },
  {
    id: 2,
    company: "Amazon",
    role: "Backend Engineer",
    status: "Offer",
    date: "2024-01-10",
    salary: "$140k - $170k",
    location: "Seattle, WA",
    url: "https://amazon.jobs",
    notes: "Offer received! Deadline to accept is Jan 25th",
    logo: "A"
  },
  {
    id: 3,
    company: "Microsoft",
    role: "Full Stack Developer",
    status: "Applied",
    date: "2024-01-12",
    salary: "$130k - $160k",
    location: "Redmond, WA",
    url: "https://careers.microsoft.com",
    notes: "Applied through referral",
    logo: "M"
  },
  {
    id: 4,
    company: "Meta",
    role: "React Developer",
    status: "Rejected",
    date: "2024-01-05",
    salary: "$160k - $200k",
    location: "Menlo Park, CA",
    url: "https://metacareers.com",
    notes: "Rejected after final round",
    logo: "Me"
  },
  {
    id: 5,
    company: "Stripe",
    role: "Software Engineer",
    status: "Interview",
    date: "2024-01-14",
    salary: "$170k - $210k",
    location: "San Francisco, CA",
    url: "https://stripe.com/jobs",
    notes: "Technical screen scheduled for tomorrow",
    logo: "S"
  },
];

const statuses = ["All", "Applied", "Interview", "Offer", "Rejected"];

export default function Jobs() {
  const [jobs, setJobs] = useState(initialJobs);
  const [searchTerm, setSearchTerm] = useState("");
  const [filterStatus, setFilterStatus] = useState("All");
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingJob, setEditingJob] = useState(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [formData, setFormData] = useState({
    company: "",
    role: "",
    status: "Applied",
    date: new Date().toISOString().split('T')[0],
    salary: "",
    location: "",
    url: "",
    notes: "",
  });

  const filteredJobs = jobs.filter(job => {
    const matchesSearch = 
      job.company.toLowerCase().includes(searchTerm.toLowerCase()) ||
      job.role.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesStatus = filterStatus === "All" || job.status === filterStatus;
    return matchesSearch && matchesStatus;
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    await new Promise(resolve => setTimeout(resolve, 500));
    if (editingJob) {
      setJobs(jobs.map(job => job.id === editingJob.id ? { ...formData, id: editingJob.id, logo: formData.company.slice(0, 2) } : job));
    } else {
      setJobs([...jobs, { ...formData, id: Date.now(), logo: formData.company.slice(0, 2) }]);
    }
    setIsModalOpen(false);
    setIsSubmitting(false);
    resetForm();
  };

  const handleDelete = (id) => {
    setJobs(jobs.filter(job => job.id !== id));
  };

  const handleEdit = (job) => {
    setEditingJob(job);
    setFormData(job);
    setIsModalOpen(true);
  };

  const resetForm = () => {
    setFormData({
      company: "",
      role: "",
      status: "Applied",
      date: new Date().toISOString().split('T')[0],
      salary: "",
      location: "",
      url: "",
      notes: "",
    });
    setEditingJob(null);
  };

  return (
    <div className="space-y-6">
      {/* HEADER */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold">💼 My Applications</h1>
          <p className="text-gray-400 mt-1">Track and manage all your job applications</p>
        </div>
        <RippleEffect>
          <button
            onClick={() => { resetForm(); setIsModalOpen(true); }}
            className="flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl hover:opacity-90 transition font-medium shadow-lg shadow-purple-500/25 active:scale-95"
          >
            <Plus size={20} />
            <span>Add Application</span>
          </button>
        </RippleEffect>
      </div>

      {/* FILTERS */}
      <div className="flex flex-col sm:flex-row gap-4">
        <div className="relative flex-1">
          <Search size={18} className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-500" />
          <input
            type="text"
            placeholder="Search company or role..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-12 pr-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 focus:bg-white/10 transition-all text-gray-200"
          />
        </div>
        <div className="flex gap-2 overflow-x-auto pb-2 sm:pb-0">
          {statuses.map(status => (
            <RippleEffect key={status}>
              <button
                onClick={() => setFilterStatus(status)}
                className={`px-4 py-2 rounded-xl whitespace-nowrap transition-all ${
                  filterStatus === status
                    ? "bg-gradient-to-r from-purple-500/20 to-pink-500/20 text-purple-300 border border-purple-500/30 shadow-md"
                    : "bg-white/5 text-gray-300 border border-white/10 hover:bg-white/10 hover:border-white/20"
                }`}
              >
                {status}
              </button>
            </RippleEffect>
          ))}
        </div>
      </div>

      {/* JOBS GRID */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
        <AnimatePresence mode="popLayout">
          {filteredJobs.map((job, i) => (
            <motion.div
              key={job.id}
              layout
              initial={{ opacity: 0, scale: 0.9, y: 20 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.9, y: -20 }}
              whileHover={{ y: -4, scale: 1.02 }}
              transition={{ delay: i * 0.05 }}
              className="p-5 rounded-2xl bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 transition-all group"
            >
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center gap-3">
                  <motion.div
                    whileHover={{ rotate: 5 }}
                    className="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center font-bold text-lg"
                  >
                    {job.logo}
                  </motion.div>
                  <div>
                    <h3 className="font-semibold text-lg">{job.company}</h3>
                    <p className="text-sm text-gray-400">{job.role}</p>
                  </div>
                </div>
                <div className="flex items-center gap-1">
                  <RippleEffect>
                    <button
                      onClick={() => handleEdit(job)}
                      className="p-2 hover:bg-white/10 rounded-lg opacity-0 group-hover:opacity-100 transition-all"
                    >
                      <Edit size={16} className="text-gray-400" />
                    </button>
                  </RippleEffect>
                  <RippleEffect>
                    <button
                      onClick={() => handleDelete(job.id)}
                      className="p-2 hover:bg-red-500/20 rounded-lg opacity-0 group-hover:opacity-100 transition-all"
                    >
                      <Trash2 size={16} className="text-red-400" />
                    </button>
                  </RippleEffect>
                </div>
              </div>

              <div className="space-y-2 mb-4">
                <div className="flex items-center gap-2 text-sm text-gray-400">
                  <Calendar size={14} />
                  <span>Applied: {new Date(job.date).toLocaleDateString()}</span>
                </div>
                {job.location && (
                  <div className="flex items-center gap-2 text-sm text-gray-400">
                    <MapPin size={14} />
                    <span>{job.location}</span>
                  </div>
                )}
                {job.salary && (
                  <div className="flex items-center gap-2 text-sm text-gray-400">
                    <DollarSign size={14} />
                    <span>{job.salary}</span>
                  </div>
                )}
              </div>

              {job.notes && (
                <p className="text-sm text-gray-500 mb-4 line-clamp-2">{job.notes}</p>
              )}

              <div className="flex items-center justify-between pt-4 border-t border-white/10">
                <StatusBadge status={job.status} />
                {job.url && (
                  <a
                    href={job.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center gap-1 text-sm text-purple-400 hover:text-purple-300 transition-all hover:gap-2"
                  >
                    <Link2 size={14} />
                    <span>View Job</span>
                  </a>
                )}
              </div>
            </motion.div>
          ))}
        </AnimatePresence>
      </div>

      {filteredJobs.length === 0 && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="flex flex-col items-center justify-center py-16 text-center"
        >
          <div className="w-20 h-20 rounded-2xl bg-white/5 flex items-center justify-center mb-4">
            <Search size={32} className="text-gray-500" />
          </div>
          <h3 className="text-lg font-medium text-gray-300 mb-1">No applications found</h3>
          <p className="text-gray-500">Try adjusting your filters or add a new application</p>
        </motion.div>
      )}

      {/* MODAL */}
      <AnimatePresence>
        {isModalOpen && (
          <>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setIsModalOpen(false)}
              className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50"
            />
            <motion.div
              initial={{ opacity: 0, y: 50, scale: 0.95 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: 50, scale: 0.95 }}
              className="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-lg z-50"
            >
              <div className="bg-gray-900/95 backdrop-blur-xl rounded-2xl border border-white/10 p-6 shadow-2xl">
                <div className="flex items-center justify-between mb-6">
                  <h2 className="text-xl font-bold">
                    {editingJob ? "Edit Application" : "Add New Application"}
                  </h2>
                  <RippleEffect>
                    <button
                      onClick={() => setIsModalOpen(false)}
                      className="p-2 hover:bg-white/10 rounded-lg transition-all"
                    >
                      <X size={20} />
                    </button>
                  </RippleEffect>
                </div>

                <form onSubmit={handleSubmit} className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-1">Company Name</label>
                    <input
                      required
                      type="text"
                      value={formData.company}
                      onChange={(e) => setFormData({ ...formData, company: e.target.value })}
                      className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 focus:bg-white/10 transition-all text-gray-200"
                      placeholder="e.g. Google"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-1">Role</label>
                    <input
                      required
                      type="text"
                      value={formData.role}
                      onChange={(e) => setFormData({ ...formData, role: e.target.value })}
                      className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 focus:bg-white/10 transition-all text-gray-200"
                      placeholder="e.g. Senior Frontend Developer"
                    />
                  </div>

                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-300 mb-1">Status</label>
                      <select
                        value={formData.status}
                        onChange={(e) => setFormData({ ...formData, status: e.target.value })}
                        className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 transition-all text-gray-200"
                      >
                        <option value="Applied">Applied</option>
                        <option value="Interview">Interview</option>
                        <option value="Offer">Offer</option>
                        <option value="Rejected">Rejected</option>
                      </select>
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-300 mb-1">Date Applied</label>
                      <input
                        type="date"
                        value={formData.date}
                        onChange={(e) => setFormData({ ...formData, date: e.target.value })}
                        className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 transition-all text-gray-200"
                      />
                    </div>
                  </div>

                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-300 mb-1">Salary Range</label>
                      <input
                        type="text"
                        value={formData.salary}
                        onChange={(e) => setFormData({ ...formData, salary: e.target.value })}
                        className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 transition-all text-gray-200"
                        placeholder="e.g. $150k - $180k"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-300 mb-1">Location</label>
                      <input
                        type="text"
                        value={formData.location}
                        onChange={(e) => setFormData({ ...formData, location: e.target.value })}
                        className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 transition-all text-gray-200"
                        placeholder="e.g. Remote"
                      />
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-1">Job URL</label>
                    <input
                      type="url"
                      value={formData.url}
                      onChange={(e) => setFormData({ ...formData, url: e.target.value })}
                      className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 transition-all text-gray-200"
                      placeholder="https://..."
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-1">Notes</label>
                    <textarea
                      value={formData.notes}
                      onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
                      rows={3}
                      className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:border-purple-400/50 resize-none transition-all text-gray-200"
                      placeholder="Add any notes about this application..."
                    />
                  </div>

                  <div className="flex gap-3 pt-4">
                    <RippleEffect>
                      <button
                        type="button"
                        onClick={() => setIsModalOpen(false)}
                        className="flex-1 px-4 py-3 bg-white/5 border border-white/10 rounded-xl hover:bg-white/10 transition-all font-medium"
                      >
                        Cancel
                      </button>
                    </RippleEffect>
                    <RippleEffect>
                      <button
                        type="submit"
                        disabled={isSubmitting}
                        className="flex-1 px-4 py-3 bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl hover:opacity-90 transition-all font-medium disabled:opacity-50"
                      >
                        {isSubmitting ? (
                          <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin mx-auto" />
                        ) : (
                          editingJob ? "Save Changes" : "Add Application"
                        )}
                      </button>
                    </RippleEffect>
                  </div>
                </form>
              </div>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </div>
  );
}

function StatusBadge({ status }) {
  const badges = {
    Applied: { bg: "bg-purple-500/20", text: "text-purple-300", border: "border-purple-500/30", icon: CheckCircle2 },
    Interview: { bg: "bg-blue-500/20", text: "text-blue-300", border: "border-blue-500/30", icon: Calendar },
    Offer: { bg: "bg-green-500/20", text: "text-green-300", border: "border-green-500/30", icon: CheckCircle2 },
    Rejected: { bg: "bg-red-500/20", text: "text-red-300", border: "border-red-500/30", icon: XCircle },
  };

  const badge = badges[status];
  const Icon = badge.icon;

  return (
    <span className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium border ${badge.bg} ${badge.text} ${badge.border}`}>
      <Icon size={12} />
      {status}
    </span>
  );
}
