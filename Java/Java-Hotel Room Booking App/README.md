# 🏨 Hotel Room Booking Console App

A menu-driven Java console application that simulates the core workflow of a hotel booking system. The project allows users to search available rooms, create bookings, manage guest information, calculate bills, cancel bookings, and maintain booking records using file handling.

This project was built to strengthen Core Java, Object-Oriented Programming (OOP), Collections Framework, File Handling, Exception Handling, and real-world business logic.

---

## 📌 Project Overview

The Hotel Room Booking Console App is designed to simulate how hotels manage room reservations and guest bookings.

Users can:

- View available rooms
- Search rooms by type
- Book a room
- Enter guest details
- Generate unique booking IDs
- Calculate booking bills
- View booking details
- Cancel bookings
- Maintain booking history using text file storage

The project follows a modular architecture by separating models, business logic, utilities, and file management into different packages.

---

# ✨ Features

### ✅ Room Management

- View available rooms
- Search rooms by room type
- Different room categories
- Room availability tracking

### ✅ Booking Management

- Create new booking
- Generate unique Booking ID
- Booking confirmation
- View booking details
- Cancel booking

### ✅ Guest Management

- Guest information
- Contact number
- Email
- ID Proof

### ✅ Billing

- Automatic night calculation
- Price per night
- Total bill generation

### ✅ Validation

- Empty name validation
- Phone number validation
- Date validation

### ✅ File Handling

- Save booking records
- Read booking history
- Store data in text file

---

# 🛠️ Tech Stack

- Java
- Core Java
- Object-Oriented Programming (OOP)
- Java Collections (ArrayList)
- File Handling
- LocalDate API
- Exception Handling
- Scanner (Console Input)

---

# 📂 Project Structure

```
Hotel-Room-Booking-Console-App

│
├── src
│   ├── model
│   │   ├── Room.java
│   │   ├── Guest.java
│   │   └── Booking.java
│   │
│   ├── service
│   │   └── HotelService.java
│   │
│   ├── repository
│   │   └── FileManager.java
│   │
│   ├── utility
│   │   └── InputValidator.java
│   │
│   └── main
│       └── Main.java
│
├── data
│   └── bookings.txt
│
├── screenshots
│
└── README.md
```

---

# 📋 Console Menu

```
========== HOTEL BOOKING SYSTEM ==========

1. View Available Rooms
2. Search Room
3. Book Room
4. View Booking
5. Cancel Booking
6. Booking History
7. Exit
```

---

# 🧠 Java Concepts Used

- Classes & Objects
- Encapsulation
- Constructors
- Methods
- ArrayList
- Loops
- Conditional Statements
- Exception Handling
- File Handling
- LocalDate API
- Input Validation
- Modular Programming

---

# 💼 Business Logic

The application follows a real-world hotel booking workflow.

```
Start Application
        │
        ▼
Display Menu
        │
        ▼
Search Available Rooms
        │
        ▼
Select Room
        │
        ▼
Enter Guest Details
        │
        ▼
Validate Input
        │
        ▼
Create Booking
        │
        ▼
Calculate Bill
        │
        ▼
Generate Booking ID
        │
        ▼
Save Booking Record
        │
        ▼
Display Confirmation
```

---

# 📁 Booking Record Example

Bookings are stored in:

```
data/bookings.txt
```

Example:

```
BK1001,Rohan,9876543210,Deluxe,301,9000.0,CONFIRMED
```

---

# ▶️ How to Run

## Clone Repository

```bash
git clone <repository-url>
```

## Compile

```bash
javac -d out src/model/*.java src/service/*.java src/repository/*.java src/utility/*.java src/main/Main.java
```

## Run

```bash
java -cp out main.Main
```

---


# 🚀 Future Enhancements

- JDBC + MySQL Integration
- Admin Dashboard
- Customer Login
- Payment Gateway Simulation
- Discount Management
- Search by Date
- GUI using JavaFX
- Spring Boot REST API
- Cloud Database Integration

---

# 🎯 Learning Outcomes

This project helped me gain practical experience with:

- Object-Oriented Programming
- Designing modular Java applications
- File Handling
- Console-based application development
- Business logic implementation
- Input validation
- Real-world booking workflow simulation

---

# 👨‍💻 Author

**Rohan Maurya**

If you found this project helpful, feel free to ⭐ the repository and share your feedback.