const readData = require("../utils/readData");
const writeData = require("../utils/writeData");
const generateId = require("../utils/generateId");

const {
  DISCUSSIONS_FILE,
} = require("../config/constants");

// GET ALL DISCUSSIONS
const getDiscussions = (req, res) => {
  try {
    const discussions = readData(
      DISCUSSIONS_FILE
    );

    res.status(200).json({
      success: true,
      discussions,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// GET SINGLE DISCUSSION
const getDiscussionById = (
  req,
  res
) => {
  try {
    const discussions = readData(
      DISCUSSIONS_FILE
    );

    const discussion =
      discussions.find(
        (d) => d.id === req.params.id
      );

    if (!discussion) {
      return res.status(404).json({
        success: false,
        message:
          "Discussion not found",
      });
    }

    res.status(200).json({
      success: true,
      discussion,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// CREATE DISCUSSION
const createDiscussion = (
  req,
  res
) => {
  try {
    const {
      title,
      description,
      category,
      author,
    } = req.body;

    const discussions = readData(
      DISCUSSIONS_FILE
    );

    const newDiscussion = {
      id: generateId(),
      title,
      description,
      category,
      author,
      votes: 0,
      commentsCount: 0,
      createdAt:
        new Date().toISOString(),
    };

    discussions.unshift(
      newDiscussion
    );

    writeData(
      DISCUSSIONS_FILE,
      discussions
    );

    res.status(201).json({
      success: true,
      discussion: newDiscussion,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// DELETE DISCUSSION
const deleteDiscussion = (
  req,
  res
) => {
  try {
    const discussions = readData(
      DISCUSSIONS_FILE
    );

    const updated =
      discussions.filter(
        (d) => d.id !== req.params.id
      );

    writeData(
      DISCUSSIONS_FILE,
      updated
    );

    res.status(200).json({
      success: true,
      message:
        "Discussion deleted",
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

module.exports = {
  getDiscussions,
  getDiscussionById,
  createDiscussion,
  deleteDiscussion,
};