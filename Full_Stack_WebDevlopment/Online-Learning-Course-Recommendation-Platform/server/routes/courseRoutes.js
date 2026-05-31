const express = require("express");
const router = express.Router();
const { getAllCourses, getCourseById, createCourse } = require("../controllers/courseController");

router.get("/", getAllCourses);
router.get("/:id", getCourseById);
router.post("/", createCourse);

module.exports = router;
