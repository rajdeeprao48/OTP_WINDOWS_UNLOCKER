import secrets
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
import logging
from tkinter import messagebox

logging.basicConfig(level=logging.INFO)

class OTPService:
    def __init__(self):
        self.otp = self.generate_otp()
        self.email_entry = None
        self.otp_entries = []
        self.root = None
        self.verification_complete = False  # Track if verification is done

    @staticmethod
    def generate_otp():
        return str(secrets.randbelow(10 ** 6)).zfill(6)  # 6-digit OTP

    def send_otp_via_email(self, email_address):
        if email_address != "rajdeeprao@amityonline.com":
            messagebox.showerror("invalid email", "please enter the correct email address.")
            return  # Stop execution if email is incorrect

        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "rajdeepraoextras@gmail.com"
        smtp_password = "suuk olda bvpp xnub"

        msg = MIMEText(f"your otp is: {self.otp}")
        msg["Subject"] = "otp to unlock"
        msg["From"] = smtp_username
        msg["To"] = email_address

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, email_address, msg.as_string())
            logging.info(f"OTP SENT TO {email_address} SUCCESSFULLY")
            messagebox.showinfo("Success", "OTP has been sent successfully!")
        except Exception as e:
            logging.error(f"FAILED TO SEND OTP MAIL: {e}")
            messagebox.showerror("error", f"failed to send otp: {e}")

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("otp verification to unlock system")

        # Make the window full-screen
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)

        # Disable close button until verification is complete
        self.root.protocol("WM_DELETE_WINDOW", self.disable_close)

        # Dark themed background
        self.root.configure(bg="#1e1e1e")

        # Main Frame
        main_frame = tk.Frame(self.root, bg="#1e1e1e")
        main_frame.pack(expand=True)

        # Header
        header_label = tk.Label(main_frame, text="welcome back", font=("Consolas", 36, "bold"), fg="#00ff00", bg="#1e1e1e")
        header_label.pack(pady=20)

        email_label = tk.Label(main_frame, text="enter your mail to receive an otp:", font=("Consolas", 20), fg="#00ff00", bg="#1e1e1e")
        email_label.pack(pady=10)

        # Email Entry
        self.email_entry = tk.Entry(main_frame, width=30, font=("Consolas", 18), fg="white", bg="#333333", bd=0, relief="flat")
        self.email_entry.pack(pady=10, ipady=10)

        send_otp_button = tk.Button(main_frame, text="send otp", command=self.send_otp, font=("Consolas", 18), bg="#007700", fg="white", bd=0, relief="flat")
        send_otp_button.pack(pady=20)

        otp_label = tk.Label(main_frame, text="enter otp:", font=("Consolas", 20), fg="#00ff00", bg="#1e1e1e")
        otp_label.pack(pady=10)

        # OTP Entry (6 boxes for 6 digits)
        otp_frame = tk.Frame(main_frame, bg="#1e1e1e")
        otp_frame.pack(pady=10)

        for i in range(6):
            otp_entry = tk.Entry(otp_frame, width=2, font=("Consolas", 36), fg="white", bg="#333333", justify="center", bd=0, relief="flat")
            otp_entry.grid(row=0, column=i, padx=5)
            otp_entry.bind("<KeyRelease>", self.move_focus)  # Add event to move focus
            self.otp_entries.append(otp_entry)

        verify_button = tk.Button(main_frame, text="verify otp", command=self.verify_otp, font=("Consolas", 18), bg="#007700", fg="white", bd=0, relief="flat")
        verify_button.pack(pady=20)

        # Footer
        footer_label = tk.Label(main_frame, text="made with ❤️ by rajdeep rao", font=("Consolas", 14), fg="#00ff00", bg="#1e1e1e")
        footer_label.pack(pady=40)

        # Start main loop
        self.root.mainloop()

    def disable_close(self):
        """Prevent window from closing unless verification is complete."""
        if not self.verification_complete:
            messagebox.showwarning("warning", "you cannot close the window until otp verification is complete.")

    def send_otp(self):
        email_address = self.email_entry.get()
        self.send_otp_via_email(email_address)

    def verify_otp(self):
        user_otp = "".join(entry.get() for entry in self.otp_entries)
        if user_otp == self.otp:
            logging.info("OTP VERIFICATION SUCCESSFUL")
            self.verification_complete = True  # Mark verification as complete
            self.root.destroy()  # Allow window to close now
        else:
            logging.error("OTP VERIFICATION FAILED")
            messagebox.showerror("error", "incorrect otp. please try again.")

    def move_focus(self, event):
        """Move focus to the next entry box when a digit is entered."""
        current_widget = event.widget
        next_widget_index = self.otp_entries.index(current_widget) + 1
        if event.keysym.isdigit() and next_widget_index < len(self.otp_entries):
            self.otp_entries[next_widget_index].focus()

# Run the OTP service
otp_service = OTPService()
otp_service.create_gui()
