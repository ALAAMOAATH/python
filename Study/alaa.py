from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
root=Tk()
root.title('start game have fun ')
style=ttk.Style()
style.theme_use('classic')
style.configure('TButton',background='purple',foreground='black',font=('Comic Sans MS',20,'bold'))
#print(style.theme_names())


#creat b1
b1=ttk.Button(root,text='')
b1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40,)
b1.config(command=lambda :bclick(1))
#creat b2
b2=ttk.Button(root,text='')
b2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
b2.config(command=lambda :bclick(2))
#creat b3
b3=ttk.Button(root,text='')
b3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
b3.config(command=lambda :bclick(3))
#creat b4
b4=ttk.Button(root,text='')
b4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
b4.config(command=lambda :bclick(4))
#creat b5
b5=ttk.Button(root,text='')
b5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
b5.config(command=lambda :bclick(5))
#creat b6
b6=ttk.Button(root,text='')
b6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
b6.config(command=lambda :bclick(6))
#creat b7
b7=ttk.Button(root,text='')
b7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
b7.config(command=lambda :bclick(7))
#creat b8
b8=ttk.Button(root,text='')
b8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
b8.config(command=lambda :bclick(8))
#creat b9
b9=ttk.Button(root,text='')
b9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
b9.config(command=lambda :bclick(9))
style.configure('Tbutton',background='blue',foreground='gray',font=('Comic Sans MS'))#,10,'bold'))
def bclick(id):
 global ActivePlayer
 global p1
 global p2
 if(ActivePlayer==1):
  root.title('tic tac toe  : Player  1')
  SetLayout(id,'X')
  p1.append(id)
  root.title('tic tac toe  : Player  2')
  ActivePlayer=2
  CheckWinner()
  AutoPlay()
 elif(ActivePlayer==2):
  SetLayout(id,'O')
  p2.append(id)
 # root.title('tic tac toe  : Player  1')
  ActivePlayer=1
  CheckWinner()
def SetLayout(id,text):
 if(id==1):
  b1.config(text=text)
  #b1.state(['disabled'])
 elif(id==2):
  b2.config(text=text)
  #b2.state(['disabled'])
 elif (id == 3):
  b3.config(text=text)
  #b3.state(['disabled'])
 elif (id == 4):
  b4.config(text=text)
  #b4.state(['disabled'])
 elif(id==5):
  b5.config(text=text)
  #b5.state(['disabled'])
 elif (id == 6):
  b6.config(text=text)
  #b6.state(['disabled'])
 elif (id == 7):
  b7.config(text=text)
  #b7.state(['disabled'])
 elif (id == 8):
  b8.config(text=text)
  #b8.state(['disabled'])
 elif (id == 9):
  b9.config(text=text)
  #b9.state(['disabled'])
#check winner
def CheckWinner():
 Winner=-1
 #for first row
 if ((1 in p1) and (2 in p1) and (3 in p1)):
   Winner=1
 if ((1 in p2) and (2 in p2) and (3 in p2)):
   Winner=2
 #for second row
 if ((4 in p1) and (5 in p1) and (6 in p1)):
   Winner=1
 if ((4 in p2) and (5 in p2) and (6 in p2)):
   Winner=2
 #for third row
 if ((7 in p1) and (8 in p1) and (9 in p1)):
   Winner=1
 if ((7 in p2) and (8 in p2) and (9 in p2)):
   Winner=2
 #for first column
 if ((1 in p1) and (4 in p1) and (7 in p1)):
   Winner=1
 if ((1 in p2) and (4 in p2) and (7 in p2)):
   Winner=2
 #for second column
 if ((2 in p1) and (5 in p1) and (8 in p1)):
   Winner=1
 if ((2 in p2) and (5 in p2) and (8 in p2)):
   Winner=2
 #for third column
 if ((3 in p1) and (6 in p1) and (9 in p1)):
   Winner=1
 if ((3 in p2) and (6 in p2) and (9 in p2)):
   Winner=2
 if Winner==1:
  messagebox.showinfo(title='congraulation',message='Player 1 is winner')
 if Winner==2:
  messagebox.showinfo(title='congraulation',message='Player 2 is winner')
def AutoPlay():
 global p1
 global p2
 emptycell=[]
 for cell in range(9):
  if (not((cell+1 in p1)or (cell+1 in p2))):
   emptycell.append(cell+1)
 RandIndex=randint(0,len(emptycell)-1)
 bclick(emptycell[RandIndex])
root.mainloop()

