# Caesar Cipher Encryption/Decryption Tool

![GUI Screenshot](screenshot.png) <!-- Add actual screenshot later -->

A Python GUI application for encrypting/decrypting text and files using the classic Caesar Cipher algorithm.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [License](#license)

## Introduction
The Caesar Cipher is one of the oldest encryption techniques, used by Julius Caesar to protect military communications. This project implements a modern GUI version that handles both text input and file encryption/decryption (.txt and .docx formats).

## Features
- **Text Encryption/Decryption**: Direct input/output in GUI text areas
- **File Support**: Process .txt and .docx files (preserves Word document structure)
- **Shift Customization**: Choose shift values between 1-25
- **Drag-and-Drop**: Intuitive file handling using TkinterDnD2
- **Real-time Results**: Instant encryption/decryption feedback
- **Error Handling**: Input validation for shift keys and file types

## Installation
1. Clone repository:
```bash
git clone https://github.com/yourusername/caesar-cipher-tool.git
cd caesar-cipher-tool