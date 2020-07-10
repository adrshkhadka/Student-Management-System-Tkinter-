import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
window = tk.Tk()
window.title("Registration form")
img=Image.open("C:/Users/acer/Downloads/bg_image.jpg")
photo=ImageTk.PhotoImage(img)
p=tk.Label(image=photo)
p.pack()

background_logo=ImageTk.PhotoImage(Image.open("C:/Users/acer/Downloads/man.png"))
bg_frame=tk.Frame(window,bg='orange')
bg_frame.place(x=620,y=100)
bg_label=tk.Label(bg_frame,image=background_logo)
bg_label.grid(column=10,row=5)

l1 = tk.Label(window,text='Registration',relief='groove',bg='pink',fg='blue',font=('arial bold',40),width=20,bd=10)
l1.place(x=450,y=0)

l2=tk.Label(window,text='First_name: ',font=('ariel bold',20),width=9)
l2.place(x=150,y=400)

l3=tk.Label(window,text='last_name: ',font=20)
l3.place(x=1050,y=400)

f_name=tk.StringVar()
entry_1=tk.Entry(window,textvariable=f_name,width=9,font=('Calibri Light',20))
entry_1.place(x=350,y=400)

l_name=tk.StringVar()
entry_2=tk.Entry(window,textvariable=l_name,width=9,font=('Calibri Light',20))
entry_2.place(x=1200,y=400)

l4=tk.Label(window,text='D.O.B:',font=('arial bold',20),width=9)
l4.place(x=150,y=500)

dob1=tk.StringVar()
dob=tk.Entry(window,textvariable=dob1,width=9,font=('Calibri Light',20))
dob.place(x=350,y=500)

l5=tk.Label(window,text='Country:',font=('arial bond',20),width=9)
l5.place(x=1050,y=500)

l6=tk.Label(window,text='Language: ',font=('arial bond',20),width=9)
l6.place(x=150,y=600)

con=tk.StringVar()
coun=ttk.Combobox(window,textvariable=con,width=12,font=('arial black',20))
coun['values']=('Nepal','India','Canada')
con.set('Select country')
coun.place(x=1250,y=500)

nep=tk.StringVar()
lang1=tk.Checkbutton(window,text='Nepali',font=9,variable=nep)
lang1.deselect()
lang1.place(x=350,y=600)

eng=tk.StringVar()
lang2=tk.Checkbutton(window,text='English',font=9,variable=eng)
lang2.deselect()
lang2.place(x=450,y=600)

gen=tk.StringVar()
l7=tk.Label(window,text='Gender:',font=20)
l7.place(x=1050,y=600)
radio1=tk.Radiobutton(window,text='Male',value='Male',font=20,variable=gen)
radio1.place(x=1150,y=600)
radio2=tk.Radiobutton(text="Female",value="Female",font=20,variable=gen)
radio2.place(x=1250,y=600)


def printing():
    first=f_name.get()
    last=l_name.get()
    date_of_b=dob1.get()
    country=con.get()
    gen1=gen.get()
    lang3=lang1
    lang3=lang2
    print(f"My full name is {first} {last}")
    print(f"My date of birth is {date_of_b}")
    print(f"My country name is {country}")
    print(f"My language is {lang3}")
    print(f"Your gender is {gen1}")
    tk.messagebox.showinfo('Welcome','You are sucessfully signed up.')


def new_window():
    window=tk.Tk()
    window.title("New Window")
    window.geometry('500x500+0+0')



b1=tk.Button(window,text='Login',bg='brown',fg='blue',command=new_window,width=12,font=20)
b1.place(x=700,y=700)

window.mainloop()


