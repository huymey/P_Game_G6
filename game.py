
import tkinter as tk
from tkinter import font
from tkinter.constants import COMMAND
import winsound
root=tk.Tk()
root.geometry("1800x1000")
frame=tk.Frame()
frame.master.title("Welcome Pacman Game")
canvas=tk.Canvas(frame)


#------------------------------------------Draw grid-----------------------------
grid=[
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,5,7,7,7,7,7,7,7,7,7,7,0,0,0,7,7,7,7,7,7,7,7,7,7,7,7,2],
    [2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,2],
    [2,7,2,7,7,7,7,7,7,7,0,7,0,7,0,7,7,7,0,7,7,7,7,7,7,7,7,7,0,7,7,7,7,7,7,7,7,7,7,0,2,0,2],
    [2,7,2,7,2,7,7,7,7,0,7,7,0,7,7,7,0,7,7,7,7,7,7,7,7,7,7,7,0,7,7,7,7,7,7,7,7,7,7,7,2,0,2],
    [2,7,2,7,2,7,7,0,7,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,0,0,0,5,0,0,0,0,7,7,7,7,7,2,0,2],
    [2,7,2,7,2,7,7,7,7,7,7,7,7,0,0,5,0,0,0,0,7,7,2,2,2,2,2,2,2,2,2,2,2,2,2,7,7,7,7,7,2,0,2],
    [2,0,2,7,2,7,7,7,7,7,7,7,7,2,2,2,2,2,2,2,7,7,7,7,7,7,7,0,7,7,0,7,7,7,7,7,7,7,7,7,2,7,2],
    [2,0,2,7,2,7,7,0,0,0,0,0,0,0,0,0,0,7,7,7,7,7,7,7,7,7,7,2,2,2,2,2,2,2,2,2,2,2,7,7,2,0,2],
    [2,0,2,7,2,7,7,2,2,2,2,2,2,2,2,2,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,2,0,2],
    [2,5,2,7,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,0,0,5,7,7,7,7,2,2,2,2,2,2,0,2],
    [2,0,2,7,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,2,2,2,2,2,2,2,2,7,7,7,7,7,7,7,7,7,2,0,2],
    [2,0,2,7,2,5,7,7,0,0,0,0,0,0,0,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,7,2],
    [2,0,2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,2,7,2],
    [2,0,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,7,2],
    [2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,2],
    [2,7,7,7,7,7,0,0,0,0,0,7,7,0,0,0,0,7,7,7,7,1,7,7,7,7,7,7,7,7,0,0,0,0,7,7,7,7,7,7,7,7,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    ]


def arrayToDrawing():
    global isTrue
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg, anchor='nw')
    y1=30
    y2=60
    if not isTrue and scoreOfCoin<20:
        for index in grid:
            x1=30
            x2=60
            for number in index:
                if number==0:
                    canvas.create_image(x1, y1, image=coins,anchor="nw")
                elif number==1:
                    canvas.create_image(x1,y1,image=myImage,anchor="nw")
                elif number==2:
                    canvas.create_rectangle(x1,y1,x2,y2,fill="")
                    canvas.create_image(x1, y1, image=img, anchor="nw")
                elif number==5:
                    canvas.create_image(x1, y1, image=anemy6, anchor="nw" )
                elif number==7:
                    canvas.create_rectangle(x1,y1,x2,y2,fill="",outline="")
                x1=x2
                x2+=30
            y1=y2
            y2+=30
    else:
        status()

#-----------------------------------score and numberoflife--------------------------


    canvas.create_text(130,75,fill="black",font="Times 16 italic bold",text="Score: "+str(scoreOfCoin))
    canvas.create_text(600,75,fill="black",font="Times 16 italic bold",text="You have: "+str(numberOfLife)+" life")


#####------------------------------set position getIndex1--------------------------

def getIndex1(grid):
    arr = []
    for row in range(len(grid)):
        value = grid[row]
        for col in range(len(value)):
            if grid[row][col] == 1:
                arr.append(row)
                arr.append(col)
                return arr

#####---------------------------------event for moveright user-----------------------

def moveRight(event):
    global grid,scoreOfCoin,isTrue,numberOfLife
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if col+1 < len(grid[0]) and grid[row][col+1]!=2 and grid[row][col+1]!=0 and grid[row][col+1]!=5:
        grid[row][col] = 7
        grid[row][col+1] = 1
        arrayToDrawing()
    elif grid[row][col+1]!=2 and grid[row][col+1]==0 and not isTrue:
        grid[row][col] = 7
        grid[row][col+1] = 1
        scoreOfCoin+=1  
        winsound.PlaySound('sound/coin4.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)    
        arrayToDrawing()
        if scoreOfCoin==20:
            isTrue=True
            status()
            winsound.PlaySound('sound/win.wav', winsound.SND_FILENAME|winsound.SND_ASYNC) 
    elif  grid[row][col+1]!=2 and grid[row][col+1]==5 and not isTrue:
        grid[row][col] = 7
        grid[row][col+1] = 1
        numberOfLife-=1
        winsound.PlaySound('sound/die.wav', winsound.SND_FILENAME|winsound.SND_ASYNC) 
        arrayToDrawing()
        if numberOfLife==0:
            isTrue=True
            status()
            winsound.PlaySound('sound/gameover1.wav', winsound.SND_FILENAME|winsound.SND_ASYNC) 
        
    print(grid)

#####-------------------------------event for moveleft user----------------------

def moveLeft(event):
    global grid,scoreOfCoin,isTrue,numberOfLife
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if col-1 >= 0 and grid[row][col-1]!=2 and grid[row][col-1]!=0 and grid[row][col-1]!=5:
        grid[row][col] = 7
        grid[row][col-1] = 1
        arrayToDrawing()
    elif grid[row][col-1]!=2 and grid[row][col-1]==0 and not isTrue:
        grid[row][col] = 7
        grid[row][col-1] = 1
        scoreOfCoin+=1
        winsound.PlaySound('sound/coin4.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
        arrayToDrawing()
        if scoreOfCoin==20:
            isTrue=True
            status()
    elif grid[row][col-1]!=2 and grid[row][col-1]==5 and not isTrue:
        grid[row][col] = 7
        grid[row][col-1] = 1
        numberOfLife-=1
        winsound.PlaySound('sound/die.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
        arrayToDrawing()
        if numberOfLife==0:
            isTrue=True
            status()  
    print(grid)

#####------------------------------event for moveDown user------------------------

def moveDown(event):
    global grid,scoreOfCoin,isTrue,numberOfLife
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if row+1 < len(grid) and grid[row+1][col]!=2 and grid[row+1][col]!=0 and grid[row+1][col]!=5:
        grid[row][col] = 7
        grid[row+1][col] = 1
        arrayToDrawing()
    elif grid[row+1][col]!=2 and grid[row+1][col]==0 and not isTrue:
        grid[row][col] = 7
        grid[row+1][col] = 1
        scoreOfCoin+=1
        winsound.PlaySound('sound/coin4.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
        arrayToDrawing()
        if scoreOfCoin==20:
            isTrue=True
            status()
    elif grid[row+1][col]!=2 and grid[row+1][col]==5 and not isTrue:
        grid[row][col] = 7
        grid[row+1][col] = 1
        numberOfLife-=1
        winsound.PlaySound('sound/die.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
        arrayToDrawing()
        if numberOfLife==0:
            isTrue=True
            status()  
    print(grid)

#####-------------------------------event for moveUp user-------------------

def moveUp(event):
    global grid,scoreOfCoin,isTrue,numberOfLife
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if row-1 >= 0 and grid[row-1][col]!=2 and grid[row-1][col]!=0 and grid[row-1][col]!=5:
        grid[row][col] = 7
        grid[row-1][col] = 1
        arrayToDrawing()
    elif grid[row-1][col]!=2 and grid[row-1][col]==0 and not isTrue:
        grid[row][col] = 7
        grid[row-1][col] = 1
        scoreOfCoin+=1
        winsound.PlaySound('sound/coin4.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
        arrayToDrawing()
        if scoreOfCoin==20:
            isTrue=True
            status() 
    elif grid[row-1][col]!=2 and grid[row-1][col]==5 and not isTrue:
        grid[row][col] = 7
        grid[row-1][col] = 1
        numberOfLife-=1
        winsound.PlaySound('sound/die.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
        arrayToDrawing()
        if numberOfLife==0:
            isTrue=True
            status()
    print(grid)


#---------------------------------create window for win / lost--------------------
def status():
    global scoreOfCoin,numberOfLife
    if scoreOfCoin==20:
        canvas.create_text(500,400,text="YOU WIN !",font=("Pursia",30,"bold"))
    elif numberOfLife==0:
        canvas.create_text(500,400,text="YOU LOST !",font=("Pursia",30,"bold"))
    canvas.create_window(500,500,window=buttonExit)
    canvas.create_window(800,500,window=buttonRestart)


## ---------------------------------Button Start Game-------------------
x1=100
y1=100
def startGame():
    arrayToDrawing()
    button_start.pack_forget()
button_start=tk.Button( root,text="Start Play",font=("Times",40) ,command=startGame)
canvas.create_window(600,400,window=button_start)



#---------------------------------------button exit-----------------------------------
def exit():
    root.destroy()
buttonExit=tk.Button(text="EXIT",font=("Pursia",20,"bold"),bg="blue",padx=20,pady=12,command=exit)


#--------------------------------------button restart-------------------------------
def restart():
    arrayToDrawing()
    buttonRestart.packt_forget()
buttonRestart=tk.Button(root,text="play",font=("Pursia",20,"bold"),bg="blue",padx=20,pady=12,command=restart)




####--------------------------------------Add image---------------------------------



myImage= tk.PhotoImage(file='images/player.png')
img=tk.PhotoImage(file="images/walls.png")
anemy6=tk.PhotoImage(file='images/enyme6.png')
coins=tk.PhotoImage(file='images/coin.png')
life=tk.PhotoImage(file='images/life.png')
bg=tk.PhotoImage(file='images/bg.png')
canvas.create_image(0, 0, image=bg, anchor='nw')


#------------------------------------//variblel globla//--------------------

numberOfLife=3
scoreOfCoin=0
topScore=173
isTrue=False

#------------------------------------event for move game-------------------
root.bind('<Right>', moveRight)
root.bind('<Left>', moveLeft)
root.bind('<Down>', moveDown)
root.bind('<Up>', moveUp)
# -------------------------------------button-------------------------------------------------
canvas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')
root.mainloop()