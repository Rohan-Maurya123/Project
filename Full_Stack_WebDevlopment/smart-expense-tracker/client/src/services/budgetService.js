import { storage } from "./storage";

export const BudgetService = {
  set(amount) {
    const data = storage.get();
    data.budget = amount;
    storage.set(data);
  },

  get() {
    return storage.get().budget;
  },
};