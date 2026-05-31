# 💰 Smart Expense Tracker

A beautiful, modern, and intuitive expense management application to help you track your income, expenses, and budget effectively.

## ✨ Features

- **Dashboard Overview**: Get a quick glance at your total income, expenses, and net balance with interactive charts
- **Transactions Management**: Add, view, and delete income/expense transactions
- **Budget Planning**: Set monthly budgets and track your spending against them with progress bars
- **Analytics**: Visualize your expenses by category with beautiful pie charts
- **Responsive Design**: Works great on all devices
- **Local Storage**: Your data is saved locally in your browser
- **Beautiful UI**: Gradient colors, smooth animations, and modern design

## 🛠️ Tech Stack

### Frontend
- React 19
- Vite
- Chart.js (react-chartjs-2)
- React Router DOM
- Axios

### Backend
- Node.js
- Express.js
- CORS
- JSON Web Token (JWT)
- UUID

## 📦 Installation & Setup

### Prerequisites
- Node.js (v18 or later)
- npm (v9 or later)

### Step 1: Clone the repository
```bash
git clone <repository-url>
cd smart-expense-tracker
```

### Step 2: Install Backend Dependencies
```bash
cd server
npm install
```

### Step 3: Install Frontend Dependencies
```bash
cd ../client
npm install
```

## 🚀 Running the Application

### Start the Backend Server
Open a terminal and navigate to the `server` directory:
```bash
cd server
npm start
```
The server will start on http://localhost:5000

### Start the Frontend Development Server
Open another terminal and navigate to the `client` directory:
```bash
cd client
npm run dev
```
The app will open on http://localhost:5173 (or next available port)

## 📂 Project Structure

```
smart-expense-tracker/
├── client/             # Frontend React application
│   ├── src/
│   │   ├── components/  # Reusable UI components
│   │   ├── pages/      # Application pages
│   │   ├── services/   # API and storage services
│   │   └── utils/      # Helper functions
│   └── package.json
├── server/             # Backend Express application
│   ├── controllers/    # Request handlers
│   ├── routes/         # API routes
│   ├── db/             # In-memory database
│   └── server.js       # Entry point
└── README.md
```

## 🌟 Usage

1. **Get Started**: Click "Get Started" on the welcome page to enter the app
2. **Add Transactions**: Navigate to Transactions, click "Add Transaction" and fill in details
3. **Track Spending**: Check the Dashboard to see your income, expenses, and net balance
4. **Set Budget**: Go to Budget to set your monthly budget
5. **Analyze**: Visit Analytics to see your expenses by category


## 📝 License

This project is open source and available for educational purposes.
