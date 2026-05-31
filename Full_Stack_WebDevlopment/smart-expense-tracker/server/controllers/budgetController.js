const db = require("../db/memoryDB");

exports.setBudget = (req, res) => {
  const { userId, amount } = req.body;

  db.budgets[userId] = amount;

  res.json({ message: "Budget set", amount });
};

exports.getBudget = (req, res) => {
  const { userId } = req.params;

  res.json({ budget: db.budgets[userId] || 0 });
};