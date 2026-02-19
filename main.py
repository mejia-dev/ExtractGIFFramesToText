import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from ascii_magic import AsciiArt

filepath = None
canvas = None
num_keyframes = 20
columns = 100

def write_message(message):
    canvas.delete("all")
    canvas.create_text(250, 125, text=message, font=("Arial", 10), fill="black")

def upload_file(event=None):
    global filepath
    filepath = filedialog.askopenfilename(
        title="Select a GIF",
        initialdir="./",
        filetypes=[
            ("GIF files", "*.gif")
        ]
    )
    write_message(f"Selected file: {filepath}")

def convert_to_ascii(event=None):
    if not filepath:
        write_message("No file selected.")
        return
    else:
        try:
            folder_path = './asciitemp'
            os.makedirs(folder_path, exist_ok=True)

            with Image.open(filepath) as img:
                for i in range(num_keyframes):
                    img.seek(img.n_frames // num_keyframes * i)
                    img.save(f'./asciitemp/{i}.png')
                    ascii_img = AsciiArt.from_image(f'./asciitemp/{i}.png')
                    ascii_img.to_file(f'./asciitemp/{i}.rtf', columns=100)
          
            write_message("Conversion complete!")
            for file in os.listdir(folder_path):
                if file.endswith('.png'):
                    os.remove(os.path.join(folder_path, file))

        except Exception as e:
            write_message(f"Error: {e}")

root = tk.Tk()
root.title("GIF to ASCII Converter")

canvas = tk.Canvas(root, width=500, height=250)
canvas.pack()

upload_button = tk.Button(root, text="Upload GIF", command=upload_file)
upload_button.pack(pady=10)

convert_button = tk.Button(root, text="Convert to ASCII", command=convert_to_ascii)
convert_button.pack(pady=10)

root.mainloop()