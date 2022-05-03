from tkinter import *
root=Tk() 
root.title('HANGMAN : THE GAME') 
root.config(bg="Red")
root.geometry("1000x800")


def onclick(): 
    global guessing_box_1,guessing_box_2,guessing_box_3,guessing_box_4,guessing_box_5,guessing_box_6,guessing_box_7,guessing_box_8,guessing_box_9,guessing_box_10,letters
    l1.config(text="LET THE GUESSING BEGIN!!!",bg="green yellow")
    clue.destroy() 
    helpclue=Label(root,text="CLUE: "+clue_box.get(),font="BOLD",bg="firebrick2")
    helpclue.pack()
    clue_box.destroy()
    if len(word.get())<=5 or len(word.get())>10: 
        clue.after(100,lambda : l1.config(text="Please enter a new word with more than 5 letters"))
        helpclue.destroy() 
        click.destroy() 
        word.destroy()
        l1.destroy()
        start()
    else: 
        guessing_box_1=Entry(root,width=2,font=("Ariel",25)) 
        guessing_box_2=Entry(root,width=2,font=("Ariel",25))
        guessing_box_3=Entry(root,width=2,font=("Ariel",25))
        guessing_box_4=Entry(root,width=2,font=("Ariel",25))
        guessing_box_5=Entry(root,width=2,font=("Ariel",25))
        guessing_box_6=Entry(root,width=2,font=("Ariel",25))
        guessing_box_7=Entry(root,width=2,font=("Ariel",25))
        guessing_box_8=Entry(root,width=2,font=("Ariel",25))
        guessing_box_9=Entry(root,width=2,font=("Ariel",25))
        guessing_box_10=Entry(root,width=2,font=("Ariel",25))
        guessing_box_1.pack(side=LEFT,expand=True)
        guessing_box_2.pack(side=LEFT,expand=True)
        guessing_box_3.pack(side=LEFT,expand=True)
        guessing_box_4.pack(side=LEFT,expand=True)
        guessing_box_5.pack(side=LEFT,expand=True)
        guessing_box_6.pack(side=LEFT,expand=True)
        if len(word.get())==7:
            guessing_box_7.pack(side=LEFT,expand=True)
        if len(word.get())==8:
            guessing_box_7.pack(side=LEFT,expand=True)
            guessing_box_8.pack(side=LEFT,expand=True)
        if len(word.get())==9:
            guessing_box_7.pack(side=LEFT,expand=True)
            guessing_box_8.pack(side=LEFT,expand=True)
            guessing_box_9.pack(side=LEFT,expand=True)
        if len(word.get())==10:
            guessing_box_7.pack(side=LEFT,expand=True)
            guessing_box_8.pack(side=LEFT,expand=True)
            guessing_box_9.pack(side=LEFT,expand=True)
            guessing_box_10.pack(side=LEFT,expand=True) 
        letters=word.get()
        click.destroy()
        word.destroy()
        aftersubmission()


def start(): 
    global l1,word,clue,clue_box,click
    l1=Label(root,text="Enter a word for the game to begin",font="BOLD",bg="Orange")
    l1.pack()
    word=Entry(root)
    word.pack()
    clue=Label(root,text="Enter a clue for the word put up",font="BOLD",bg="Green")
    clue.pack()
    clue_box=Entry(root)
    clue_box.pack()
    click=Button(root,text="SUBMIT",command=onclick,bg="cyan") 
    click.pack() 
start() 


def aftersubmission(): 
    global letterentrylabel
    letterentrylabel=Label(root,text="Enter the letters one by one",font="BOLD",bg="yellow")
    letterentrylabel.pack()
    keyboard()


count=7 
def keyboard(): 
    global l,displaycount
    A=Button(root,text='A',command=lambda:keyonclick("A")) 
    B=Button(root,text='B',command=lambda:keyonclick("B")) 
    C=Button(root,text='C',command=lambda:keyonclick("C")) 
    D=Button(root,text='D',command=lambda:keyonclick("D"))
    E=Button(root,text='E',command=lambda:keyonclick("E"))
    F=Button(root,text='F',command=lambda:keyonclick("F"))
    G=Button(root,text='G',command=lambda:keyonclick("G"))
    H=Button(root,text='H',command=lambda:keyonclick("H"))
    I=Button(root,text='I',command=lambda:keyonclick("I"))
    J=Button(root,text='J',command=lambda:keyonclick("J"))
    K=Button(root,text='K',command=lambda:keyonclick("K"))
    L=Button(root,text='L',command=lambda:keyonclick("L"))
    M=Button(root,text='M',command=lambda:keyonclick("M"))
    N=Button(root,text='N',command=lambda:keyonclick("N"))
    O=Button(root,text='O',command=lambda:keyonclick("O"))
    P=Button(root,text='P',command=lambda:keyonclick("P"))
    Q=Button(root,text='Q',command=lambda:keyonclick("Q"))
    R=Button(root,text='R',command=lambda:keyonclick("R"))
    S=Button(root,text='S',command=lambda:keyonclick("S"))
    T=Button(root,text='T',command=lambda:keyonclick("T"))
    U=Button(root,text='U',command=lambda:keyonclick("U"))
    V=Button(root,text='V',command=lambda:keyonclick("V"))
    W=Button(root,text='W',command=lambda:keyonclick("W"))
    X=Button(root,text='X',command=lambda:keyonclick("X"))
    Y=Button(root,text='Y',command=lambda:keyonclick("Y"))
    Z=Button(root,text='Z',command=lambda:keyonclick("Z"))
    l=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z] 
    for button in l:
        button.pack(side=TOP,fill=BOTH)
    displaycount=Label(root,text=count,font="BOLD",bg="lawn green")
    displaycount.pack()


def display(): 
    global victory
    for boxes in guessingboxes:
        boxes.destroy()
    for let in l: 
        let.destroy() 
    victory=Label(root,text="CONGRATS YOU HAVE FOUND THE WORD!!!!",font="BOLD",bg="gold")
    if count!=0:
        victory.pack()
    Label(root,text="The correct word was "+letters.upper(),font="BOLD",bg="dodger blue").pack()
    l1.destroy()
    letterentrylabel.destroy()
    again()



c=0
alphabetlist=[str(chr(alphabet)) for alphabet in range(65,91)] 
def keyonclick(text): 
    l1=list(letters.upper()) 
    for button in l:
        if button.cget('text')==text: 
            if button.cget('text') in l1:
                button.config(bg="deep sky blue") 
            else:
                button.config(bg='orange red') 
    global guessingboxes,c,count
    if text in l1: 
        if text in l1[0] and len(guessing_box_1.get())!=1: 
            guessing_box_1.insert(0,text)
            c=c+1
        if text in l1[1] and len(guessing_box_2.get())!=1:
            guessing_box_2.insert(0,text)
            c=c+1
        if text in l1[2] and len(guessing_box_3.get())!=1:
            guessing_box_3.insert(0,text)
            c=c+1
        if text in l1[3] and len(guessing_box_4.get())!=1:
            guessing_box_4.insert(0,text)
            c=c+1
        if text in l1[4] and len(guessing_box_5.get())!=1:
            guessing_box_5.insert(0,text)
            c=c+1
        if text in l1[5] and len(guessing_box_6.get())!=1:
            guessing_box_6.insert(0,text)
            c=c+1
        if len(l1)>=7 and text in l1[6] and len(guessing_box_7.get())!=1:
            guessing_box_7.insert(0,text)
            c=c+1
        if len(l1)>=8 and text in l1[7] and len(guessing_box_8.get())!=1:
            guessing_box_8.insert(0,text)
            c=c+1
        if len(l1)>=9 and text in l1[8] and len(guessing_box_9.get())!=1:
            guessing_box_9.insert(0,text)
            c=c+1
        if len(l1)==10 and text in l1[9] and len(guessing_box_10.get())!=1:
            guessing_box_10.insert(0,text)
            c=c+1
    else: 
        if text in alphabetlist: 
            count=count-1
        displaycount.config(text=count)
    if text in alphabetlist: 
        alphabetlist.pop(alphabetlist.index(str(text)))
    if c==len(l1) or count==0: 
        guessingboxes=[guessing_box_1,guessing_box_2,guessing_box_3,guessing_box_4,guessing_box_5,guessing_box_6,guessing_box_7,guessing_box_8,guessing_box_9,guessing_box_10]
        display()

def again():
    victory.config(root,text='Do you want to play the game again?',font='Bold',bg='Green')
    victory.pack()

    

root.mainloop()