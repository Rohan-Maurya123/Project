const bcrypt = require("bcryptjs");

const readData = require("../utils/readData");
const writeData = require("../utils/writeData");

const generateId = require("../utils/generateId");
const generateToken = require("../utils/generateToken");

const {
  USERS_FILE,
} = require("../config/constants");

// REGISTER
const registerUser = async (req, res) => {
  try {
    const { name, email, password } = req.body;

    if (!name || !email || !password) {
      return res.status(400).json({
        success: false,
        message: "All fields are required",
      });
    }

    const users = readData(USERS_FILE);

    const existingUser = users.find(
      (user) => user.email === email
    );

    if (existingUser) {
      return res.status(400).json({
        success: false,
        message: "Email already exists",
      });
    }

    const hashedPassword =
      await bcrypt.hash(password, 10);

    const newUser = {
      id: generateId(),
      name,
      email,
      password: hashedPassword,
      createdAt: new Date(),
    };

    users.push(newUser);

    writeData(USERS_FILE, users);

    res.status(201).json({
      success: true,
      message: "User registered successfully",
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// LOGIN
const loginUser = async (req, res) => {
  try {
    const { email, password } = req.body;

    const users = readData(USERS_FILE);

    const user = users.find(
      (u) => u.email === email
    );

    if (!user) {
      return res.status(400).json({
        success: false,
        message: "User not found",
      });
    }

    const isMatch =
      await bcrypt.compare(
        password,
        user.password
      );

    if (!isMatch) {
      return res.status(400).json({
        success: false,
        message: "Invalid password",
      });
    }

    const token = generateToken(user.id);

    res.status(200).json({
      success: true,
      token,
      user: {
        id: user.id,
        name: user.name,
        email: user.email,
      },
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

module.exports = {
  registerUser,
  loginUser,
};