const readData = require("../utils/readData");

const {
  NOTIFICATIONS_FILE,
} = require("../config/constants");

const getNotifications = (
  req,
  res
) => {
  const notifications =
    readData(
      NOTIFICATIONS_FILE
    );

  res.json({
    success: true,
    notifications,
  });
};

module.exports = {
  getNotifications,
};