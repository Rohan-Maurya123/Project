import React from "react";

const Enrolled = () => {
  const enrolledCourses = [
    {
      id: 1,
      title: "Advanced React & Redux",
      instructor: "Sarah Johnson",
      progress: 72,
      completedLessons: 34,
      totalLessons: 48,
      duration: "12 Hours",
      image:
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200",
      nextLesson: "Redux Toolkit Fundamentals",
    },
    {
      id: 2,
      title: "Node.js Backend Masterclass",
      instructor: "Michael Brown",
      progress: 45,
      completedLessons: 27,
      totalLessons: 60,
      duration: "15 Hours",
      image: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200",
      nextLesson: "Authentication & JWT",
    },
    {
      id: 3,
      title: "Generative AI with OpenAI",
      instructor: "Emily Wilson",
      progress: 88,
      completedLessons: 37,
      totalLessons: 42,
      duration: "10 Hours",
      image:
        "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200",
      nextLesson: "Building AI Applications",
    },
  ];

  const totalCourses = enrolledCourses.length;

  const avgProgress = Math.round(
    enrolledCourses.reduce((acc, item) => acc + item.progress, 0) /
      enrolledCourses.length,
  );

  return (
    <div className="max-w-7xl mx-auto px-6 py-8">
      {/* Header */}
      <div className="mb-10">
        <h1 className="text-5xl font-extrabold bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent mb-3">
          My Learning
          
        </h1>

        <p className="text-slate-400 text-lg">
          Continue your learning journey and track your progress.
        </p>
      </div>

      {/* Stats Cards */}
      <div className="grid md:grid-cols-3 gap-6 mb-12">
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <h3 className="text-slate-400 mb-2">Enrolled Courses</h3>
          <p className="text-4xl font-bold text-white">{totalCourses}</p>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <h3 className="text-slate-400 mb-2">Average Progress</h3>
          <p className="text-4xl font-bold text-green-400">{avgProgress}%</p>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <h3 className="text-slate-400 mb-2">Learning Hours</h3>
          <p className="text-4xl font-bold text-indigo-400">37h</p>
        </div>
      </div>

      {/* Courses Grid */}
      <div className="grid lg:grid-cols-2 gap-8">
        {enrolledCourses.map((course) => (
          <div
            key={course.id}
            className="bg-slate-900 border border-slate-800 rounded-3xl overflow-hidden shadow-xl hover:shadow-indigo-500/20 hover:-translate-y-2 transition-all duration-300"
          >
            <img
              src={course.image}
              alt={course.title}
              className="w-full h-56 object-cover"
            />

            <div className="p-6">
              <h2 className="text-2xl font-bold text-white mb-2">
                {course.title}
              </h2>

              <p className="text-slate-400 mb-4">
                Instructor: {course.instructor}
              </p>

              <div className="flex justify-between text-sm text-slate-400 mb-4">
                <span>
                  📚 {course.completedLessons}/{course.totalLessons} Lessons
                </span>

                <span>⏱ {course.duration}</span>
              </div>

              <div className="mb-4">
                <div className="flex justify-between mb-2 text-sm">
                  <span className="text-slate-300">Progress</span>

                  <span className="text-indigo-400 font-semibold">
                    {course.progress}%
                  </span>
                </div>

                <div className="w-full bg-slate-700 rounded-full h-3">
                  <div
                    className="bg-gradient-to-r from-indigo-500 to-purple-500 h-3 rounded-full"
                    style={{
                      width: `${course.progress}%`,
                    }}
                  />
                </div>
              </div>

              <div className="bg-indigo-500/10 border border-indigo-500/20 rounded-xl p-4 mb-5">
                <p className="text-indigo-300 text-sm">▶ Next Lesson:</p>

                <p className="text-white font-medium mt-1">
                  {course.nextLesson}
                </p>
              </div>

              <div className="flex gap-3">
                <button className="flex-1 py-3 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-semibold hover:opacity-90 transition">
                  Continue Learning
                </button>

                <button className="px-5 py-3 rounded-xl border border-slate-700 text-slate-300 hover:bg-slate-800 transition">
                  Details
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Achievement Section */}
      <div className="mt-14 bg-slate-900 border border-slate-800 rounded-3xl p-8">
        <h2 className="text-3xl font-bold text-white mb-6">
          🏆 Learning Achievements
        </h2>

        <div className="grid md:grid-cols-3 gap-6">
          <div className="bg-slate-800 rounded-2xl p-5">
            <div className="text-5xl mb-3">🎯</div>
            <h3 className="text-white font-bold mb-2">Consistent Learner</h3>
            <p className="text-slate-400 text-sm">
              Studied for 15 consecutive days.
            </p>
          </div>

          <div className="bg-slate-800 rounded-2xl p-5">
            <div className="text-5xl mb-3">🚀</div>
            <h3 className="text-white font-bold mb-2">Fast Progress</h3>
            <p className="text-slate-400 text-sm">
              Completed 80% of AI course.
            </p>
          </div>

          <div className="bg-slate-800 rounded-2xl p-5">
            <div className="text-5xl mb-3">🏅</div>
            <h3 className="text-white font-bold mb-2">Top Performer</h3>
            <p className="text-slate-400 text-sm">
              Among top learners this month.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Enrolled;
