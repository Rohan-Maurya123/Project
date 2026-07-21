# Online Complaint Management System using Java

A Java-based Complaint Management System designed to manage user complaints digitally through a structured workflow. The application allows users to register complaints, track their progress, and provide feedback, while administrators can review, assign, update, resolve, and close complaints.

This project demonstrates Java Object-Oriented Programming, file handling, role-based access, validation, and service-based application design.

---

# Project Overview

In many organizations, complaints are handled manually through emails, registers, or disconnected communication channels. This creates problems such as delayed responses, poor tracking, and lack of accountability.

The Online Complaint Management System provides a simple ticket-based approach where every complaint receives a unique Complaint ID and moves through different stages until resolution.

The system can be adapted for:

- Customer support systems
- College help desks
- Housing societies
- IT service desks
- Employee support portals
- Government grievance systems

---

# Features

## User Features

- User registration
- Secure login system
- Submit complaints
- Automatic complaint ID generation
- Select complaint category
- Select complaint priority
- View submitted complaints
- Track complaint status
- Submit feedback after resolution


## Admin Features

- Admin login
- View all complaints
- Search complaints by ID
- Assign complaints
- Update complaint status
- Change complaint priority
- Add resolution notes
- Close complaints


## Complaint Workflow

```
Complaint Created

        ↓

OPEN

        ↓

ASSIGNED

        ↓

IN_PROGRESS

        ↓

RESOLVED

        ↓

CLOSED

        ↓

USER FEEDBACK
```

---

# Technology Stack

## Programming Language

- Java


## Concepts Used

- Object-Oriented Programming
- Classes and Objects
- Encapsulation
- Enums
- Collections
- Exception Handling
- File Handling
- Input Validation
- Role Based Access Control


## Storage

File-based persistence:

```
data/
│
├── users.txt
├── complaints.txt
└── feedback.txt
```

---

# Project Architecture

```
Online Complaint Management System

                Main.java

                    |

                    |

              Service Layer

                    |

                    |

            Repository Layer

                    |

                    |

              File Storage
```


## Package Structure

```
src/

├── model
│
├── service
│
├── repository
│
├── utility
│
├── exception
│
├── constants
│
└── main
```

---

# Complaint Categories

The system supports:

- Technical
- Billing
- Service
- Product
- Infrastructure
- Other


# Complaint Priority

Available priorities:

- Low
- Medium
- High
- Critical


# Complaint Status

Available statuses:

- Open
- Assigned
- In Progress
- Resolved
- Closed
- Rejected


---

# How To Run

## Requirements

- Java JDK 17 or above
- VS Code / IntelliJ IDEA / Eclipse


---

# Running Using Command Line

Navigate to project folder:

```bash
cd Online-Complaint-Management-System-Java
```

Compile:

```bash
javac -d out src/**/*.java
```

Run:

```bash
java -cp out main.Main
```

---

# Sample User Flow

```
Register User

      ↓

Login

      ↓

Submit Complaint

      ↓

Receive Complaint ID

      ↓

Track Status

      ↓

Give Feedback
```

---

# Sample Admin Flow

```
Admin Login

      ↓

View Complaints

      ↓

Assign Complaint

      ↓

Update Status

      ↓

Add Resolution

      ↓

Close Complaint
```

---

# Example Complaint

```
Complaint ID:
CMP-BC2A1D41


Title:
Laptop Not Working


Category:
TECHNICAL


Priority:
HIGH


Status:
OPEN
```

---

# Learning Outcomes

Through this project, the following skills were practiced:

- Designing a Java backend application
- Applying OOP principles
- Creating modular architecture
- Managing application data
- Implementing authentication flow
- Building workflow-based systems
- Handling real-world problem scenarios


---

# Future Enhancements

Possible improvements:

- JDBC + MySQL database integration
- REST API using Spring Boot
- Web frontend
- Email notifications
- Dashboard analytics
- AI-based complaint classification
- Cloud deployment


---

# Screenshots

Project screenshots are available in:

```
screenshots/
```

---

# Author

**Rohan Maurya**

Java Developer Portfolio Project


---

# Special Thanks

Special thanks to my mentor **Umesh Yadav** for guidance, support, and valuable feedback throughout this project.

---

# License

This project is created for learning .