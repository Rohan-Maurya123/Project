const db = require("../db/memoryDB");
const jwt = require("jsonwebtoken");
const { v4: uuid } = require("uuid");

const SECRET = "secretkey";

exports.register = (req, res) => {
  const { email, password } = req.body;

  const user = {
    id: uuid(),
    email,
    password,
  };

  db.users.push(user);

  res.json({ message: "User registered successfully" });
};

exports.login = (req, res) => {
  const { email, password } = req.body;

  const user = db.users.find(
    (u) => u.email === email && u.password === password
  );

  if (!user) return res.status(401).json({ message: "Invalid credentials" });

  const token = jwt.sign({ id: user.id }, SECRET, { expiresIn: "1d" });

  res.json({ token });
};