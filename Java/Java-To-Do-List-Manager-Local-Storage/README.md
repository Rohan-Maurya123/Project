# ✅ Smart To-Do List Manager

A modern desktop-based **Task Management Application** built using **Java Swing** that helps users organize daily activities, track progress, and manage tasks efficiently through a clean and user-friendly interface.

The application focuses on creating a simple yet powerful productivity tool where users can add, update, complete, search, and manage their tasks while keeping their data stored locally.

---

# 📌 Project Overview

Managing daily tasks manually can become difficult when multiple activities, deadlines, and priorities are involved. This application provides a structured way to organize tasks, monitor progress, and maintain productivity.

The project follows a layered architecture approach where the user interface, business logic, and data storage are separated for better maintainability and scalability.

---

# ✨ Features

## 📋 Task Management

- Create new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- View all available tasks


## 🎯 Task Organization

- Set task priority:
  - Low
  - Medium
  - High
  - Critical

- Categorize tasks:
  - Study
  - Work
  - Personal
  - Health
  - Shopping
  - Other


## 📊 Dashboard

A dedicated dashboard provides a quick overview of:

- Total tasks
- Completed tasks
- Pending tasks
- Overdue tasks


## 🔍 Search & Filtering

- Search tasks by title
- Filter tasks based on status
- Filter tasks based on priority


## 💾 Local Data Storage

- Task data is stored locally using Java Serialization
- Tasks remain available after restarting the application
- No external database setup required


## 🎨 Modern User Interface

- Dark-themed modern design
- Rounded cards and buttons
- Clean navigation
- User-friendly desktop experience

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Java | Core application development |
| Java Swing | Graphical User Interface |
| OOP Concepts | Application structure |
| File Handling | Local data persistence |
| Java Serialization | Task storage |
| VS Code | Development Environment |

---

# 🏗️ Project Architecture

```
Smart-ToDo-List-Manager

src
│
├── model
│   ├── Task.java
│   ├── TaskPriority.java
│   ├── TaskStatus.java
│   └── TaskCategory.java
│
├── service
│   └── TaskService.java
│
├── repository
│   └── FileTaskRepository.java
│
├── ui
│   ├── MainFrame.java
│   ├── DashboardPanel.java
│   ├── TaskManagementPanel.java
│   ├── TaskTableModel.java
│   ├── AddTaskDialog.java
│   └── EditTaskDialog.java
│
├── theme
│   ├── AppColors.java
│   ├── AppFonts.java
│   ├── RoundedButton.java
│   └── RoundedPanel.java
│
└── main
    └── Main.java
```

---

# ▶️ How to Run

## Requirements

- Java JDK 17 or above
- VS Code / IntelliJ IDEA

---

## Run Using Terminal

Compile the project:

```bash
javac -d target src/**/*.java
```

Run the application:

```bash
java -cp target main.Main
```

---

# 📸 Application Screenshots

(Add your screenshots here)

Example:

```
screenshots/

├── dashboard.png
├── task-list.png
├── add-task.png
└── edit-task.png
```

---

# 🧪 Testing

The application has been tested for:

✅ Adding tasks  
✅ Updating tasks  
✅ Deleting tasks  
✅ Completing tasks  
✅ Searching tasks  
✅ Filtering tasks  
✅ Saving and loading data after restart  

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Designing Java applications using OOP principles
- Creating desktop interfaces with Java Swing
- Managing application layers
- Implementing local storage systems
- Building user-focused software solutions
- Structuring projects professionally

---

# 🚀 Future Improvements

Possible enhancements:

- Database integration (MySQL/PostgreSQL)
- User authentication
- Cloud synchronization
- Task reminders and notifications
- Calendar integration
- Mobile version

---

# 🙌 Acknowledgement

Special thanks to my mentor **Umesh Yadav** for his valuable guidance, continuous support, and motivation throughout this learning journey.

His guidance helped me improve my development approach and build projects with better understanding and confidence.

---

# 👨‍💻 Developer

**Rohan Maurya**

Java Developer | Software Development Learner

---

⭐ If you find this project useful, feel free to explore and share your feedback.