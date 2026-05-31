export const calculateIncome = (data) =>
  data.filter(t => t.type === "income")
      .reduce((a, b) => a + Number(b.amount), 0);

export const calculateExpense = (data) =>
  data.filter(t => t.type === "expense")
      .reduce((a, b) => a + Number(b.amount), 0);