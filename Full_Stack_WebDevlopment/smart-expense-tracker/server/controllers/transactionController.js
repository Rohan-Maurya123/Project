const db = require("../db/memoryDB");
const { v4: uuid } = require("uuid");

exports.getAll = (req, res) => {
  res.json(db.transactions);
};

exports.add = (req, res) => {
  const { type, amount, category, note } = req.body;

  const transaction = {
    id: uuid(),
    type, // income or expense
    amount,
    category,
    note,
    date: new Date(),
  };

  db.transactions.push(transaction);

  res.json(transaction);
};

exports.remove = (req, res) => {
  const { id } = req.params;

  db.transactions = db.transactions.filter((t) => t.id !== id);

  res.json({ message: "Deleted" });
};