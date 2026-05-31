const mongoose = require("mongoose");

const groceryItemSchema = new mongoose.Schema(
  {
    user: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },

    name: {
      type: String,
      required: true,
      trim: true,
    },

    category: {
      type: String,
      required: true,
      trim: true,
    },

    quantity: {
      type: Number,
      required: true,
      default: 0,
    },

    unit: {
      type: String,
      required: true,
    },

    minStock: {
      type: Number,
      required: true,
      default: 1,
    },

    expiryDate: {
      type: Date,
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("GroceryItem", groceryItemSchema);