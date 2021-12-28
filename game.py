
import tkinter as tk
from tkinter import Menu, font
from tkinter.constants import COMMAND
import winsound
root=tk.Tk()
root.geometry("1800x1000")
frame=tk.Frame()
frame.master.title("Project Game")
canvas=tk.Canvas(frame)

#_________________________________Draw grid_________________________________
grid=[
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,7,7,7,7,7,7,7,7,7,7,2],
    [2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,2],
    [2,7,2,7,7,7,7,7,7,7,0,7,0,7,0,7,7,7,0,7,7,7,7,7,7,7,7,7,0,7,7,7,7,7,7,7,7,7,7,0,2,0,2],
    [2,7,2,7,2,7,7,7,7,0,7,7,0,7,7,7,0,7,7,7,7,7,7,7,7,7,7,7,0,7,7,7,7,7,7,7,7,7,7,7,2,0,2],
    [2,7,2,7,2,7,7,0,7,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,0,0,0,5,0,0,0,0,7,7,7,7,7,2,0,2],
    [2,0,2,7,2,7,7,7,7,7,7,7,7,0,0,5,0,0,0,0,7,7,2,2,2,2,2,2,2,2,2,2,2,2,2,7,7,7,7,7,2,0,2],
    [2,0,2,7,2,7,7,7,7,7,7,7,7,2,2,2,2,2,2,2,7,7,7,7,7,7,7,0,7,7,0,7,7,7,7,7,7,7,7,7,2,7,2],
    [2,0,2,7,2,7,7,0,0,0,0,0,0,0,0,0,0,7,7,7,7,7,7,7,7,7,7,2,2,2,2,2,2,2,2,2,2,2,7,7,2,7,2],
    [2,0,2,7,2,7,7,2,2,2,2,2,2,2,2,2,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,2,0,2],
    [2,7,2,7,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,0,0,5,7,7,7,7,2,2,2,2,2,2,0,2],
    [2,0,2,7,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,2,2,2,2,2,2,2,2,7,7,7,7,7,7,7,7,7,2,0,2],
    [2,0,2,7,2,5,7,7,0,0,0,0,0,0,0,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,7,2],
    [2,0,2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,2,7,2],
    [2,0,2,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,7,0,0,0,0,0,7,7,7,7,7,7,7,7,7,7,7,7,7,2,7,2],
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
                    canvas.create_rectangle(x1,y1,x2,y2,fill="pink")
                    canvas.create_image(x1, y1, image=img, anchor="nw")
                elif number==5:
                    canvas.create_image(x1, y1, image=anemy6, anchor="nw" )
                elif number==7:
                    # grid-empty
                    canvas.create_rectangle(x1,y1,x2,y2,fill="",outline="")
                x1=x2
                x2+=30
            y1=y2
            y2+=30

#____________________________score and numoflife_________________________________

    canvas.create_text(130,75,fill="black",font="Times 16 italic bold",text="Score: "+str(scoreOfCoin))
    canvas.create_text(600,75,fill="black",font="Times 16 italic bold",text="You have: "+str(numberOfLife)+" life")
    

#####_________________________set position getIndex1_________________________________

def getIndex1(grid):
    arr = []
    for row in range(len(grid)):
        value = grid[row]
        for col in range(len(value)):
            if grid[row][col] == 1:
                arr.append(row)
                arr.append(col)
                return arr
#_____________________________event for move right left up and down_________________________________ 
def positionOfPlayer(position):
    global grid,scoreOfCoin,isTrue,numberOfLife
    arrayOfindex1 = getIndex1(grid)
    row = arrayOfindex1[0]
    col = arrayOfindex1[1]
    if col+1 < len(grid[0]) and grid[row][col+1]!=2 and grid[row][col+1]!=0 and grid[row][col+1]!=5 and position=="Right":
        grid[row][col] = 7
        grid[row][col+1] = 1
        arrayToDrawing()
    elif grid[row][col+1]!=2 and grid[row][col+1]==0 and not isTrue and position=="Right" :
        grid[row][col] = 7
        grid[row][col+1] = 1
        touchCoin()
        scoreOfCoin+=1  
        arrayToDrawing()
        if scoreOfCoin==10:
            isTrue=True
            win()
    elif  grid[row][col+1]!=2 and grid[row][col+1]==5 and not isTrue and position=="Right":
        grid[row][col] = 7
        grid[row][col+1] = 1
        numberOfLife-=1
        playerDie() 
        arrayToDrawing()
        if numberOfLife==0:
            isTrue=True
            lost()
    ####______________________________move left______________________________
    elif col-1 >= 0 and grid[row][col-1]!=2 and grid[row][col-1]!=0 and grid[row][col-1]!=5 and position=="Left":
        grid[row][col] = 7
        grid[row][col-1] = 1
        arrayToDrawing()
    elif grid[row][col-1]!=2 and grid[row][col-1]==0 and not isTrue and position=="Left":
        grid[row][col] = 7
        grid[row][col-1] = 1
        scoreOfCoin+=1
        touchCoin()
        arrayToDrawing()
        if scoreOfCoin==10:
            isTrue=True
            win()
    elif grid[row][col-1]!=2 and grid[row][col-1]==5 and not isTrue and position=="Left":
        grid[row][col] = 7
        grid[row][col-1] = 1
        numberOfLife-=1
        playerDie()
        arrayToDrawing()
        if numberOfLife==0:
            isTrue=True
            lost()
    #______________________________move down______________________________
    elif row+1 < len(grid) and grid[row+1][col]!=2 and grid[row+1][col]!=0 and grid[row+1][col]!=5 and position=="Down":
        grid[row][col] = 7
        grid[row+1][col] = 1
        arrayToDrawing()
    elif grid[row+1][col]!=2 and grid[row+1][col]==0 and not isTrue and position=="Down":
        grid[row][col] = 7
        grid[row+1][col] = 1
        scoreOfCoin+=1
        touchCoin()
        arrayToDrawing()
        if scoreOfCoin==10:
            isTrue=True
            win()
    elif grid[row+1][col]!=2 and grid[row+1][col]==5 and not isTrue and position=="Down":
        grid[row][col] = 7
        grid[row+1][col] = 1
        numberOfLife-=1
        playerDie()
        arrayToDrawing()
        if numberOfLife==0:
            isTrue=True
            lost()
    #______________________________move up_________________________________

    elif row-1 >= 0 and grid[row-1][col]!=2 and grid[row-1][col]!=0 and grid[row-1][col]!=5 and position=="Up":
        grid[row][col] = 7
        grid[row-1][col] = 1
        arrayToDrawing()
    elif grid[row-1][col]!=2 and grid[row-1][col]==0 and not isTrue and position=="Up":
        grid[row][col] = 7
        grid[row-1][col] = 1
        scoreOfCoin+=1
        touchCoin()
        arrayToDrawing()
        if scoreOfCoin==10:
            isTrue=True
            win()

    elif grid[row-1][col]!=2 and grid[row-1][col]==5 and not isTrue and position=="Up":
        grid[row][col] = 7
        grid[row-1][col] = 1
        numberOfLife-=1
        playerDie()
        arrayToDrawing()
        if numberOfLife==0:
            isTrue=True
            lost()
#_________________________________event for moveright user_________________________________
def moveRight(event):
    positionOfPlayer("Right")

#_________________________________event for moveleft user

def moveLeft(event):
        positionOfPlayer("Left")
#_________________________________event for moveDown user_________________________________

def moveDown(event):
        positionOfPlayer("Down")
#_________________________________event for moveUp user_________________________________

def moveUp(event):
    positionOfPlayer("Up")
    
# _________________________________display message win_________________________________

def win():
    global grid
    canvas.delete("all")
    canvas.create_image(650, 300, image=winnerImg)
    canvas.create_text(700,300,text="🙌YOU WIN🙌 !",font=("Pursia",30,"bold"))
    gameWin()

# _________________________________display message lost_________________________________
def lost():
    canvas.delete("all")
    canvas.create_image(650, 300, image=lostImg)
    canvas.create_text(700,300)
    gameOver()

##_________________________________Button Start Game_________________________________

def startGame():
    arrayToDrawing()
    button_start.pack_forget()
button_start=tk.Button( root,text="Start Play",font=("Times",40) ,command=startGame)
canvas.create_window(600,400,window=button_start)
winsound.PlaySound('sound/startgame.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)

#__________________________________________sound action____________
def touchCoin():
    winsound.PlaySound('sound/coin4.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
def playerDie():
    winsound.PlaySound('sound/die.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
def gameOver():
    winsound.PlaySound('sound/gameover1.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
def gameWin():
    winsound.PlaySound('sound/win.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)


#__________________________________________add image_________________
myImage= tk.PhotoImage(file='images/player.png')
img=tk.PhotoImage(file="images/walls.png")
anemy6=tk.PhotoImage(file='images/enyme6.png')
coins=tk.PhotoImage(file='images/coin.png')
bg=tk.PhotoImage(file='images/bg.png')
canvas.create_image(0, 0, image=bg, anchor='nw')
winnerImg = tk.PhotoImage(file="images/winner.png")
lostImg = tk.PhotoImage(file="images/lost.png")
#________________________________________variblel globla__________________

numberOfLife=3
scoreOfCoin=0
topScore=173
isTrue=False
isWon = True

#__________________________________event for move game_________________________________
root.bind('<Right>', moveRight)
root.bind('<Left>', moveLeft)
root.bind('<Down>', moveDown)
root.bind('<Up>', moveUp)
# _________________________________button_________________________________
canvas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')
root.mainloop()