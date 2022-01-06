from tkinter import *

root = Tk()

e=Entry(root, width=50,border=5,fg='red',bg='white')
e.pack()
e.get()
def myclick():
    myLabel=Label(root,text=e.get()).pack()
    

myButton=Button(root,text='Enter your name',command=myclick,fg='white',bg='red')
myButton.pack()

root.mainloop()   
