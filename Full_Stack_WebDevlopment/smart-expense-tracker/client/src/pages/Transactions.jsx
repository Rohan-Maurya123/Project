import { useState, useEffect } from "react";
import TransactionTable from "../components/TransactionTable";
import { TransactionService } from "../services/transactionService";

export default function Transactions() {
  const [data, setData] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newTransaction, setNewTransaction] = useState({
    type: "expense",
    amount: "",
    category: "",
  });

  useEffect(() => {
    setData(TransactionService.getAll());
  }, []);

  const handleAddTransaction = () => {
    if (!newTransaction.amount || !newTransaction.category) return;
    TransactionService.add(newTransaction);
    setData(TransactionService.getAll());
    setNewTransaction({
      type: "expense",
      amount: "",
      category: "",
    });
    setIsModalOpen(false);
  };

  const handleDelete = (id) => {
    TransactionService.delete(id);
    setData(TransactionService.getAll());
  };

  return (
    <div style={{ padding: "32px" }}>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: "24px",
        }}
      >
        <h1
          style={{
            fontSize: "28px",
            fontWeight: "800",
            color: "#1e293b",
          }}
        >
          Transactions
        </h1>
        <button className="btn btn-primary" onClick={() => setIsModalOpen(true)}>
          ➕ Add Transaction
        </button>
      </div>

      <TransactionTable data={data} onDelete={handleDelete} />

      {isModalOpen && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: "rgba(0, 0, 0, 0.75)",
            backdropFilter: "blur(8px)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            zIndex: 1000,
            padding: "20px",
          }}
          onClick={() => setIsModalOpen(false)}
        >
          <div
            className="card"
            style={{
              width: "100%",
              maxWidth: "520px",
              animation: "fadeIn 0.3s ease",
              borderRadius: "24px",
              overflow: "hidden",
              boxShadow: "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
              background: "#ffffff",
            }}
            onClick={(e) => e.stopPropagation()}
          >
            {/* Modal Header */}
            <div
              style={{
                background: "linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)",
                padding: "24px",
                textAlign: "center",
              }}
            >
              <div
                style={{
                  width: "64px",
                  height: "64px",
                  borderRadius: "16px",
                  background: "rgba(255, 255, 255, 0.2)",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: "32px",
                  margin: "0 auto 16px",
                }}
              >
                💸
              </div>
              <h2
                style={{
                  fontSize: "24px",
                  fontWeight: "800",
                  color: "white",
                  marginBottom: "4px",
                }}
              >
                New Transaction
              </h2>
              <p style={{ color: "rgba(255, 255, 255, 0.8)", fontSize: "14px" }}>
                Record your income or expense
              </p>
            </div>

            {/* Modal Body */}
            <div style={{ padding: "28px" }}>
              {/* Type Selection */}
              <div style={{ marginBottom: "24px" }}>
                <label
                  style={{
                    display: "block",
                    marginBottom: "12px",
                    fontWeight: "600",
                    color: "#374151",
                    fontSize: "14px",
                  }}
                >
                  Transaction Type
                </label>
                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "12px" }}>
                  <button
                    type="button"
                    onClick={() =>
                      setNewTransaction({ ...newTransaction, type: "income" })
                    }
                    style={{
                      padding: "16px",
                      borderRadius: "12px",
                      border:
                        newTransaction.type === "income"
                          ? "2px solid #10b981"
                          : "2px solid #e2e8f0",
                      background:
                        newTransaction.type === "income"
                          ? "rgba(16, 185, 129, 0.1)"
                          : "white",
                      color: newTransaction.type === "income" ? "#059669" : "#374151",
                      fontWeight: "700",
                      fontSize: "15px",
                      cursor: "pointer",
                      transition: "all 0.2s ease",
                      display: "flex",
                      flexDirection: "column",
                      gap: "8px",
                    }}
                    onMouseEnter={(e) => {
                      if (newTransaction.type !== "income") {
                        e.currentTarget.background = "#f8fafc";
                      }
                    }}
                    onMouseLeave={(e) => {
                      if (newTransaction.type !== "income") {
                        e.currentTarget.background = "white";
                      }
                    }}
                  >
                    <span style={{ fontSize: "24px" }}>💰</span>
                    Income
                  </button>
                  <button
                    type="button"
                    onClick={() =>
                      setNewTransaction({ ...newTransaction, type: "expense" })
                    }
                    style={{
                      padding: "16px",
                      borderRadius: "12px",
                      border:
                        newTransaction.type === "expense"
                          ? "2px solid #ef4444"
                          : "2px solid #e2e8f0",
                      background:
                        newTransaction.type === "expense"
                          ? "rgba(239, 68, 68, 0.1)"
                          : "white",
                      color: newTransaction.type === "expense" ? "#dc2626" : "#374151",
                      fontWeight: "700",
                      fontSize: "15px",
                      cursor: "pointer",
                      transition: "all 0.2s ease",
                      display: "flex",
                      flexDirection: "column",
                      gap: "8px",
                    }}
                  >
                    <span style={{ fontSize: "24px" }}>🛍️</span>
                    Expense
                  </button>
                </div>
              </div>

              {/* Amount Input */}
              <div style={{ marginBottom: "24px" }}>
                <label
                  style={{
                    display: "block",
                    marginBottom: "12px",
                    fontWeight: "600",
                    color: "#374151",
                    fontSize: "14px",
                  }}
                >
                  Amount
                </label>
                <div style={{ position: "relative" }}>
                  <span
                    style={{
                      position: "absolute",
                      left: "16px",
                      top: "50%",
                      transform: "translateY(-50%)",
                      fontSize: "18px",
                      fontWeight: "700",
                      color: "#64748b",
                    }}
                  >
                    $
                  </span>
                  <input
                    type="number"
                    className="input"
                    placeholder="0.00"
                    value={newTransaction.amount}
                    onChange={(e) =>
                      setNewTransaction({ ...newTransaction, amount: e.target.value })
                    }
                    style={{
                      paddingLeft: "44px",
                      fontSize: "18px",
                      fontWeight: "600",
                    }}
                  />
                </div>
              </div>

              {/* Category Input */}
              <div style={{ marginBottom: "28px" }}>
                <label
                  style={{
                    display: "block",
                    marginBottom: "12px",
                    fontWeight: "600",
                    color: "#374151",
                    fontSize: "14px",
                  }}
                >
                  Category
                </label>
                <input
                  type="text"
                  className="input"
                  placeholder="e.g., Food, Salary, Rent"
                  value={newTransaction.category}
                  onChange={(e) =>
                    setNewTransaction({ ...newTransaction, category: e.target.value })
                  }
                />
              </div>

              {/* Action Buttons */}
              <div style={{ display: "flex", gap: "12px" }}>
                <button
                  className="btn"
                  style={{
                    flex: 1,
                    padding: "14px",
                    background: "#f1f5f9",
                    color: "#374151",
                    fontWeight: "600",
                    borderRadius: "12px",
                  }}
                  onClick={() => setIsModalOpen(false)}
                >
                  Cancel
                </button>
                <button
                  className="btn btn-primary"
                  style={{
                    flex: 1,
                    padding: "14px",
                    borderRadius: "12px",
                    fontSize: "15px",
                  }}
                  onClick={handleAddTransaction}
                >
                  Add Transaction ✅
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
