

import tkinter as tk
root=tk.Tk()
root.geometry("600x600")
frame=tk.Frame()
frame.master.title("Welcome Pacman Game")
canvas=tk.Canvas(frame)
# root.resizable(0,0)
####add image

myImage= tk.PhotoImage(file='images/player.png')
img=tk.PhotoImage(file="images/walls.png")
anemy5=tk.PhotoImage(file='images/Enyme5.png')
coins=tk.PhotoImage(file='images/Coins.png')
life=tk.PhotoImage(file='images/life.png')
####Data

# empty=0
# wall=2
# player=1
# coin=3
# monster=4

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
    [2,0,2,0,2,0,2,1,5,0,5,0,2,0,2,0,2,0,0,2],
    [2,0,2,0,0,0,2,0,0,5,0,5,2,0,0,0,2,0,0,2],
    [2,0,2,0,2,0,2,0,2,2,2,2,2,0,2,0,2,0,0,2],
    [2,0,2,0,2,0,2,0,0,0,0,0,0,0,2,0,2,0,0,2],
    [2,0,2,0,2,0,2,2,2,2,2,2,2,0,2,0,2,0,0,2],
    [2,0,2,0,2,0,0,0,0,0,0,0,0,0,2,0,2,0,0,2],
    [2,0,2,0,2,2,2,2,2,0,2,2,2,2,2,0,2,0,0,2],
    [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2],
    [2,0,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    ]
numberOfLife=3
ScoreOfCoin=0
topScore=173
IsTrue=False
def arrayToDrawing():
    canvas.delete("all")
    y1=0
    y2=30
    for index in grid:
        x1=0
        x2=30
        for number in index:
            if number==0:
                canvas.create_image(x1, y1, image=coins,anchor="nw")
            elif number==1:
                canvas.create_image(x1,y1,image=myImage,anchor="nw")
            elif number==2:
                canvas.create_rectangle(x1,y1,x2,y2,fill="pink")
                canvas.create_image(x1, y1, image=img, anchor="nw")
            elif number==5:
                canvas.create_image(x1, y1, image=anemy5, anchor="nw" )
            elif number==7:
                # grid-empty
                canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline="")
            # elif number==8:
            #     canvas.create_image(x1,y1,image=life,anchor="nw")
            #     print(x1,y1)
            x1=x2
            x2+=30
        y1=y2
        y2+=30
    
    canvas.create_text(90,45,fill="black",font="Times 16 italic bold",text="Score: "+str(ScoreOfCoin))
    canvas.create_text(300,45,fill="black",font="Times 16 italic bold",text="Level:  1")
    canvas.create_text(450,45,fill="black",font="Times 16 italic bold",text="You have: "+str(numberOfLife)+" life")
    
arrayToDrawing()


## Create score  and Level to tasbar
# status
def getStatus():
    if ScoreOfCoin==topScore:
        canvas.create_text(300,300,fill="black",font="Times 30 italic bold",text="You win!")
    elif numberOfLife==0: 
        canvas.create_text(300,300,fill="black",font="Times 30 italic bold",text="You lost!")
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
    global grid,ScoreOfCoin,IsTrue,numberOfLife
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if col+1 < len(grid[0]) and grid[row][col+1]!=2 and grid[row][col+1]!=0 and grid[row][col+1]!=5:
        grid[row][col] = 7
        grid[row][col+1] = 1
        arrayToDrawing()
    elif grid[row][col+1]!=2 and grid[row][col+1]==0 and not IsTrue:
        grid[row][col] = 7
        grid[row][col+1] = 1
        ScoreOfCoin+=1     
        arrayToDrawing()
        if ScoreOfCoin==173:
            IsTrue=True
            getStatus()
    elif  grid[row][col+1]!=2 and grid[row][col+1]==5 and not IsTrue:
        grid[row][col] = 7
        grid[row][col+1] = 1
        numberOfLife-=1
        arrayToDrawing()
        if numberOfLife==0:
            IsTrue=True
            getStatus()
    print(grid)

#####move left

def moveLeft(event):
    global grid,ScoreOfCoin,IsTrue,numberOfLife
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if col-1 >= 0 and grid[row][col-1]!=2 and grid[row][col-1]!=0 and grid[row][col-1]!=5:
        grid[row][col] = 7
        grid[row][col-1] = 1
        arrayToDrawing()
    elif grid[row][col-1]!=2 and grid[row][col-1]==0 and not IsTrue:
        grid[row][col] = 7
        grid[row][col-1] = 1
        ScoreOfCoin+=1
        arrayToDrawing()
        if ScoreOfCoin==173:
            IsTrue=True
            getStatus()
    elif grid[row][col-1]!=2 and grid[row][col-1]==5 and not IsTrue:
        grid[row][col] = 7
        grid[row][col-1] = 1
        numberOfLife-=1
        arrayToDrawing()
        if numberOfLife==0:
            IsTrue=True
            getStatus()  
    print(grid)

#####move 

def moveDown(event):
    global grid,ScoreOfCoin,IsTrue,numberOfLife
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if row+1 < len(grid) and grid[row+1][col]!=2 and grid[row+1][col]!=0 and grid[row+1][col]!=5:
        grid[row][col] = 7
        grid[row+1][col] = 1
        arrayToDrawing()
    elif grid[row+1][col]!=2 and grid[row+1][col]==0 and not IsTrue:
        grid[row][col] = 7
        grid[row+1][col] = 1
        ScoreOfCoin+=1
        arrayToDrawing()
        if numberOfLife==0:
            IsTrue=True
            getStatus()
    elif grid[row+1][col]!=2 and grid[row+1][col]==5 and not IsTrue:
        grid[row][col] = 7
        grid[row+1][col] = 1
        numberOfLife-=1
        arrayToDrawing()
        if numberOfLife==0:
            IsTrue=True
            getStatus()  
    print(grid)

#####move up

def moveUp(event):
    global grid,ScoreOfCoin,IsTrue,numberOfLife
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if row-1 >= 0 and grid[row-1][col]!=2 and grid[row-1][col]!=0 and grid[row-1][col]!=5:
        grid[row][col] = 7
        grid[row-1][col] = 1
        arrayToDrawing()
    elif grid[row-1][col]!=2 and grid[row-1][col]==0 and not IsTrue:
        grid[row][col] = 7
        grid[row-1][col] = 1
        ScoreOfCoin+=1
        arrayToDrawing()
        if ScoreOfCoin==173:
            IsTrue=True
            getStatus() 
    elif grid[row-1][col]!=2 and grid[row-1][col]==5 and not IsTrue:
        grid[row][col] = 7
        grid[row-1][col] = 1
        numberOfLife-=1
        arrayToDrawing()
        if numberOfLife==0:
            IsTrue=True
            getStatus()
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