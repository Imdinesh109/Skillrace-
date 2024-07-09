import tkinter as tk
from tkinter import messagebox
import time
class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.geometry("300x150")
        self.label = tk.Label(master, text="Enter time in seconds:", font=("Helvetica", 12))
        self.label.pack(pady=10)
        self.entry = tk.Entry(master, font=("Helvetica", 14))
        self.entry.pack(pady=5)
        self.start_button = tk.Button(master, text="Start Timer", command=self.start_timer, font=("Helvetica", 12))
        self.start_button.pack(pady=5)
        self.time_label = tk.Label(master, text="", font=("Helvetica", 18))
        self.time_label.pack(pady=10)
    def start_timer(self):
        try:
            self.time_left = int(self.entry.get())
            self.update_timer()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number of seconds.")
    def update_timer(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            time_format = f'{mins:02d}:{secs:02d}'
            self.time_label.config(text=time_format)
            self.time_left -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.time_label.config(text="Time's up!")
            messagebox.showinfo("Time's up", "The countdown has finished.")
if __name__ == "__main__":
    root = tk.Tk()
    countdown_timer = CountdownTimer(root)
    root.mainloop()