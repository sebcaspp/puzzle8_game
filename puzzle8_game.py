from tkinter import *

root = Tk() 
root.attributes('-type', 'dialog')
root.title("8-puzzle game")
root.configure(width=400, height=400)
        

frame: Frame = Frame(root) 
frame.configure(width=400, height=400)
frame.pack()

nx = 3
ny = 3

puzzle = [["","2","3"],["1","8","6"],["7","4","5"]]
goal = [["1","2","3"],["4","5","6"],["7","8",""]]

actualState = puzzle.copy()

buttons = [list(range(nx)) for i in range(ny)]
blankButton = (-1,-1)
movesCounter = 0

def disableButtons():
    for x in range(3):
        for y in range(3):
            buttons[x][y].config(state="disable")

def validateActiveBottons():
     disableButtons()    
     x,y = blankButton
     if x-1 >= 0: buttons[x-1][y].config(state="normal")
     if x+1 <  3: buttons[x+1][y].config(state="normal")
     if y-1 >= 0: buttons[x][y-1].config(state="normal")
     if y+1 <  3: buttons[x][y+1].config(state="normal")

def moveBlankButton(x,y):
    global blankButton    
    global movesCounter
    global actualState

    blankX,blankY = blankButton
    if blankX==-1: return

    actualPuzzleValue = buttons[x][y]['text']
    buttons[blankX][blankY].config(text=actualPuzzleValue)
    buttons[x][y].config(text="")
    blankButton = (x,y)
    validateActiveBottons()

    actualState[x][y]=""
    actualState[blankX][blankY]=actualPuzzleValue
    movesCounter+=1
    if goal==actualState:
        print("finalizado!!!")
    
def buttonCallback(x,y):
    return lambda : moveBlankButton(x,y)


for x in range(3):
    for y in range(3):
        puzzleValue = puzzle[x][y]    
        button:Button = Button(frame, text = puzzleValue, fg ='black', width=20,  height=15, command = buttonCallback(x,y) ) 
        button.config(state="disable")
        button.grid(row=x, column=y)
        buttons[x][y]=button
        if puzzleValue=="": 
            blankButton = (x,y)

validateActiveBottons()


root.mainloop()

print("number of moves: ", movesCounter)