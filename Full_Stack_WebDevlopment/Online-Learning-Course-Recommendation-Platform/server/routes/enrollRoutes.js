const express = require("express");
const router = express.Router();
const { enrollCourse, getEnrolledCourses, updateProgress } = require("../controllers/enrollController");

router.post("/", enrollCourse);
router.get("/:userId", getEnrolledCourses);
router.put("/progress", updateProgress);

module.exports = router;
