require("dotenv").config();

const express = require("express");
const cors = require("cors");
const http = require("http");

const authRoutes = require("./routes/authRoutes");
const discussionRoutes = require("./routes/discussionRoutes");
const commentRoutes = require("./routes/commentRoutes");
const messageRoutes = require("./routes/messageRoutes");
const notificationRoutes = require("./routes/notificationRoutes");

const setupSocket =
  require("./sockets/chatSocket");

const app = express();

const server =
  http.createServer(app);

app.use(cors());

app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    message: "Community Forum API Running",
  });
});

app.use("/api/auth", authRoutes);

app.use(
  "/api/discussions",
  discussionRoutes
);

app.use(
  "/api/comments",
  commentRoutes
);

app.use(
  "/api/messages",
  messageRoutes
);

app.use(
  "/api/notifications",
  notificationRoutes
);

setupSocket(server);

const PORT =
  process.env.PORT || 5000;

server.listen(PORT, () => {
  console.log(
    `Server running on port ${PORT}`
  );
});