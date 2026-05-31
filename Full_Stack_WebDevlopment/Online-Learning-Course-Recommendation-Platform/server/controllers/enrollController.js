const Enrollment = require("../models/Enrollment");
const Course = require("../models/Course");

exports.enrollCourse = async (req, res) => {
  try {
    const { userId, courseId } = req.body;
    
    if (global.inMemoryStorage?.useInMemory) {
      const existing = global.inMemoryStorage.enrollments.find(e => e.userId === userId && e.courseId === courseId);
      if (existing) return res.status(400).json("Already enrolled");
      
      const enrollment = { _id: Date.now().toString(), userId, courseId, progress: 0 };
      global.inMemoryStorage.enrollments.push(enrollment);
      res.json(enrollment);
    } else {
      const existing = await Enrollment.findOne({ userId, courseId });
      if (existing) return res.status(400).json("Already enrolled");
      
      const enrollment = await Enrollment.create({ userId, courseId });
      res.json(enrollment);
    }
  } catch (err) {
    res.status(500).json(err.message);
  }
};

exports.getEnrolledCourses = async (req, res) => {
  try {
    const { userId } = req.params;
    let enrollments, courses;
    
    if (global.inMemoryStorage?.useInMemory) {
      enrollments = global.inMemoryStorage.enrollments.filter(e => e.userId === userId);
      courses = enrollments.map(e => {
        const course = global.inMemoryStorage.courses.find(c => c._id === e.courseId);
        return course ? { ...course, progress: e.progress } : null;
      }).filter(Boolean);
    } else {
      enrollments = await Enrollment.find({ userId });
      const courseIds = enrollments.map(e => e.courseId);
      courses = await Course.find({ _id: { $in: courseIds } });
      
      courses = courses.map(course => {
        const enrollment = enrollments.find(e => e.courseId === course._id.toString());
        return { ...course._doc, progress: enrollment ? enrollment.progress : 0 };
      });
    }
    
    res.json(courses);
  } catch (err) {
    res.status(500).json(err.message);
  }
};

exports.updateProgress = async (req, res) => {
  try {
    const { userId, courseId, progress } = req.body;
    
    if (global.inMemoryStorage?.useInMemory) {
      let enrollment = global.inMemoryStorage.enrollments.find(e => e.userId === userId && e.courseId === courseId);
      if (enrollment) {
        enrollment.progress = progress;
      } else {
        enrollment = { _id: Date.now().toString(), userId, courseId, progress };
        global.inMemoryStorage.enrollments.push(enrollment);
      }
      res.json(enrollment);
    } else {
      const enrollment = await Enrollment.findOneAndUpdate(
        { userId, courseId },
        { progress },
        { new: true, upsert: true }
      );
      res.json(enrollment);
    }
  } catch (err) {
    res.status(500).json(err.message);
  }
};
