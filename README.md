# Windows OTP Unlocker

## Project Overview

The **Windows OTP Unlocker** is a security application that verifies a user's identity by sending a One-Time Password (OTP) to a pre-configured email address (`rajdeephighondata@gmail.com`). This application ensures access is granted only when the correct OTP is entered. The system features enhanced security by strictly validating email input and rejecting any unauthorized email addresses. This project can serve as an example for basic authentication systems used in applications requiring secure login mechanisms.

---

## Features

### 1. **OTP Verification System**:
   - The system generates a random six-digit OTP and sends it to the registered email address (`rajdeephighondata@gmail.com`).
   - Once the user enters the correct OTP in the application, access is granted.
   - If an incorrect OTP is entered, an error message is displayed, allowing the user to retry.
   - The OTP remains valid for a limited time (modifiable based on your needs).

### 2. **Email Validation**:
   - The application ensures that only the pre-configured email (`rajdeephighondata@gmail.com`) is valid for receiving the OTP.
   - If the user enters any email other than the registered one, an "Invalid Email" error is triggered, and the OTP is not sent.

### 3. **Simple GUI Interface**:
   - A user-friendly interface built using `tkinter` allows easy input of the email address and OTP.
   - Minimalist design that ensures ease of use while maintaining security.

### 4. **Enhanced Security Mechanism**:
   - By enforcing a fixed email address, the application minimizes the risk of unauthorized access.
   - The OTP is securely generated and delivered through the email system using SMTP.

---

## Prerequisites

To run this project, the following prerequisites must be met:

1. **Python Version**:
   - The application requires Python 3.7 or higher.

2. **Required Python Libraries**:
   - `Pillow` – for image handling (used in GUI if needed for visual enhancements).
   - `tkinter` – to create the graphical user interface.
   - `smtplib` – to send emails containing the OTP.
   
   Install these libraries using `pip`:
   ```bash
   pip install Pillow
