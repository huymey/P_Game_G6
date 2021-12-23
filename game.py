

import tkinter as tk
root=tk.Tk()
root.geometry("600x600")
frame=tk.Frame()
frame.master.title("move up & down")
canvas=tk.Canvas(frame)

####add image

myImage= tk.PhotoImage(file='images/player.png')
img=tk.PhotoImage(file="images/walls.png")
anemy3= tk.PhotoImage(file='images/Enyme3.png')
anemy4=tk.PhotoImage(file='images/Enyme4.png')
anemy5=tk.PhotoImage(file='images/Enyme5.png')
anemy6=tk.PhotoImage(file='images/Enyme6.png')
coins=tk.PhotoImage(file='images/Coins.png')

####Data

empty=0
wall=2
player=1
coin=3
monster=4



#####Draw grid
grid=[
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,2,0,2,2,2,2,2,0,2,2,2,2,2,0,2,0,0,2],
    [2,0,2,0,2,0,0,0,0,0,0,0,0,0,2,0,2,0,0,2],
    [2,0,2,0,2,0,2,2,2,2,2,2,2,0,2,0,2,0,0,2],
    [2,0,2,0,2,0,2,0,0,0,0,0,0,0,2,0,2,0,0,2],
    [2,0,2,0,2,0,2,0,2,2,2,2,2,0,2,0,2,0,0,2],
    [2,0,2,0,2,0,2,0,6,0,4,0,2,0,2,0,2,0,0,2],
    [2,0,2,0,0,0,2,0,0,3,0,5,2,0,0,0,2,0,0,2],
    [2,0,2,0,2,0,2,0,2,2,2,2,2,0,2,0,2,0,0,2],
    [2,0,2,0,2,0,2,0,0,0,0,0,0,0,2,0,2,0,0,2],
    [2,0,2,0,2,0,2,2,2,2,2,2,2,0,2,0,2,0,0,2],
    [2,0,2,0,2,0,0,0,0,0,0,0,0,0,2,0,2,0,0,2],
    [2,0,2,0,2,2,2,2,2,0,2,2,2,2,2,0,2,0,0,2],
    [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2],
    [2,0,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    ]
def arrayToDrawing():
    y1=40
    y2=70
    for i in grid:
        x1=0
        x2=30
        for n in i:
            if n==0:
                canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline="")
                canvas.create_image(x1, y1, image=coins,anchor="nw")
            elif n==2:
                canvas.create_rectangle(x1,y1,x2,y2,fill="pink")
                canvas.create_image(x1, y1, image=img, anchor="nw")
            elif n==3:
                canvas.create_image(x1, y1, image=anemy3, anchor="nw" )
            elif n==4:
                canvas.create_image(x1, y1, image=anemy4, anchor="nw" )
            elif n==5:
                canvas.create_image(x1, y1, image=anemy5, anchor="nw" )
            elif n==6:
                canvas.create_image(x1, y1, image=anemy6, anchor="nw" )
            else:
                canvas.create_image(x1,y1,image=myImage,anchor="nw")
            x1=x2
            x2+=30
        y1=y2
        y2+=30
arrayToDrawing()

#####getIndex1

def getIndex1(grid):
    arr = []
    for i in range(len(grid)):
        value = grid[i]
        for j in range(len(value)):
            if grid[i][j] == 1:
                arr.append(i)
                arr.append(j)
                return arr

#####move right

def moveRight(event):
    global grid
    arrayOfindex1 = getIndex1(grid)
    i = arrayOfindex1[0]
    j = arrayOfindex1[1]
    if j+1 < len(grid[0]):
        grid[i][j] = 0
        grid[i][j+1] = 1
    arrayToDrawing()
    print(grid)

#####move left

def moveLeft(event):
    global grid
    arrayOfindex1 = getIndex1(grid)
    i = arrayOfindex1[0]
    j = arrayOfindex1[1]
    if j-1 >= 0:
        grid[i][j] = 0
        grid[i][j-1] = 1
    arrayToDrawing()
    print(grid)

#####move 

def moveDown(event):
    global grid
    arrayOfindex1 = getIndex1(grid)
    i = arrayOfindex1[0]
    j = arrayOfindex1[1]
    if i+1 < len(grid):
        grid[i][j] = 0
        grid[i+1][j] = 1
    arrayToDrawing()
    print(grid)

#####move up

def moveUp(event):
    global grid
    arrayOfindex1 = getIndex1(grid)
    i = arrayOfindex1[0]
    j = arrayOfindex1[1]
    if i-1 >= 0:
        grid[i][j] = 0
        grid[i-1][j] = 1
    arrayToDrawing()
    print(grid)


    
#####button

arrayToDrawing()
root.bind('<Right>', moveRight)
root.bind('<Left>', moveLeft)
root.bind('<Down>', moveDown)
root.bind('<Up>', moveUp)

canvas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')
root.mainloop()