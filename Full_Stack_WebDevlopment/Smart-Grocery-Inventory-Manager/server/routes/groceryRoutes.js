const express = require("express");

const {
  createItem,
  getItems,
  updateItem,
  deleteItem,
  getLowStockItems,
  getExpiryAlerts,
  getDashboardSummary,
} = require("../controllers/groceryController");

const { protect } = require("../middleware/authMiddleware");

const router = express.Router();

router.route("/")
  .post(protect, createItem)
  .get(protect, getItems);

router.get(
  "/alerts/low-stock",
  protect,
  getLowStockItems
);

router.get(
  "/alerts/expiry",
  protect,
  getExpiryAlerts
);

router.get(
  "/dashboard",
  protect,
  getDashboardSummary
);

router.route("/:id")
  .put(protect, updateItem)
  .delete(protect, deleteItem);

module.exports = router;