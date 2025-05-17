# Caesar Cipher Encryption/Decryption Tool

![GUI Screenshot](screenshot.png)

A Python tool for encrypting and decrypting text and files using the classic Caesar Cipher algorithm. Includes both a **Graphical User Interface (GUI)** and a **Command-Line Interface (CLI)**.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [GUI Usage](#gui-usage)
  - [CLI Usage](#cli-usage)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [License](#license)

---

## Introduction

The Caesar Cipher is a basic encryption technique used by Julius Caesar. This project brings it to modern applications with:
- Real-time GUI encryption/decryption
- Support for `.txt` and `.docx` files
- Input validation and user-friendly features

---

## Features

- 🔐 **Text Encryption/Decryption**
- 📄 **File Support**: `.txt`, `.docx`
- 🔁 **Customizable Shift Key**: 1–25, wraps beyond 25
- 🖱️ **Drag & Drop Files** (via TkinterDnD2)
- ⚠️ **Error Handling** for invalid input
- 🎛️ **Interactive CLI Mode**

---

## Installation

1. **Clone this repository:**

```bash
git clone https://github.com/AdityaSomasagar/Encryption-and-decryption-tool.git
cd Encryption-and-decryption-tool
```

2. **Install required dependencies:**

```bash
pip install -r requirements.txt
```

_If `requirements.txt` is not available, install manually:_

```bash
pip install tkinter tkinterdnd2 python-docx
```

> Note: `tkinter` is included by default with most Python installations.

---

## Usage

### 🔵 GUI Usage

Run the GUI:

```bash
python gui_frontend.py
```

#### Steps:
1. **Enter Text** or **Upload File**
2. **Choose Operation**: Encrypt or Decrypt
3. **Enter Shift Key** (e.g., 3, 5, 13)
4. **View Output** instantly
5. **Save** results (for files)

#### Shift Key Rules

| Scenario          | Behavior                   |
|------------------|----------------------------|
| Shift = 0        | Invalid                    |
| Shift > 25       | Auto-adjusted (mod 26)     |
| Non-integer      | Shows error message        |

---

### ⚫ CLI Usage

Run the CLI version:

```bash
python main.py
```

#### Sample Workflow:

1. Select:
   - `1` for encryption
   - `2` for decryption
   - `3` to exit

2. Enter message:
   - e.g., `Hello World`

3. Enter shift:
   - e.g., `4`

4. Get result:
   - `Encrypted Message: Lipps Asvph`

---

## How It Works

- **CaesarCipher.py** contains encryption and decryption logic.
- **main.py** provides terminal interface.
- **gui_frontend.py** is the GUI built with Tkinter and TkinterDnD2.
- `.docx` files are processed using `python-docx` (preserves formatting).

---

## Limitations

- Only supports **English alphabets**
- Non-alphabetic characters are **preserved unchanged**
- Not suitable for **high-security** applications (for educational use only)

---

## License

This project is licensed under the MIT License.  
Feel free to use, modify, and share!

---

## Author

**Aditya A S**  
_Student project for educational/demo purposes._
