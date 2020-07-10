from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk


class Register:
    def __init__(self,window):
        self.window = window
        self.window.title("Registration Window")
        self.window.geometry('1500x1500+0+0')
        self.window.config(bg='sky blue')

        # ==== Background Image ====#

        self.bg=ImageTk.PhotoImage(file="C:/Users/acer/Downloads/bg_image.jpg")
        bg=Label(self.window,image=self.bg)
        bg.place(x=250,y=0,relwidth=1,relheight=1)

        # ===Left image=== #

        self.left=ImageTk.PhotoImage(file="C:/Users/acer/Downloads/blue img.jpg")
        left=Label(self.window,image=self.left)
        left.place(x=150,y=150,width=500,height=550)

        # Frame img===

        frame1=Frame(self.window,bg='pink')
        frame1.place(x=400,y=150,width=700,height=550)

        # ===Title

        title=Label(self.window,text='Register Here',font=('arail italic',25),bg='yellow',fg='green')
        title.place(x=650,y=175)

        # first name
        self.first_name=StringVar()
        self.f_name=Label(self.window,text='First Name',font=15)
        self.f_name.place(x=450,y=250)
        self.entry_f=Entry(self.window,bg='light gray',font=15,textvariable=self.first_name)
        self.entry_f.place(x=450,y=280,width=150)

        # last name
        last_name=StringVar()
        self.l_name=Label(self.window,text='Last Name',font=15)
        self.l_name.place(x=850,y=250)
        self.entry_l=Entry(self.window,bg='light gray',font=15,textvariable=last_name)
        self.entry_l.place(x=850,y=280,width=150)

        # contact number
        contact_num=StringVar()
        self.contact=Label(self.window,text='Contact No:',bg='white',font=15,)
        self.contact.place(x=450,y=350)
        self.entry_contact=Entry(self.window,bg='light gray',font=15,textvariable=contact_num)
        self.entry_contact.place(x=450,y=380,width=150)

        # e_mail
        Email=StringVar()
        self.email=Label(self.window,text='E_Mail',font=15)
        self.email.place(x=850,y=350)
        self.entry_email=Entry(self.window,bg='light gray',font=15,textvariable=Email)
        self.entry_email.place(x=850,y=380)

        # Security Question
        Question=StringVar()
        self.sec_ques=Label(self.window,text='Select Question',font=15)
        self.sec_ques.place(x=450 , y =450 )
        self.combo=ttk.Combobox(self.window,font=15,textvariable=Question,state='readonly',justify=CENTER)
        self.combo['values']=('Select','Your birth place','Your pet name','Your best friend name')
        self.combo.place(x=450,y=480)

        # Answer
        Answer=StringVar()
        self.ans=Label(self.window,text="Answer",font=15)
        self.ans.place(x=850,y=445)
        self.entry_ans=Entry(self.window,font=15,textvariable=Answer)
        self.entry_ans.place(x=850,y=470)

        # Password
        password=StringVar()
        self.passw=Label(self.window,text="Password",font=15)
        self.passw.place(x=450,y=540)

        self.entry_passw=Entry(self.window,font=15,show='*',textvariable=password)
        self.entry_passw.place(x=450,y=565)

        # Confirm password
        confirmation=StringVar
        self.confpass=Label(self.window,text='Confirm Password',font=15)
        self.confpass.place(x=850 ,y = 540 )
        self.entry_confpass=Entry(self.window,font=15,show='*',textvariable=confirmation)
        self.entry_confpass.place(x=850,y=565)

        # Terms and conditions
        self.cond=Checkbutton(self.window,text='I agree terms and conditions',font=15,bg='white')
        self.cond.place(x=450,y=600)

        # Register
        self.bt=ImageTk.PhotoImage(file="C:/Users/acer/Downloads/register img.png")
        button=Button(self.window,image=self.bt,cursor='hand2',height=28,width=150,bd=0,command=self.printing)
        button.place(x=650,y=650)

        # Signup

        self.signup=Button(self.window,text='Sign Up',font=20,bg='red')
        self.signup.place(x=250,y=500)
        self.exit=Button(self.window,text='Exit',font=20,bg='purple',command=exit)
        self.exit.place(x=250,y=650)

    def printing(self):
        print(self.first_name.get())

    def exit(self):
        exit()


window = Tk()
r1 = Register(window)
window.mainloop()