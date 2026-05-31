const readData = require("../utils/readData");
const writeData = require("../utils/writeData");
const generateId = require("../utils/generateId");

const {
  MESSAGES_FILE,
} = require("../config/constants");

const getMessages = (
  req,
  res
) => {
  const messages = readData(
    MESSAGES_FILE
  );

  res.json({
    success: true,
    messages,
  });
};

const saveMessage = (
  req,
  res
) => {
  const messages = readData(
    MESSAGES_FILE
  );

  const newMessage = {
    id: generateId(),
    room: req.body.room,
    sender:
      req.body.sender,
    message:
      req.body.message,
    createdAt:
      new Date().toISOString(),
  };

  messages.push(newMessage);

  writeData(
    MESSAGES_FILE,
    messages
  );

  res.status(201).json({
    success: true,
    message: newMessage,
  });
};

module.exports = {
  getMessages,
  saveMessage,
};