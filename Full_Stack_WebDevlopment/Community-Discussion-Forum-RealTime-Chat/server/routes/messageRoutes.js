const express = require("express");

const router = express.Router();

const {
  getMessages,
  saveMessage,
} = require("../controllers/messageController");

router.get("/", getMessages);

router.post("/", saveMessage);

module.exports = router;