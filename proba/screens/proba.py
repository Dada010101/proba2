

import tkinter as tk
from PIL import Image, ImageTk

def add_image():
    text.image_create(tk.END, image = img) # Example 1
    text.window_create(tk.END, window = tk.Label(text, image = img)) # Example 2

root = tk.Tk()

text = tk.Text(root)
text.pack(padx = 20, pady = 20)

tk.Button(root, text = "Insert", command = add_image).pack()
a= Image.open("./images/imagesBiljke/bosiljak.jpg")

img = ImageTk.PhotoImage(a)

root.mainloop()