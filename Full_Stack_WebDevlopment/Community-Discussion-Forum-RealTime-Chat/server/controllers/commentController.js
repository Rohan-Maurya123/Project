const readData = require("../utils/readData");
const writeData = require("../utils/writeData");
const generateId = require("../utils/generateId");

const {
  COMMENTS_FILE,
} = require("../config/constants");

const getComments = (
  req,
  res
) => {
  const comments = readData(
    COMMENTS_FILE
  );

  res.json({
    success: true,
    comments,
  });
};

const addComment = (
  req,
  res
) => {
  const comments = readData(
    COMMENTS_FILE
  );

  const newComment = {
    id: generateId(),
    discussionId:
      req.body.discussionId,
    user: req.body.user,
    comment:
      req.body.comment,
    createdAt:
      new Date().toISOString(),
  };

  comments.push(newComment);

  writeData(
    COMMENTS_FILE,
    comments
  );

  res.status(201).json({
    success: true,
    comment: newComment,
  });
};

module.exports = {
  getComments,
  addComment,
};