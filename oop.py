from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Login:
    def __init__(self, window):
        self.window = window
        self.window.title('Login')
        self.window.geometry('1600x1200')
        self.window.config(bg='white')
        #===Adding Topic===#
        self.main_topic=Label(self.window,text='Login Page',bg='white',fg='navyblue',font=('times new roman',40))
        self.main_topic.pack()
        #===Adding Frame===#
        self.frame1=Frame(self.window,bg='gray',bd=10)
        self.frame1.place(x=200,y=100,height=600,width=1200)
        # ===Frame1 work===#
        self.label1=Label(self.frame1,text='Login Here',bg='gray',fg='purple',font=('times new roman',30))
        self.label1.pack()
        # =Adding label in frame===#
        self.userlabel=Label(self.frame1,text='Username :',bg='gray',fg='black',font=('arial black',20))
        self.userlabel.place(x=250,y=200)
        self.passlabel=Label(self.frame1,text='Password :',font=('arial black',20),bg='gray',fg='black')
        self.passlabel.place(x=250,y=280)
        # === Adding Entry button === #
        self.userentry=Entry(self.frame1,bd=10)
        self.userentry.place(x=500,y=200,width=200,height=45)
        self.passentry = Entry(self.frame1,bd=10)
        self.passentry.place(x=500,y=280,width=200,height=45)
        #===Adding Login Button===#
        self.bt=Button(self.frame1,text='Login',font=('times new roman',20),bg='skyblue')
        self.bt.place(x=400,y=400,width=100,height=50)
        self.bt1=Button(self.frame1,text='Exit',font=('times new roman',20),bg='pink',fg='crimson',command=exit)
        self.bt1.place(x=520,y=400,width=100,height=51)

    def login(self):
        pass
        
    def exit(self):
        exit()




window = Tk()
l1 = Login(window)
window.mainloop()

