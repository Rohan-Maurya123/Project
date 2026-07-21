# Java Chat App with Socket Programming

A real-time console-based chat application built using Java Socket Programming and Multithreading.

This project demonstrates how client-server communication works using TCP sockets, where multiple clients can connect to a central server, exchange public messages, send private messages, manage usernames, and maintain chat history.

---

# Project Overview

Modern applications such as messaging platforms, collaboration tools, customer support systems, and multiplayer games rely on real-time communication between multiple users.

This project implements the core concepts behind such systems using:

- Java Networking
- TCP Socket Programming
- Multithreading
- Client-Server Architecture
- Exception Handling
- File Handling

The application allows multiple users to communicate through a central server in real time.

---

# Features

## Core Features

✅ Client-Server communication using TCP sockets  
✅ Multiple client connections  
✅ Real-time public messaging  
✅ Private messaging between users  
✅ Username management  
✅ Join and leave notifications  
✅ Active user list  
✅ Graceful client disconnect  
✅ Server-side chat logging  
✅ Multithreaded client handling  
✅ Exception handling  

---

# Commands

| Command | Description |
|--------|-------------|
| `/users` | Display currently connected users |
| `/msg username message` | Send a private message |
| `/exit` | Disconnect from the chat server |

Example:

```
/msg Aman Hello Aman
```

---

# Project Architecture

```
                    Client 1
                       |
                       |
                    Socket
                       |
                       |
Client 2  -------- Chat Server -------- Client 3
                       |
                       |
              Client Handler Threads
                       |
                       |
               Message Management
                       |
                       |
                Chat History Logger
```

---

# Working Flow

```
Client Starts

      |
      ↓

Connects to ServerSocket

      |
      ↓

Server Accepts Connection

      |
      ↓

Creates ClientHandler Thread

      |
      ↓

User Sends Message

      |
      ↓

Server Processes Message

      |
      ↓

Broadcast / Private Message

      |
      ↓

Clients Receive Message
```

---

# Technology Stack

| Technology | Purpose |
|-----------|---------|
| Java | Application development |
| Socket Programming | Network communication |
| TCP | Reliable communication protocol |
| Threads | Handling multiple clients |
| File Handling | Chat history storage |

---

# Project Structure

```
Java-Chat-App-Socket-Programming/

│
├── src/
│   │
│   ├── server/
│   │   ├── ChatServer.java
│   │   ├── ClientHandler.java
│   │   └── ServerManager.java
│   │
│   ├── client/
│   │   ├── ChatClient.java
│   │   ├── ClientSender.java
│   │   └── ClientReceiver.java
│   │
│   ├── common/
│       ├── Constants.java
│       ├── TimeUtil.java
│       ├── MessageFormatter.java
│       ├── UsernameValidator.java
│       └── ChatLogger.java
│
├── logs/
│   └── chat_history.txt
│
├── screenshots/
│
├── docs/
│
├── README.md
├── .gitignore
└── LICENSE
```

---

# How To Run

## Requirements

- Java JDK 17 or above
- VS Code / IntelliJ IDEA / Eclipse
- Terminal or Command Prompt

---

# Compile Project

Open terminal in project folder.

Run:

```bash
javac -d out src/common/*.java src/server/*.java src/client/*.java
```

---

# Start Server

Run:

```bash
java -cp out server.ChatServer
```

Expected output:

```
======================================
      JAVA CHAT SERVER STARTED
======================================

Host : localhost
Port : 5000

Chat Server started successfully...
Waiting for clients...
```

---

# Start Client

Open another terminal.

Run:

```bash
java -cp out client.ChatClient
```

Enter username:

```
Rohan
```

---

# Multiple Client Testing

Open multiple terminals:

Client 1:

```
Rohan
```

Client 2:

```
Aman
```

Client 3:

```
Priya
```

All users can communicate through the same server.

---

# Example Chat

Public Message:

```
Rohan:
Hello everyone
```

Output:

```
[10:30:12] Rohan : Hello everyone
```

---

Private Message:

```
/msg Aman Hello Aman
```

Output:

```
[PRIVATE] Rohan -> Aman : Hello Aman
```

---

# Multithreading Concept

Every connected client receives its own thread.

Example:

```
Client 1
   |
ClientHandler Thread 1


Client 2
   |
ClientHandler Thread 2


Client 3
   |
ClientHandler Thread 3
```

This allows multiple users to communicate simultaneously.

---

# Networking Concepts Used

## Socket

Provides communication endpoint between client and server.

## ServerSocket

Used by the server to listen for incoming client connections.

## BufferedReader

Receives messages from network streams.

## PrintWriter

Sends messages through socket connections.

## Threads

Allows multiple clients to communicate at the same time.

---

# Testing Completed

The application was tested for:

✅ Multiple client connections  
✅ Public messaging  
✅ Private messaging  
✅ User list functionality  
✅ Client disconnect  
✅ Username validation  
✅ Chat logging  
✅ Server-client communication  

---

# Future Improvements

Possible enhancements:

- GUI using Java Swing or JavaFX
- User authentication
- Database storage
- File sharing
- Chat rooms
- Online/offline status
- Cloud server deployment

---

# Learning Outcomes

Through this project, I learned:

- How TCP communication works
- How client-server applications are designed
- How multithreading manages multiple users
- How sockets transfer data
- How real-time communication systems work

---

# Author

**Rohan Maurya**

Java Developer | Backend Learner

---

# Special Thanks

Special thanks to my mentor **Umesh Yadav** for guidance, support, and continuous motivation throughout this learning journey.

---

# License

This project is licensed under the MIT License.