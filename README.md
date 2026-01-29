# **🔐 File-Encryption-Tool**
A simple and secure **Python file encryption & decryption tool** using **password-based encryption** with **PBKDF2 + Fernet (AES)**.

This project allows you to encrypt any file using a password and decrypt it later using the same password.

---

## 🚀 Features

- 🔒 Encrypt any file with a password
- 🔓 Decrypt encrypted files
- 🔑 Secure key derivation using PBKDF2 + SHA256
- 🧂 Random salt for each file
- 🛡️ Uses industry-standard `cryptography` library
- 📦 Simple command-line interface
- ❌ Impossible to decrypt without the correct password

---

## 📁 Project Structure

File-Encryption-Tool/
│── main.py
│── crypto_utils.py
│── requirements.txt
│── README.md

---

## 🛠️ Installation

### 1️⃣ Install Python

Download from:
https://www.python.org/downloads/

Check installation:

``bash
python --version

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### ▶️ How to Run

Open terminal in project folder:

**python main.py**

---

## 🧪 How to Use

When the program starts, you will see:

1. Encrypt File
2. Decrypt File
3. Exit

### 🔐 Encrypt a File

Choose option 1

Enter file name (example):

test.txt

Enter password

Output:

test.txt.enc

### 🔓 Decrypt a File

Choose option 2

Enter encrypted file name:

test.txt.enc

Enter the same password

Output:

test.txt

---

## 🔒 How It Works

A random salt is generated for each file

Your password is converted into a strong key using:

PBKDF2

SHA256

Encryption is done using:

Fernet (AES + HMAC)

The salt is stored inside the encrypted file

Without the correct password, the file cannot be decrypted

---

## ⚠️ Important Notes

  ❗ If you forget the password, the file cannot be recovered

  ❗ Do not modify .enc files manually

  ❗ This is real encryption, not fake or reversible encoding

---

## 🎯 Good For

  Cybersecurity mini project

  Python cryptography learning

  Portfolio project

  Secure file storage tool

---

## 📦 Requirements

The project depends on:

**cryptography>=41.0.0**

---

## 📜 License

Free to use for educational purposes.

---

##✨ Author

Created by **Lobaina Ehsan**
Gmail: lobaina401@gmail.com

---
