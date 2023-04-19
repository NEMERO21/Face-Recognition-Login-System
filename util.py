import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

def get_button(master, text, color, command, fg='white'):
    button = tk.Button(master, text=text, bg=color, fg=fg, font=('Arial', 14), command=command)
    return button

def get_text_label(master, text, font_size=14):
    label = tk.Label(master, text=text, font=('Arial', font_size))
    return label

def get_entry_text(master):
    entry_text = tk.Text(master, height=1, width=20, font=('Arial', 14))
    return entry_text

def get_img_label(master):
    img_label = tk.Label(master)
    return img_label

def add_img_to_label(label, img):
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.config(image=imgtk)

def msg_box(title, message):
    messagebox.showinfo(title, message)
