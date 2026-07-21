# 🔐 Encryption-Decryption Tool (Java Swing)

A desktop-based **Encryption-Decryption Tool** developed using **Java Swing** that allows users to securely encrypt and decrypt both text and files using **AES-GCM encryption** with password-based key derivation.

This project demonstrates modern cryptographic practices, secure password handling, file processing, and Java GUI development in a beginner-friendly and modular structure.

---

## 🚀 Features

### Text Encryption & Decryption

* Encrypt plaintext using AES-GCM
* Decrypt encrypted text using the correct password
* Base64 encoded encrypted output
* Secure password-based encryption

### File Encryption & Decryption

* Encrypt selected files
* Decrypt encrypted files
* Restore original file content
* Support for text and binary files

### User Interface

* Java Swing graphical interface
* Plain text input area
* Encrypted/Decrypted output area
* Password field
* Encrypt button
* Decrypt button
* Copy output button
* Clear button
* File selection support
* Status messages

### Security

* AES-GCM authenticated encryption
* PBKDF2WithHmacSHA256 password-based key derivation
* Random salt generation
* Random IV generation
* No hardcoded passwords or encryption keys
* Passwords are never stored

---

## 🏗️ Project Structure

```text
Encryption-Decryption-Tool-Java-GUI/

├── src/
│   ├── gui/
│   ├── crypto/
│   ├── service/
│   ├── utility/
│   ├── exception/
│   └── main/
│
├── sample_files/
├── encrypted_files/
├── decrypted_files/
├── outputs/
├── screenshots/
├── docs/
│
├── README.md
├── .gitignore
└── pom.xml
```

---

## ⚙️ Technologies Used

* Java 17+
* Java Swing
* AES-GCM Encryption
* PBKDF2WithHmacSHA256
* Base64 Encoding
* SecureRandom
* JFileChooser

---

## 🔐 Encryption Workflow

```text
Plain Text
     │
     ▼
Password
     │
     ▼
PBKDF2 Key Derivation
     │
     ▼
Random Salt + Random IV
     │
     ▼
AES-GCM Encryption
     │
     ▼
Base64 Encoding
     │
     ▼
Encrypted Output
```

---

## 🔓 Decryption Workflow

```text
Encrypted Text
      │
      ▼
Base64 Decode
      │
      ▼
Extract Salt + IV
      │
      ▼
PBKDF2 Key Derivation
      │
      ▼
AES-GCM Decryption
      │
      ▼
Original Plain Text
```

---

## ▶️ How to Run

1. Clone the repository.
2. Open the project in IntelliJ IDEA or Eclipse.
3. Ensure Java 17 (or later) is installed.
4. Run:

```text
src/main/Main.java
```

5. Enter text and password.
6. Encrypt or decrypt text and files using the GUI.

---

## 📚 Learning Outcomes

Through this project, I explored:

* Java Swing GUI development
* AES-GCM encryption
* Password-based key derivation (PBKDF2)
* Secure file handling
* Exception handling
* Modular project architecture
* Object-Oriented Programming in Java

---

## 📌 Future Improvements

* Save output functionality
* Show/Hide password
* Improved UI design
* Password strength indicator
* Theme selector
* Drag-and-drop file support
* Executable JAR packaging

---

## 👨‍🏫 Acknowledgement

A heartfelt thank you to my mentor **Umesh Yadav** for the continuous guidance, encouragement, and support throughout this learning journey. The concepts, feedback, and motivation have played a significant role in helping me build projects like this with confidence.

---

## 📄 License

This project is created for educational and learning purposes.
