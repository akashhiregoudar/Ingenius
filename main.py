import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from PIL import ImageTk,Image
import numpy
import textwrap
import pytesseract
from tkinter import Canvas
from tkinter import Label
from tkinter import LabelFrame


root=tk.Tk()
root.title('SoftechWings')
img = ImageTk.PhotoImage(Image.open(r'logo.png'))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes", padx=30, pady=20)
canvas= Canvas(root,width=900, height=500, bg='#434e52')
canvas.pack()
lable= Label(canvas,text='Team SoftechWings')
lable.config(font=("Courier", 20))
lable.pack()
filename=''

def fileDialog():
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("All Files", "*.*"), ("All Files", "*.*")))
        label = ttk.Label(labelFrame, text="")
        label.grid(column=1, row=2)
        base = os.path.basename(filename)
        filename, file_extension = os.path.splitext(filename)
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        x = Image.open(filename + file_extension)
        count = 0
        file = open(filename + ".txt" , "a")
        while True:
            try :
                x.seek(count)
            except EOFError:
                break
            count += 1
        if count == 1:
            x.save(filename + "1.jpg")
        else:
            for y in range(0, count):
                x.seek(y)
                x.save(filename + f"{y}.jpg")
        count = 0
        while True:
            try:
                x.seek(count)
            except EOFError:
                break
            count += 1

        if count == 1:
            file.write(pytesseract.image_to_string(filename + "1.jpg"))
            os.remove(filename + "1.jpg")
        else:
            for y in range(0, count):
                file.write(pytesseract.image_to_string(filename + f"{y}.jpg"))
                os.remove(filename + f"{y}.jpg")
        label.configure(text="Successfully Completed")
        file.close()


labelFrame=LabelFrame(root,width=75, height=40)
labelFrame.pack()
b=button = ttk.Button(labelFrame, text = "Browse file", command = fileDialog)
button.grid(pady=25,padx=50)
root.mainloop()