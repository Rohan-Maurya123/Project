import mongoose from "mongoose";

const jobSchema = new mongoose.Schema({
  title: String,
  company: String,
  status: {
    type: String,
    default: "Applied"
  },
  date: String,
  notes: String,
  userId: String
});

export default mongoose.model("Job", jobSchema);