import { storage } from "./storage";

export const TransactionService = {
  getAll() {
    return storage.get().transactions;
  },

  add(transaction) {
    const data = storage.get();
    data.transactions.push({ id: Date.now(), ...transaction });
    storage.set(data);
  },

  delete(id) {
    const data = storage.get();
    data.transactions = data.transactions.filter(t => t.id !== id);
    storage.set(data);
  },
};