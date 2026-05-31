const GroceryItem = require("../models/GroceryItem");

// Create Item
const createItem = async (req, res) => {
  try {
    const {
      name,
      category,
      quantity,
      unit,
      minStock,
      expiryDate,
    } = req.body;

    const item = await GroceryItem.create({
      user: req.user._id,
      name,
      category,
      quantity,
      unit,
      minStock,
      expiryDate,
    });

    res.status(201).json(item);
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

// Get All Items
const getItems = async (req, res) => {
  try {
    const items = await GroceryItem.find({
      user: req.user._id,
    });

    res.status(200).json(items);
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

// Update Item
const updateItem = async (req, res) => {
  try {
    const item = await GroceryItem.findById(req.params.id);

    if (!item) {
      return res.status(404).json({
        message: "Item not found",
      });
    }

    const updatedItem = await GroceryItem.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );

    res.status(200).json(updatedItem);
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

// Delete Item
const deleteItem = async (req, res) => {
  try {
    const item = await GroceryItem.findById(req.params.id);

    if (!item) {
      return res.status(404).json({
        message: "Item not found",
      });
    }

    await item.deleteOne();

    res.status(200).json({
      message: "Item deleted successfully",
    });
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};


// Low Stock Items
const getLowStockItems = async (req, res) => {
  try {
    const items = await GroceryItem.find({
      user: req.user._id,
    });

    const lowStockItems = items.filter(
      (item) => item.quantity <= item.minStock
    );

    res.status(200).json(lowStockItems);
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

const getExpiryAlerts = async (req, res) => {
  try {
    const items = await GroceryItem.find({
      user: req.user._id,
    });

    const today = new Date();

    const next7Days = new Date();

    next7Days.setDate(today.getDate() + 7);

    const expiringItems = items.filter(
      (item) =>
        item.expiryDate &&
        item.expiryDate >= today &&
        item.expiryDate <= next7Days
    );

    res.status(200).json(expiringItems);
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

const getDashboardSummary = async (req, res) => {
  try {
    const items = await GroceryItem.find({
      user: req.user._id,
    });

    const totalItems = items.length;

    const lowStockItems = items.filter(
      (item) => item.quantity <= item.minStock
    );

    const today = new Date();
    const next7Days = new Date();
    next7Days.setDate(today.getDate() + 7);

    const expiringItems = items.filter(
      (item) =>
        item.expiryDate &&
        item.expiryDate >= today &&
        item.expiryDate <= next7Days
    );

    const categoryCount = {};

    items.forEach((item) => {
      categoryCount[item.category] =
        (categoryCount[item.category] || 0) + 1;
    });

    res.status(200).json({
      totalItems,
      lowStockCount: lowStockItems.length,
      expiringCount: expiringItems.length,
      categoryCount,
    });
  } catch (error) {
    res.status(500).json({
      message: error.message,
    });
  }
};

module.exports = {
  createItem,
  getItems,
  updateItem,
  deleteItem,
  getLowStockItems,
  getExpiryAlerts,
  getDashboardSummary,
};