# 🛒 Smart Grocery Manager (Full Stack SaaS)

A full-stack inventory management system built using React, Node.js, Express, and MongoDB.  
It helps users manage grocery stock, track low inventory, and monitor expiry alerts with a modern dashboard UI.

---

## 🚀 Features

- 🔐 JWT Authentication (Login System)
- 📦 Inventory Management (Add / Update / Delete items)
- ⚠ Low Stock Alerts
- ⏳ Expiry Tracking System
- 📊 Dashboard Analytics (Total, Low Stock, Categories)
- 🔍 Search & Category Filter
- 📱 Responsive UI Design
- ⚡ Real-time UI updates after API actions

---

## 🏗 Tech Stack

**Frontend:**
- React (Vite)
- React Router DOM
- Tailwind CSS
- Axios

**Backend:**
- Node.js
- Express.js
- MongoDB (Mongoose)
- JWT Authentication
- CORS

---

## 📁 Project Structure

Smart-Grocery-Manager/
│
├── client/        (Frontend - React)
│   ├── src/
│   ├── pages/
│   ├── components/
│   ├── services/
│
├── server/        (Backend - Node + Express)
│   ├── models/
│   ├── routes/
│   ├── controllers/
│   ├── middleware/
│
└── README.md

---

## ⚙ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/your-username/smart-grocery-manager.git
cd smart-grocery-manager

2️⃣ Backend Setup
cd server
npm install


Create .env file in /server
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key

Run backend server
npm run dev

Backend runs at:http://localhost:5000



3️⃣ Frontend Setup

cd client
npm install
npm run dev

Frontend runs at:http://localhost:5173 



🧠 Future Improvements
🔔 Push notifications for alerts
📈 Advanced analytics dashboard
👥 Multi-user support
📱 Mobile app version
☁ Offline sync support

👨‍💻 Author : Rohan Maurya

⭐ Support
If you like this project:
⭐ Star the repository
🍴 Fork it
📢 Share it

MIT License

Copyright (c) 2026 Rohan Maurya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction...