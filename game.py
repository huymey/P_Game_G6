

import tkinter as tk
root=tk.Tk()
root.geometry("600x600")
frame=tk.Frame()
frame.master.title("Welcome Pacman Game")
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
    [2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2],
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
ScoreOfCoin=0
StepOfMoving=1

def arrayToDrawing():
    canvas.delete("all")
    y1=40
    y2=70
    for index in grid:
        x1=0
        x2=30
        for number in index:
            if number==0:
                canvas.create_image(x1, y1, image=coins,anchor="nw")
            elif number==7:
                canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline="")
                
            elif number==2:
                canvas.create_rectangle(x1,y1,x2,y2,fill="pink")
                canvas.create_image(x1, y1, image=img, anchor="nw")
            elif number==3:
                canvas.create_image(x1, y1, image=anemy3, anchor="nw" )
            elif number==4:
                canvas.create_image(x1, y1, image=anemy4, anchor="nw" )
            elif number==5:
                canvas.create_image(x1, y1, image=anemy5, anchor="nw" )
            elif number==6:
                canvas.create_image(x1, y1, image=anemy6, anchor="nw" )
            elif number==1:
                canvas.create_image(x1,y1,image=myImage,anchor="nw")
            x1=x2
            x2+=30
        y1=y2
        y2+=30
    canvas.create_text(40,20,fill="black",font="Times 16 italic bold",text="Score: "+str(ScoreOfCoin))
    canvas.create_text(200,20,fill="black",font="Times 16 italic bold",text="Level: "+str(StepOfMoving))
    return None
arrayToDrawing()


## Create score  and Level to tasbar



#####getIndex1

def getIndex1(grid):
    arr = []
    for row in range(len(grid)):
        value = grid[row]
        for col in range(len(value)):
            if grid[row][col] == 1:
                arr.append(row)
                arr.append(col)
                return arr

#####move right

def moveRight(event):
    global grid
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if col+1 < len(grid[0]) and grid[row][col+1]!=2:
        grid[row][col] = 7
        grid[row][col+1] = 1
    arrayToDrawing()
    print(grid)

#####move left

def moveLeft(event):
    global grid
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if col-1 >= 0 and grid[row][col-1]!=2 :
        grid[row][col] = 7
        grid[row][col-1] = 1
    arrayToDrawing()
    print(grid)

#####move 

def moveDown(event):
    global grid
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if row+1 < len(grid) and grid[row+1][col]!=2:
        grid[row][col] = 7
        grid[row+1][col] = 1
    arrayToDrawing()
    print(grid)

#####move up

def moveUp(event):
    global grid
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if row-1 >= 0 and grid[row-1][col]!=2:
        grid[row][col] = 7
        grid[row-1][col] = 1
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