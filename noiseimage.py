import random
file = open("test.cif",'wb')

compression=16
sizex = 512
sizey = 512

file.write(int(compression).to_bytes(1))
file.write(int(sizex).to_bytes(2,'little'))
file.write(int(sizey).to_bytes(2,'little'))

for i in range(4,sizex*sizey*3):
    file.write(int(random.random()*255).to_bytes())
