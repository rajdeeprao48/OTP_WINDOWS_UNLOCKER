import secrets
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
import logging
from tkinter import messagebox

# Configure logging to display INFO level messages
logging.basicConfig(level=logging.INFO)

class OTPService:
    def __init__(self):
        """
        Initializes the OTPService class, setting up initial values for the OTP,
        email entry widget, OTP entry widgets, root Tkinter window, and verification status.
        """
        self.otp = self.generate_otp()  # Generate an initial OTP
        self.email_entry = None  # Entry widget for the email address
        self.otp_entries = []  # List to store OTP entry widgets
        self.root = None  # Root Tkinter window
        self.verification_complete = False  # Flag to track if verification is complete

    @staticmethod
    def generate_otp():
        """
        Generates a 6-digit OTP (One Time Password).
        Uses secrets.randbelow to create a random number and zfill to ensure it is 6 digits long.
        
        Returns:
            str: 6-digit OTP as a string.
        """
        return str(secrets.randbelow(10 ** 6)).zfill(6)

    def send_otp_via_email(self, email_address):
        """
        Sends the generated OTP to the specified email address using SMTP.
        
        Parameters:
            email_address (str): The recipient email address.
        """
        if email_address.lower() != "rajdeeprao@amityonline.com":
            # Show an error if the email is incorrect
            messagebox.showerror("INVALID EMAIL", "PLEASE ENTER THE CORRECT EMAIL ADDRESS.".upper())
            return  # Stop execution if email is incorrect

        # SMTP server configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "rajdeepraoextras@gmail.com"
        smtp_password = "suuk olda bvpp xnub"

        # Create the email message
        msg = MIMEText(f"YOUR OTP TO UNLOCK YOUR SYSTEM IS: {self.otp}")
        msg["Subject"] = "OTP TO UNLOCK".upper()
        msg["From"] = smtp_username
        msg["To"] = email_address

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(smtp_username, smtp_password)  # Log in to the SMTP server
                server.sendmail(smtp_username, email_address, msg.as_string())  # Send the email
            logging.info(f"OTP SENT TO {email_address} SUCCESSFULLY")
            messagebox.showinfo("SUCCESS", "OTP HAS BEEN SENT SUCCESSFULLY!".upper())
        except Exception as e:
            # Log and display an error if the email could not be sent
            logging.error(f"FAILED TO SEND OTP MAIL: {e}")
            messagebox.showerror("ERROR", f"FAILED TO SEND OTP: {e}".upper())

    def create_gui(self):
        """
        Creates and displays the Tkinter GUI for OTP verification.
        """
        self.root = tk.Tk()  # Create the main Tkinter window
        self.root.title("OTP VERIFICATION TO UNLOCK SYSTEM".upper())  # Set the window title

        # Make the window full-screen
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)

        # Disable the close button until verification is complete
        self.root.protocol("WM_DELETE_WINDOW", self.disable_close)

        # Set a dark-themed background for the window
        self.root.configure(bg="#1e1e1e")

        # Main Frame to contain all other widgets
        main_frame = tk.Frame(self.root, bg="#1e1e1e")
        main_frame.pack(expand=True)

        # Header Label
        header_label = tk.Label(main_frame, text="WELCOME BACK".upper(), font=("Consolas", 36, "bold"), fg="#00ff00", bg="#1e1e1e")
        header_label.pack(pady=20)

        # Label for Email Entry
        email_label = tk.Label(main_frame, text="ENTER YOUR MAIL TO RECEIVE AN OTP:".upper(), font=("Consolas", 20), fg="#00ff00", bg="#1e1e1e")
        email_label.pack(pady=10)

        # Email Entry Widget
        self.email_entry = tk.Entry(main_frame, width=30, font=("Consolas", 18), fg="white", bg="#333333", bd=0, relief="flat")
        self.email_entry.pack(pady=10, ipady=10)

        # Button to Send OTP
        send_otp_button = tk.Button(main_frame, text="SEND OTP".upper(), command=self.send_otp, font=("Consolas", 18), bg="#007700", fg="white", bd=0, relief="flat")
        send_otp_button.pack(pady=20)

        # Label for OTP Entry
        otp_label = tk.Label(main_frame, text="ENTER OTP:".upper(), font=("Consolas", 20), fg="#00ff00", bg="#1e1e1e")
        otp_label.pack(pady=10)

        # Frame to contain OTP Entry Widgets (6 boxes for 6 digits)
        otp_frame = tk.Frame(main_frame, bg="#1e1e1e")
        otp_frame.pack(pady=10)

        for i in range(6):
            # Create OTP entry widgets and add them to the frame
            otp_entry = tk.Entry(otp_frame, width=2, font=("Consolas", 36), fg="white", bg="#333333", justify="center", bd=0, relief="flat")
            otp_entry.grid(row=0, column=i, padx=5)
            otp_entry.bind("<KeyRelease>", self.move_focus)  # Bind the focus movement event
            self.otp_entries.append(otp_entry)

        # Button to Verify OTP
        verify_button = tk.Button(main_frame, text="VERIFY OTP".upper(), command=self.verify_otp, font=("Consolas", 18), bg="#007700", fg="white", bd=0, relief="flat")
        verify_button.pack(pady=20)

        # Footer Label
        footer_label = tk.Label(main_frame, text="MADE WITH ❤️ BY RAJDEEP RAO".upper(), font=("Consolas", 14), fg="#00ff00", bg="#1e1e1e")
        footer_label.pack(pady=40)

        # Start the Tkinter main loop
        self.root.mainloop()

    def disable_close(self):
        """
        Prevents the window from closing if OTP verification is not complete.
        """
        if not self.verification_complete:
            messagebox.showwarning("WARNING", "YOU CANNOT CLOSE THE WINDOW UNTIL OTP VERIFICATION IS COMPLETE.".upper())

    def send_otp(self):
        """
        Retrieves the email address from the entry widget and sends the OTP.
        """
        email_address = self.email_entry.get()
        self.send_otp_via_email(email_address)

    def verify_otp(self):
        """
        Retrieves the OTP entered by the user and verifies it against the generated OTP.
        """
        user_otp = "".join(entry.get() for entry in self.otp_entries)
        if user_otp == self.otp:
            logging.info("OTP VERIFICATION SUCCESSFUL")
            self.verification_complete = True  # Mark verification as complete
            self.root.destroy()  # Close the window now
        else:
            logging.error("OTP VERIFICATION FAILED")
            messagebox.showerror("ERROR", "INCORRECT OTP. PLEASE TRY AGAIN.".upper())

    def move_focus(self, event):
        """
        Moves focus to the next OTP entry widget when a digit is entered.
        
        Parameters:
            event (tk.Event): The event triggered when a key is released.
        """
        current_widget = event.widget
        next_widget_index = self.otp_entries.index(current_widget) + 1
        if event.keysym.isdigit() and next_widget_index < len(self.otp_entries):
            self.otp_entries[next_widget_index].focus()

# Run the OTP service
otp_service = OTPService()
otp_service.create_gui()
