const express = require("express");
const router = express.Router();

const controller = require("../controllers/budgetController");

router.post("/", controller.setBudget);
router.get("/:userId", controller.getBudget);

module.exports = router;