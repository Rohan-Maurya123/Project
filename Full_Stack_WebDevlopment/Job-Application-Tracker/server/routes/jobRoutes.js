import express from "express";
import Job from "../models/Job.js";

const router = express.Router();

// CREATE
router.post("/", async (req, res) => {
  const job = await Job.create(req.body);
  res.json(job);
});

// GET ALL
router.get("/:userId", async (req, res) => {
  const jobs = await Job.find({ userId: req.params.userId });
  res.json(jobs);
});

// UPDATE
router.put("/:id", async (req, res) => {
  const job = await Job.findByIdAndUpdate(req.params.id, req.body);
  res.json(job);
});

// DELETE
router.delete("/:id", async (req, res) => {
  await Job.findByIdAndDelete(req.params.id);
  res.json({ message: "Deleted" });
});

export default router;