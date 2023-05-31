import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image

path = filedialog.askopenfilename(initialdir=".", filetypes=(("Supported Image Files","*.png *.jpg *.jpeg"),("All Files","*.*")),title="Open Image")

image = Image.open(path)

#path = filedialog.askopenfilename(initialdir=".", filetypes=(("Bitmap Basic File","*.bmb *.bmp2"),("All Files","*.*")),title="Save As")

SaveAs = filedialog.asksaveasfilename(initialdir=".",filetypes=(("Compressed Image Format","*.cif"),("All Files","*.*")),title="Save As",defaultextension=".cif")

file = open(SaveAs,'wb')

#file = filedialog.asksaveasfilename(initialdir=".",filetypes=(("Bitmap Basic File","*.bmb *.bmb2"),("All Files","*.*")),title="Save As",defaultextension=".bmb")

imagesize = image.size

compression = (tkinter.simpledialog.askinteger("Compression", "Compression Value 1-255: "))

if imagesize[0]>65635 or imagesize[1]>65635:
    print("Image too big!")
    imagesize = (65635,65635)

pointer = [0,0]

file.write(int(compression).to_bytes(1))
file.write(int(imagesize[0]).to_bytes(2,'little'))
file.write(int(imagesize[1]).to_bytes(2,'little'))

while True:
    pixel = image.getpixel((pointer[0],pointer[1]))
    lum = (pixel[0]*0.299)+(pixel[1]*0.587)+(pixel[2]*0.114)
    cb = (-0.1687*pixel[0])-(0.3313*pixel[1])+(0.5*pixel[2])+128
    cr = (0.5*pixel[0])-(0.4187*pixel[1])-(0.0813*pixel[2])+128
    if pointer[0]%compression == 0:
        file.write(int(cr).to_bytes())
        file.write(int(cb).to_bytes())
    file.write(int(lum).to_bytes())
    if pointer[0]<(imagesize[0])-1:
        pointer[0] = pointer[0] + 1
    else:
        pointer[0] = 0
        pointer[1] = pointer[1] + 1
        if pointer[1]>(imagesize[1])-2:
            break

file.close()
image.close()
tkinter.messagebox.showinfo(title="Successful",message="File Conversion was Successful!")
#print("Successful!")
#input()
