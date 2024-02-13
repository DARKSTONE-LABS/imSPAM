import tkinter as tk
from tkinter import ttk
import time
from threading import Thread
import pyperclip
import pyautogui

def countdown():
    for i in range(3, 0, -1):
        app.update()  # Update the GUI to refresh the countdown label
        countdown_label.config(text=str(i))
        time.sleep(1)
    countdown_label.config(text="Go!")
    app.update()  # Update the GUI to show the "Go!" message
    start_loop()

def start_loop():
    try:
        quantity = int(quantity_entry.get())
        interval = float(interval_entry.get())
        text_to_send = text_entry.get()
        for _ in range(quantity):
            pyperclip.copy(text_to_send)
            pyautogui.hotkey('ctrl', 'v')  # Paste the text from the clipboard
            pyautogui.press('enter')  # Simulate pressing the Enter key
            time.sleep(interval)
    finally:
        countdown_label.config(text="")

def start_thread():
    Thread(target=countdown, daemon=True).start()

app = tk.Tk()
app.title("imSPAM")
app.geometry("400x400")
app.configure(bg='#000000')
app.attributes('-topmost', True)

text_label = ttk.Label(app, text="Text to Send:", foreground="green", background="black", font=("Arial", 12, "bold"))
text_label.pack(pady=(20,0))
text_entry = ttk.Entry(app, font=("Arial", 12))
text_entry.pack(fill=tk.X, padx=50, pady=5)

quantity_label = ttk.Label(app, text="Quantity:", foreground="green", background="black", font=("Arial", 12, "bold"))
quantity_label.pack()
quantity_entry = ttk.Entry(app, font=("Arial", 12))
quantity_entry.pack(fill=tk.X, padx=50, pady=5)

interval_label = ttk.Label(app, text="Time Interval (seconds):", foreground="green", background="black", font=("Arial", 12, "bold"))
interval_label.pack()
interval_entry = ttk.Entry(app, font=("Arial", 12))
interval_entry.pack(fill=tk.X, padx=50, pady=5)

countdown_label = ttk.Label(app, text="", foreground="green", background="black", font=("Arial", 16, "bold"))
countdown_label.pack(pady=5)

start_button = ttk.Button(app, text="Start", command=start_thread)
start_button.pack(side=tk.LEFT, expand=True, padx=(50,10), pady=20)

stop_button = ttk.Button(app, text="Stop", command=app.quit)
stop_button.pack(side=tk.RIGHT, expand=True, padx=(10,50), pady=20)

app.mainloop()
