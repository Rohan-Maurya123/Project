const express = require("express");
const cors = require("cors");
const bcrypt = require("bcryptjs");
const dotenv = require("dotenv");
const connectDB = require("./config/db");
const authRoutes = require("./routes/authRoutes");
const courseRoutes = require("./routes/courseRoutes");
const enrollRoutes = require("./routes/enrollRoutes");
const recommendRoutes = require("./routes/recommendRoutes");
const Course = require("./models/Course");

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json());

// In-memory storage fallback if MongoDB not available
let inMemoryCourses = [
  { _id: "1", title: "Complete Web Development Bootcamp", category: "Programming", level: "Beginner", tags: ["javascript", "html", "css", "react"] },
  { _id: "2", title: "Advanced React Patterns", category: "Programming", level: "Advanced", tags: ["react", "javascript", "frontend"] },
  { _id: "3", title: "Python for Data Science", category: "Data Science", level: "Intermediate", tags: ["python", "data", "machine learning"] },
  { _id: "4", title: "Machine Learning A-Z", category: "Data Science", level: "Beginner", tags: ["machine learning", "python", "ai"] },
  { _id: "5", title: "UI/UX Design Fundamentals", category: "Design", level: "Beginner", tags: ["design", "ui", "ux", "figma"] },
  { _id: "6", title: "Figma Masterclass", category: "Design", level: "Intermediate", tags: ["figma", "design", "prototyping"] },
  { _id: "7", title: "Digital Marketing 101", category: "Marketing", level: "Beginner", tags: ["marketing", "seo", "social media"] },
  { _id: "8", title: "SEO & Content Marketing", category: "Marketing", level: "Intermediate", tags: ["seo", "content", "marketing"] },
  { _id: "9", title: "Mobile App Development with React Native", category: "Programming", level: "Intermediate", tags: ["react native", "mobile", "javascript"] },
  { _id: "10", title: "AWS Cloud Practitioner", category: "Cloud", level: "Beginner", tags: ["aws", "cloud", "devops"] },
];
let inMemoryUsers = [];
let inMemoryEnrollments = [];
let useInMemory = false;

app.use("/api/auth", authRoutes);
app.use("/api/courses", courseRoutes);
app.use("/api/enroll", enrollRoutes);
app.use("/api/recommend", recommendRoutes);

// Override models with in-memory if needed
const originalFind = Course.find;
const originalFindById = Course.findById;
const originalCreate = Course.create;
const originalCountDocuments = Course.countDocuments;

const init = async () => {
  try {
    await connectDB();
    
    // Seed sample courses if none exist
    const count = await Course.countDocuments();
    if (count === 0) {
      await Course.insertMany(inMemoryCourses.map(({_id, ...c}) => c));
      console.log("Sample courses seeded ✅");
    }
  } catch (err) {
    console.log("MongoDB not available, using in-memory storage 💾");
    useInMemory = true;
    
    // Pre-add test user
    const hashedPassword = await bcrypt.hash("123456", 10);
    inMemoryUsers.push({
      _id: "1",
      name: "Rohan",
      email: "rohan@gmail.com",
      password: hashedPassword,
      interests: ["Programming", "Data Science"]
    });
    
    // Override Course model methods
    Course.find = function(query = {}) {
      let filtered = [...inMemoryCourses];
      if (query.category) filtered = filtered.filter(c => c.category === query.category);
      if (query.level) filtered = filtered.filter(c => c.level === query.level);
      if (query.title && query.title.$regex) {
        const regex = new RegExp(query.title.$regex, query.title.$options);
        filtered = filtered.filter(c => regex.test(c.title));
      }
      return { exec: () => Promise.resolve(filtered) };
    };
    Course.findById = function(id) {
      return { exec: () => Promise.resolve(inMemoryCourses.find(c => c._id === id)) };
    };
    Course.countDocuments = function() {
      return { exec: () => Promise.resolve(inMemoryCourses.length) };
    };
  }
};

init();

app.get("/", (req, res) => {
  res.send(`Backend is running 🚀 (Using ${useInMemory ? "in-memory storage" : "MongoDB"}) - Test user: rohan@gmail.com / 123456`);
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Expose in-memory storage for controllers
global.inMemoryStorage = {
  courses: inMemoryCourses,
  users: inMemoryUsers,
  enrollments: inMemoryEnrollments,
  useInMemory
};
