const KEY = "expense_data";

export const storage = {
  get() {
    return JSON.parse(localStorage.getItem(KEY)) || {
      transactions: [],
      budget: 0,
    };
  },

  set(data) {
    localStorage.setItem(KEY, JSON.stringify(data));
  },
};