import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import os

def generate_qr():
    data = entry.get()
    entries = [entry.strip() for entry in data.split(",")]  # Split input by commas
    num_entries = len(entries)
    num_columns = 3  # Number of columns in the grid
    for i, entry_text in enumerate(entries):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(entry_text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_pil = img.convert('RGB')
        img_tk = ImageTk.PhotoImage(img_pil)
        qr_labels[i].config(image=img_tk)
        qr_labels[i].image = img_tk

def save_qr_codes():
    data = entry.get()
    entries = [entry.strip() for entry in data.split(",")]  # Split input by commas
    for i, entry_text in enumerate(entries):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(entry_text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_pil = img.convert('RGB')
        filename = f"qrcode_{i+1}_{entry_text}.png"  # Unique filename based on content
        img_pil.save(filename)

# Create tkinter window
root = tk.Tk()
root.title("QR Code Generator")

# Create entry widget to take input
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Button to generate QR code
generate_button = tk.Button(root, text="Generate QR Codes", command=generate_qr)
generate_button.pack(pady=5)

# Button to save QR codes
save_button = tk.Button(root, text="Save QR Codes", command=save_qr_codes)
save_button.pack(pady=5)

# Labels to display QR codes
num_qrs = 6  # Number of QR codes to display
qr_labels = [tk.Label(root) for _ in range(num_qrs)]
for label in qr_labels:
    label.pack(pady=5, padx=5, side=tk.LEFT)

root.mainloop()
