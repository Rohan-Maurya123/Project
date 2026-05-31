const mongoose = require("mongoose");

const enrollSchema = new mongoose.Schema({
  userId: String,
  courseId: String,
  progress: { type: Number, default: 0 },
});

module.exports = mongoose.model("Enrollment", enrollSchema);