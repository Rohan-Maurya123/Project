const User = require("../models/User");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

const generateToken = (id) => {
  return jwt.sign({ id }, process.env.JWT_SECRET || "secretkey123", { expiresIn: "7d" });
};

exports.register = async (req, res) => {
  try {
    const { name, email, password, interests } = req.body;
    
    if (global.inMemoryStorage?.useInMemory) {
      const existing = global.inMemoryStorage.users.find(u => u.email === email);
      if (existing) return res.status(400).json("User already exists");
      
      const hashedPassword = await bcrypt.hash(password, 10);
      const user = {
        _id: Date.now().toString(),
        name,
        email,
        password: hashedPassword,
        interests: interests || []
      };
      global.inMemoryStorage.users.push(user);
      
      res.json({
        _id: user._id,
        name: user.name,
        token: generateToken(user._id),
      });
    } else {
      const hashedPassword = await bcrypt.hash(password, 10);
      const user = await User.create({
        name,
        email,
        password: hashedPassword,
        interests: interests || []
      });
      
      res.json({
        _id: user._id,
        name: user.name,
        token: generateToken(user._id),
      });
    }
  } catch (err) {
    res.status(500).json(err.message);
  }
};

exports.login = async (req, res) => {
  try {
    const { email, password } = req.body;
    
    let user;
    if (global.inMemoryStorage?.useInMemory) {
      user = global.inMemoryStorage.users.find(u => u.email === email);
    } else {
      user = await User.findOne({ email });
    }
    
    if (!user) return res.status(400).json("User not found");
    
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) return res.status(400).json("Invalid credentials");
    
    res.json({
      _id: user._id,
      name: user.name,
      token: generateToken(user._id),
    });
  } catch (err) {
    res.status(500).json(err.message);
  }
};
