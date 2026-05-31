const Course = require("../models/Course");
const Enrollment = require("../models/Enrollment");
const User = require("../models/User");

exports.getRecommendations = async (req, res) => {
  try {
    const { userId } = req.params;
    let recommendations = [];
    let enrolledIds = [];
    let userInterests = [];
    
    if (global.inMemoryStorage?.useInMemory) {
      const enrollments = global.inMemoryStorage.enrollments.filter(e => e.userId === userId);
      enrolledIds = enrollments.map(e => e.courseId);
      const user = global.inMemoryStorage.users.find(u => u._id === userId);
      userInterests = user?.interests || [];
      
      if (userInterests.length > 0) {
        recommendations = global.inMemoryStorage.courses.filter(c => 
          !enrolledIds.includes(c._id) && 
          (userInterests.includes(c.category) || c.tags?.some(t => userInterests.includes(t)))
        );
      }
      
      if (recommendations.length === 0) {
        recommendations = global.inMemoryStorage.courses.filter(c => !enrolledIds.includes(c._id)).slice(0, 10);
      }
    } else {
      const user = await User.findById(userId);
      const enrollments = await Enrollment.find({ userId });
      enrolledIds = enrollments.map(e => e.courseId);
      userInterests = user?.interests || [];
      
      if (userInterests.length > 0) {
        recommendations = await Course.find({
          _id: { $nin: enrolledIds },
          $or: [
            { category: { $in: userInterests } },
            { tags: { $in: userInterests } }
          ]
        });
      }
      
      if (recommendations.length === 0) {
        recommendations = await Course.find({ _id: { $nin: enrolledIds } }).limit(10);
      }
    }
    
    res.json(recommendations);
  } catch (err) {
    res.status(500).json(err.message);
  }
};
