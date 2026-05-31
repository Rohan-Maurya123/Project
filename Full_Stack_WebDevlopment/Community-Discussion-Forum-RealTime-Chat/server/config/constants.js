const path = require("path");

module.exports = {
  USERS_FILE: path.join(
    __dirname,
    "../data/users.json"
  ),

  DISCUSSIONS_FILE: path.join(
    __dirname,
    "../data/discussions.json"
  ),

  COMMENTS_FILE: path.join(
    __dirname,
    "../data/comments.json"
  ),

  MESSAGES_FILE: path.join(
    __dirname,
    "../data/messages.json"
  ),

  NOTIFICATIONS_FILE: path.join(
    __dirname,
    "../data/notifications.json"
  ),
};