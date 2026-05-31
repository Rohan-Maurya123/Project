const Course = require("../models/Course");

exports.getAllCourses = async (req, res) => {
  try {
    const { category, level, search } = req.query;
    
    if (global.inMemoryStorage?.useInMemory) {
      let courses = [...global.inMemoryStorage.courses];
      if (category && category !== "All") courses = courses.filter(c => c.category === category);
      if (level && level !== "All") courses = courses.filter(c => c.level === level);
      if (search) courses = courses.filter(c => c.title.toLowerCase().includes(search.toLowerCase()));
      res.json(courses);
    } else {
      let query = {};
      if (category && category !== "All") query.category = category;
      if (level && level !== "All") query.level = level;
      if (search) query.title = { $regex: search, $options: "i" };
      
      const courses = await Course.find(query);
      res.json(courses);
    }
  } catch (err) {
    res.status(500).json(err.message);
  }
};

exports.getCourseById = async (req, res) => {
  try {
    const { id } = req.params;
    
    if (global.inMemoryStorage?.useInMemory) {
      const course = global.inMemoryStorage.courses.find(c => c._id === id);
      res.json(course);
    } else {
      const course = await Course.findById(id);
      res.json(course);
    }
  } catch (err) {
    res.status(500).json(err.message);
  }
};

exports.createCourse = async (req, res) => {
  try {
    if (global.inMemoryStorage?.useInMemory) {
      const course = { _id: Date.now().toString(), ...req.body };
      global.inMemoryStorage.courses.push(course);
      res.json(course);
    } else {
      const course = await Course.create(req.body);
      res.json(course);
    }
  } catch (err) {
    res.status(500).json(err.message);
  }
};
