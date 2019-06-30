from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#globle variable

ActivePlayer = 1
p1 = [] #What player one select
p2 = [] #What player two select

root = Tk()
root.title('Tic Tac Toe: Player1')

#add button
bt1 = ttk.Button(root, text = "")
bt1.grid(row = 0, column = 0, sticky = 'snew', ipadx = 40, ipady = 40)
bt1.config(command = lambda: ButClick(1))

bt2 = ttk.Button(root, text = "")
bt2.grid(row = 0, column = 1, sticky = 'snew', ipadx = 40, ipady = 40)
bt2.config(command = lambda: ButClick(2))

bt3 = ttk.Button(root, text = "")
bt3.grid(row = 0, column = 2, sticky = 'snew', ipadx = 40, ipady = 40)
bt3.config(command = lambda: ButClick(3))

bt4 = ttk.Button(root, text = "")
bt4.grid(row = 1, column = 0, sticky = 'snew', ipadx = 40, ipady = 40)
bt4.config(command = lambda: ButClick(4))

bt5 = ttk.Button(root, text = "")
bt5.grid(row = 1, column = 1, sticky = 'snew', ipadx = 40, ipady = 40)
bt5.config(command = lambda: ButClick(5))

bt6 = ttk.Button(root, text = "")
bt6.grid(row = 1, column = 2, sticky = 'snew', ipadx = 40, ipady = 40)
bt6.config(command = lambda: ButClick(6))

bt7 = ttk.Button(root, text = "")
bt7.grid(row = 2, column = 0, sticky = 'snew', ipadx = 40, ipady = 40)
bt7.config(command = lambda: ButClick(7))

bt8 = ttk.Button(root, text = "")
bt8.grid(row = 2, column = 1, sticky = 'snew', ipadx = 40, ipady = 40)
bt8.config(command = lambda: ButClick(8))

bt9 = ttk.Button(root, text = "")
bt9.grid(row = 2, column = 2, sticky = 'snew', ipadx = 40, ipady = 40)
bt9.config(command = lambda: ButClick(9))


def ButClick(id):
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(id,'X')
        p1.append(id)
        root.title('Tic Tac Toy: Player 2')
        ActivePlayer = 2
        #print(f'p1{p1}')
    elif(ActivePlayer==2) :
        SetLayout(id, 'O')
        p2.append(id)
        root.title('Tic Tac Toy: Player 1')
        ActivePlayer = 1
        #print(f'p2{p2}')
    CheckWinner()


def SetLayout(id,  PlayerSymbol):
    if id == 1:
        bt1.config(text = PlayerSymbol)
        bt1.state(['disabled'])

    elif id == 2:
        bt2.config(text = PlayerSymbol)
        bt2.state(['disabled'])

    elif id == 3:
        bt3.config(text = PlayerSymbol)
        bt3.state(['disabled'])

    elif id == 4:
        bt4.config(text = PlayerSymbol)
        bt4.state(['disabled'])

    elif id == 5:
        bt5.config(text = PlayerSymbol)
        bt5.state(['disabled'])

    elif id == 6:
        bt6.config(text = PlayerSymbol)
        bt6.state(['disabled'])

    elif id == 7:
        bt7.config(text = PlayerSymbol)
        bt7.state(['disabled'])

    elif id == 8:
        bt8.config(text = PlayerSymbol)
        bt8.state(['disabled'])

    elif id == 9:
        bt9.config(text=PlayerSymbol)
        bt9.state(['disabled'])

def CheckWinner():
    winner = -1
    if(( 1 in p1 ) and (2 in p1) and (3 in p1)):
        winner =1
    if (( 1 in p2) and (2 in p2) and (3 in p2)):
        winner = 2

    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winner = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winner = 2

    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winner = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winner = 2

    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winner = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winner = 2

    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winner = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winner = 2

    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winner = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winner = 2

    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner = 2

    if ((3 in p1) and (5 in p1) and (7 in p1)):
        winner = 1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        winner = 2

    if winner==1:
        messagebox.showinfo(title='congrats', message = 'Player 1 is winner')
    elif winner ==2:
        messagebox.showinfo(title='congrats', message='Player 2 is winner')


root.mainloop()