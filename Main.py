from tkinter import *
from random import choice
import string

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Generator")
        self.window.geometry("500x300")
        self.window.config(bg="#1e1e1e")  # Dark background

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        Label(
            self.window,
            text="🔐 Password Generator",
            font=("Segoe UI", 20, "bold"),
            bg="#1e1e1e",
            fg="#00ffcc"
        ).pack(pady=(20, 10))

        # Entry field
        self.password_entry = Entry(
            self.window,
            font=("Consolas", 16),
            bg="#2e2e2e",
            fg="#00ffcc",
            width=30,
            relief="raised",
            justify="center",
            insertbackground="#00ffcc"
        )
        self.password_entry.pack(pady=(0, 20))

        # Length slider
        self.length = IntVar(value=16)
        frame = Frame(self.window, bg="#1e1e1e")
        frame.pack(pady=10)
        Label(frame, text="Password Length:", font=("Segoe UI", 10), bg="#1e1e1e", fg="white").pack(side=LEFT)
        Scale(
            frame, from_=8, to=40, orient=HORIZONTAL,
            variable=self.length, bg="#1e1e1e", fg="#00ffcc",
            troughcolor="#333333", highlightthickness=0
        ).pack(side=LEFT)

        # Buttons
        Button(
            self.window,
            text="Generate Password",
            font=("Segoe UI", 12, "bold"),
            bg="#00ffcc",
            fg="#1e1e1e",
            activebackground="#00e6b8",
            relief="flat",
            command=self.generate_password
        ).pack(pady=(15, 5))

        Button(
            self.window,
            text="📋 Copy to Clipboard",
            font=("Segoe UI", 10),
            bg="#2e2e2e",
            fg="white",
            activebackground="#444444",
            relief="flat",
            command=self.copy_password
        ).pack()

    def generate_password(self):
        characters = string.ascii_letters + string.punctuation + string.digits
        length = self.length.get()
        password = ''.join(choice(characters) for _ in range(length))
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

    def copy_password(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.password_entry.get())
        self.window.update()

if __name__ == "__main__":
    app = App()
    app.window.mainloop()
