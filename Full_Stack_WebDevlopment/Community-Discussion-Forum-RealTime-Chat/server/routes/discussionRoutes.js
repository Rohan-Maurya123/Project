const express = require("express");

const router = express.Router();

const {
  getDiscussions,
  getDiscussionById,
  createDiscussion,
  deleteDiscussion,
} = require("../controllers/discussionController");

router.get("/", getDiscussions);

router.get("/:id", getDiscussionById);

router.post("/", createDiscussion);

router.delete(
  "/:id",
  deleteDiscussion
);

module.exports = router;