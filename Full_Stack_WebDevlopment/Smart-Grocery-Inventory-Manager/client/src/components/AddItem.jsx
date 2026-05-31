import { useState } from "react";
import API from "../services/api";

function AddItem({ refresh }) {
  const [form, setForm] = useState({
    name: "",
    category: "",
    quantity: "",
    unit: "",
    minStock: "",
    expiryDate: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await API.post("/items", form);
      refresh();
      setForm({
        name: "",
        category: "",
        quantity: "",
        unit: "",
        minStock: "",
        expiryDate: "",
      });
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white p-4 rounded shadow mb-6 grid grid-cols-2 gap-3"
    >
      <input
        name="name"
        placeholder="Name"
        value={form.name}
        onChange={handleChange}
        className="border p-2"
      />
      <input
        name="category"
        placeholder="Category"
        value={form.category}
        onChange={handleChange}
        className="border p-2"
      />
      <input
        name="quantity"
        placeholder="Quantity"
        value={form.quantity}
        onChange={handleChange}
        className="border p-2"
      />
      <input
        name="unit"
        placeholder="Unit"
        value={form.unit}
        onChange={handleChange}
        className="border p-2"
      />
      <input
        name="minStock"
        placeholder="Min Stock"
        value={form.minStock}
        onChange={handleChange}
        className="border p-2"
      />
      <input
        name="expiryDate"
        type="date"
        value={form.expiryDate}
        onChange={handleChange}
        className="border p-2"
      />

      <button className="col-span-2 bg-green-500 text-white py-2 rounded hover:bg-green-600">
        ➕ Add Item
      </button>
    </form>
  );
}

export default AddItem;
