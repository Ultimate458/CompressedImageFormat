from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pygame,os

path = filedialog.askopenfilename(initialdir=".", filetypes=(("Compressed Image Format","*.cif"),("All Files","*.*")),title="Load CIF Image")
file = open(path,'rb')

cmp=int.from_bytes(file.read(1))
x=int.from_bytes(file.read(2),'little')
y=int.from_bytes(file.read(2),'little')
print(str(cmp))
print(str(x))
print(str(y))
size = x*y

pygame.init()
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption(path)

running = True

pointer = [0,0]
pixpoint = 0
pixel = [0,0,0]

first=True
lcr=0
lcb=0
cr=0
cb=0
cro=0
cbo=0

def lerp(a,b,x):
    return a+(b-a)*x

def norm(a):
    b = int(a+0.5)
    if b<0:
        b=0
    if b>255:
        b=255
    return b

while True:
    percomp = pointer[0]%cmp
    if percomp == 0:
        lcr=cr
        lcb=cb
        cro = int.from_bytes(file.read(1))
        cbo = int.from_bytes(file.read(1))
        cr=lcr
        cb=lcb
        if first:
            first=False
            lcr=cr
            lcb=cb
    else:
        cr = lerp(lcr,cro,percomp/cmp)
        cb = lerp(lcb,cbo,percomp/cmp)
        
    lum = int.from_bytes(file.read(1))
    
    pixel[2] = norm(lum + 1.772 * (cb-128))
    pixel[1] = norm(lum - 0.344136 * (cb-127) - 0.714136 * (cr-128))
    pixel[0] = norm(lum + 1.402 * (cr-128))
    try:
        screen.set_at([(pointer[0]),(pointer[1])],pixel)
    except:
        print(pixel)
    
    if pointer[0]<x-1:
        pointer[0]=pointer[0]+1
    else:
        pygame.event.pump()
        pygame.display.flip()
        pointer[0]=0
        pointer[1]=pointer[1]+1
        if pointer[1] == y:
            break
            
pygame.display.flip()

file.close()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
