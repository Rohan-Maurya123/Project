import React from "react";

const Recommendations = () => {
  const basedOnSkills = [
    {
      id: 1,
      title: "Advanced React & Redux",
      category: "Web Development",
      instructor: "Sarah Johnson",
      instructorImage: "https://randomuser.me/api/portraits/women/44.jpg",
      rating: 4.8,
      students: 12450,
      reviews: 3240,
      duration: "12 Hours",
      lessons: 48,
      level: "Intermediate",
      progress: 65,
      image:
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200",
      reason: "Because you completed React Basics",
    },
    {
      id: 2,
      title: "Node.js Backend Masterclass",
      category: "Backend Development",
      instructor: "Michael Brown",
      instructorImage: "https://randomuser.me/api/portraits/men/32.jpg",
      rating: 4.7,
      students: 9870,
      reviews: 2800,
      duration: "15 Hours",
      lessons: 60,
      level: "Advanced",
      progress: 40,
      image: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200",
      reason: "Matches your JavaScript skills",
    },
  ];

  const trendingCourses = [
    {
      id: 3,
      title: "Generative AI with OpenAI",
      category: "Artificial Intelligence",
      instructor: "Emily Wilson",
      instructorImage: "https://randomuser.me/api/portraits/women/68.jpg",
      rating: 4.9,
      students: 24500,
      reviews: 7200,
      duration: "10 Hours",
      lessons: 42,
      level: "Beginner",
      progress: 20,
      image:
        "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200",
    },
    {
      id: 4,
      title: "Cyber Security Essentials",
      category: "Security",
      instructor: "James Carter",
      instructorImage: "https://randomuser.me/api/portraits/men/52.jpg",
      rating: 4.6,
      students: 11200,
      reviews: 2200,
      duration: "8 Hours",
      lessons: 30,
      level: "Beginner",
      progress: 10,
      image:
        "https://images.unsplash.com/photo-1510511459019-5dda7724fd87?w=1200",
    },
  ];

  const skillGapCourses = [
    {
      id: 5,
      title: "System Design Fundamentals",
      category: "Software Engineering",
      instructor: "David Miller",
      instructorImage: "https://randomuser.me/api/portraits/men/41.jpg",
      rating: 4.8,
      students: 15400,
      reviews: 4500,
      duration: "14 Hours",
      lessons: 55,
      level: "Intermediate",
      progress: 0,
      image:
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200",
      reason: "Recommended to strengthen backend architecture skills",
    },
    {
      id: 6,
      title: "Data Structures & Algorithms",
      category: "Computer Science",
      instructor: "Sophia Adams",
      instructorImage: "https://randomuser.me/api/portraits/women/24.jpg",
      rating: 4.9,
      students: 32600,
      reviews: 9200,
      duration: "20 Hours",
      lessons: 95,
      level: "Advanced",
      progress: 0,
      image: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200",
      reason: "Frequently required for software engineering interviews",
    },
  ];

  const CourseCard = ({ course }) => {
    return (
      <div className="bg-slate-900 rounded-3xl overflow-hidden border border-slate-800 shadow-xl hover:shadow-indigo-500/20 hover:-translate-y-2 transition-all duration-300">
        <img
          src={course.image}
          alt={course.title}
          className="w-full h-52 object-cover"
        />

        <div className="p-5">
          <div className="flex items-center justify-between mb-3">
            <span className="bg-indigo-600/20 text-indigo-400 text-xs px-3 py-1 rounded-full">
              {course.category}
            </span>

            <span className="bg-green-500/20 text-green-400 text-xs px-3 py-1 rounded-full">
              {course.level}
            </span>
          </div>

          <h3 className="text-xl font-bold text-white mb-2">{course.title}</h3>

          <div className="flex items-center gap-3 mb-4">
            <img
              src={course.instructorImage}
              alt={course.instructor}
              className="w-10 h-10 rounded-full object-cover"
            />

            <div>
              <p className="text-white text-sm font-medium">
                {course.instructor}
              </p>
              <p className="text-slate-400 text-xs">Instructor</p>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3 mb-4 text-sm">
            <div className="text-slate-300">⭐ {course.rating}</div>

            <div className="text-slate-300">
              👥 {course.students.toLocaleString()}
            </div>

            <div className="text-slate-300">📚 {course.lessons} Lessons</div>

            <div className="text-slate-300">⏱ {course.duration}</div>
          </div>

          {course.reason && (
            <div className="bg-indigo-500/10 border border-indigo-500/20 rounded-xl p-3 mb-4">
              <p className="text-indigo-300 text-sm">🎯 {course.reason}</p>
            </div>
          )}

          <div className="mb-4">
            <div className="flex justify-between text-xs text-slate-400 mb-2">
              <span>Learning Progress</span>
              <span>{course.progress}%</span>
            </div>

            <div className="w-full bg-slate-700 rounded-full h-2">
              <div
                className="bg-gradient-to-r from-indigo-500 to-purple-500 h-2 rounded-full"
                style={{ width: `${course.progress}%` }}
              ></div>
            </div>
          </div>

          <button className="w-full py-3 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-semibold hover:opacity-90 transition">
            View Course
          </button>
        </div>
      </div>
    );
  };

  const Section = ({ title, courses }) => (
    <div className="mb-14">
      <h2 className="text-3xl font-bold text-white mb-6">{title}</h2>

      <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-8">
        {courses.map((course) => (
          <CourseCard key={course.id} course={course} />
        ))}
      </div>
    </div>
  );

  return (
    <div className="max-w-7xl mx-auto px-6 py-8">
      <div className="mb-12">
        <h1 className="text-5xl font-extrabold bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent mb-4">
          Recommended For You
        </h1>

        <p className="text-slate-400 text-lg">
          Personalized learning recommendations based on your interests, skills,
          and learning activity.
        </p>
      </div>

      <Section title="🎯 Based On Your Skills" courses={basedOnSkills} />

      <Section title="🔥 Trending Courses" courses={trendingCourses} />

      <Section title="📈 Skill Gap Recommendations" courses={skillGapCourses} />
    </div>
  );
};

export default Recommendations;
