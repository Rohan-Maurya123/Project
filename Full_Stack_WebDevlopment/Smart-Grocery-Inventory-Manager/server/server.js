const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");

const connectDB = require("./config/db");

const { protect } = require("./middleware/authMiddleware");

const authRoutes = require("./routes/authRoutes");

const User = require("./models/User");
const GroceryItem = require("./models/GroceryItem");
const groceryRoutes = require("./routes/groceryRoutes");

dotenv.config();

connectDB();

const app = express();

app.use(cors());
app.use(express.json());

app.use("/api/auth", authRoutes);

app.use("/api/items", groceryRoutes);

app.get("/", (req, res) => {
  res.send("Smart Grocery Inventory Manager API Running...");
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

app.get("/api/protected", protect, (req, res) => {
  res.json({
    message: "Protected Route Access Granted",
    user: req.user,
  });
});