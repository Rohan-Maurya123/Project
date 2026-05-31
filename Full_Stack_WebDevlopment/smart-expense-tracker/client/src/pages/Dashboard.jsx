import { useEffect, useState } from "react";
import Card from "../components/Card";
import ChartBar from "../components/ChartBar";
import { TransactionService } from "../services/transactionService";
import { calculateIncome, calculateExpense } from "../utils/helpers";

export default function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    setData(TransactionService.getAll());
  }, []);

  const income = calculateIncome(data);
  const expense = calculateExpense(data);
  const balance = income - expense;

  return (
    <div style={{ padding: "32px" }}>
      <h1
        style={{
          fontSize: "28px",
          fontWeight: "800",
          color: "#1e293b",
          marginBottom: "24px",
        }}
      >
        Dashboard Overview
      </h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))",
          gap: "24px",
          marginBottom: "32px",
        }}
      >
        <Card title="Total Income" value={income} icon="💵" color="success" />
        <Card title="Total Expense" value={expense} icon="💸" color="danger" />
        <Card title="Net Balance" value={balance} icon="💰" color="primary" />
      </div>

      <ChartBar income={income} expense={expense} />
    </div>
  );
}
