from tkinter import *
import tkinter.messagebox as tmsg
import random
import time
root=Tk()
global colors,fgc
colors=["red","white","black","yellow","cyan"]
fgc=["red","white","black","yellow","cyan"]

root.config(bg="chocolate")


head=Label(root,text="Color Name Pickers",bd=5,relief=SUNKEN,fg="white",bg="cyan",font="santia 15 bold")
head.pack(side="top",fill="both")
frame_rules=Frame(root,height=400,width=200,bg="white")
frame_rules.pack(fill="both")
rules=Label(master=frame_rules,text="Here are the rules",bg="white",fg="green",font="santia 12 bold")
rules.pack()
rules1=Label(master=frame_rules,text="1.Enter the background color of the text\n\n2.You have 60 seconds to play the game.",bg="white",fg="black",font="santia 8")
rules1.pack(side="left")

Game=Frame(root,bg="skyblue",height=1200,width=1200,relief=SUNKEN,bd=4)
Game.place(x=0,y=400)
global label
label=Label(master=Game,text="Score ",bg="skyblue",fg="red",font="santia 9 bold").place(x=0,y=0)
global count
count=0
global value,tried
value=60
tried=0
#Creating the functuins
def tim():
	global value,tried,count
	if value<60:
			label=Label(master=Game,text=value,bg="skyblue",fg="white",font="santia 9 bold").place(x=450,y=0)
	if value<=30:
		label=Label(master=Game,text=value,bg="skyblue",fg="orange",font="santia 9 bold").place(x=450,y=0)
	if value<10:
		label=Label(master=Game,text=value,bg="skyblue",fg="red",font="santia 9 bold").place(x=450,y=0)
	if value<0:
			l3=Label(master=Game,text="Times Up",bg="skyblue",fg="red",font="times 17 bold").place(x=410,y=300)
			label=Label(master=Game,text="0",bg="skyblue",fg="red",font="santia 9 bold").place(x=450,y=0)
			tmsg.showinfo("Result",f"Total Played-{count+tried}\nScore:{count}\nFailed:{tried}")
			root.quit
			return
		
	value=value-1
	gap()
#for calling times
def gap():
	root.after(1000,tim)
#play function startjng game	
def begin():
	global b3
	b3.config(state=DISABLED)
	game()
	tim()

	

	

	
#to reset the game	
def reset():
	global e1
	e1.delete(0,END)
#to check the answers	
def submit():
	global b,e1,count,b4,tried
	if b==e1.get():
		l3=Label(master=Game,text=" ",bg="skyblue",fg="red",width=20,font="times 17 bold").place(x=410,y=300)
		count+=1
		label=Label(master=Game,text=(f"Score {count}"),bg="skyblue",fg="red",font="santia 9 bold").place(x=0,y=0)
		e1.insert(0,a)
		game()
		
	else:
		l3=Label(master=Game,text="Please Try Again",bg="skyblue",fg="red").place(x=410,y=300)
		tried+=1
		if tried==3:
			b4.config(state=ACTIVE)
		
		
		e1.delete(0,END)
	
		

				
#for clicking next
def next():
	game()
	

def game():
	global e1,text,words,colors,a,b,fgc
	a=random.choice(colors)
	b=random.choice(fgc)

	e1=Entry(master=Game,bd=5,width=42,bg="white",font="times 14")
	e1.place(x=10,y=380)
	
	b1=Button(master=Game,text="Reset",activebackground="powderblue",background="powderblue",bd=5,relief=SUNKEN,width=5,command=reset)
	b1.place(x=50,y=550)
	
	b2=Button(master=Game,text="Submit",activebackground="powderblue",background="powderblue",bd=5,relief=SUNKEN,width=5,command=submit)
	b2.place(x=400,y=550)
	global b4
	b4=Button(master=Game,text="Next",activebackground="powderblue",background="powderblue",bd=5,relief=SUNKEN,width=5,command=next)
	b4.place(x=800,y=550)
	b4.config(state=DISABLED)
	
	words=Label(master=Game,text=a,bg="skyblue",fg=b,font="times 12 bold",width=8).place(x=390,y=200)
	
	
	

global b3
b3=Button(root,text="Play",activebackground="powderblue",background="powderblue",bd=5,relief=SUNKEN,width=15,command=begin)
b3.place(x=300,y=1200)
b4=Button(root,text="Quit",activebackground="powderblue",background="powderblue",bd=5,relief=SUNKEN,width=15,command=root.quit)
b4.place(x=300,y=1400)


root.mainloop()