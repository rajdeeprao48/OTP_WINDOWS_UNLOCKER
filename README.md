# OTP Verification System using Python and Tkinter

This project implements an OTP (One Time Password) verification system using Python, Tkinter for GUI, and SMTP for email communication. The purpose of this application is to securely verify a user's identity through an OTP sent via email. The system features a full-screen GUI, user input validation, and OTP generation and verification.

## Features

- **OTP Generation**: Generates a random 6-digit OTP using Python's `secrets` module for secure OTP creation.
- **Email Validation**: The user is required to enter a specific email (customizable) to receive the OTP. Incorrect emails trigger an error message.
- **Send OTP via Email**: The system sends the generated OTP to the specified email using SMTP.
- **OTP Verification**: The user enters the OTP in a custom interface with 6 individual boxes, and the system verifies it.
- **Full-screen GUI**: The application runs in full-screen mode to prevent unauthorized closure.
- **Error Handling**: Comprehensive error handling is provided for email sending and OTP verification failures.
- **Disable Close**: The window cannot be closed until the OTP verification is successfully completed.

## Technologies Used

- **Python 3.x**: The core programming language for the entire project.
- **Tkinter**: Used for the graphical user interface (GUI).
- **SMTP (Simple Mail Transfer Protocol)**: Used to send the OTP to the user's email address.
- **Secrets Module**: For secure and random OTP generation.
- **Logging**: Python's `logging` module is used to capture success or failure of various actions like OTP generation and email sending.

## Prerequisites

- **Python 3.x**: Make sure you have Python 3 installed on your system.
- **Tkinter**: Comes pre-installed with Python, but if missing, you can install it via your package manager.
- **SMTP Gmail Access**: To send emails, you will need a valid Gmail account and enable "Less Secure App Access" for your account or use an App Password if you have 2FA enabled.
  
### Install Required Packages

Use `pip` to install necessary dependencies.

```bash
pip install smtplib
pip install email