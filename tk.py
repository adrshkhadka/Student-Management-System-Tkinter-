from tkinter import *
from tkinter import ttk
import pymysql


class Student:
    def __init__(self, window):
        self.window=window
        self.window.title("Student Information System")
        self.window.geometry('1700x1700+0+0')
        self.window.config(bg='navyblue')

        # === All variables === #
        self.Roll_no_Var = StringVar()
        self.Name_Var = StringVar()
        self.Email_Var = StringVar()
        self.Gender_Var = StringVar()
        self.Contact_Var = StringVar()
        self.Date_of_birth_Var = StringVar()
        self.Address_Var = StringVar()

        # ===Label for topic===#
        label=Label(self.window,text='Student Information System',font=('arial black',40,'bold'),bg='yellow',fg='purple',relief=RAISED,bd=10)
        label.pack(side=TOP,fill=X)

        # === Frame for manage students === #
        manage_frame=Frame(self.window,bg='crimson',bd=10)
        manage_frame.place(x=40,y=100,height=670,width=520)

        # === Label inside manage frame === #
        manage_label=Label(manage_frame,text='Manage Students',font=('times new roman',25),bg='crimson',fg='white')
        manage_label.pack()

        rollno=Label(manage_frame,text='Roll No.',font=('times new roman',20),bg='crimson',fg='white')
        rollno.place(x=20,y=60)

        name=Label(manage_frame,text='Name',font=('times new roman',20),bg='crimson',fg='white')
        name.place(x=20,y=120)

        email=Label(manage_frame,text='Email',font=('times new roman',20),bg='crimson',fg='white')
        email.place(x=20,y=180)

        gender=Label(manage_frame,text='Gender',font=('times new roman',20),bg='crimson',fg='white')
        gender.place(x=20,y=240)

        contact=Label(manage_frame,text='Contact No.',font=('time new roman',20),bg='crimson',fg='white')
        contact.place(x=20,y=300)

        dob=Label(manage_frame,text='D.O.B',font=('times new roman',20),bg='crimson',fg='white')
        dob.place(x=20,y=360)

        address=Label(manage_frame,text='Address',font=('times new roman',20),bg='crimson',fg='white')
        address.place(x=20,y=360)

        # ===Entry for all labels === #
        self.entry_roll=Entry(manage_frame,textvariable=self.Roll_no_Var,font=('times new roman',20),bg='lightgray',bd=5)
        self.entry_roll.place(x=200,y=60)

        self.entry_name=Entry(manage_frame,textvariable=self.Name_Var,font=('times new roman',20),bg='lightgray',bd=5)
        self.entry_name.place(x=200,y=120)

        self.entry_email=Entry(manage_frame,textvariable=self.Email_Var,font=('times new roman',20),bg='lightgray',bd=5)
        self.entry_email.place(x=200,y=180)

        self.entry_contact=Entry(manage_frame,textvariable=self.Contact_Var,font=('times new roman',20),bg='lightgray',bd=5)
        self.entry_contact.place(x=200,y=300)

        self.entry_address=Entry(manage_frame,textvariable=self.Address_Var,font=('times new roman',20),bg='lightgray',bd=5)
        self.entry_address.place(x=200,y=360)

        # === Combobox for Gender === #

        self.combogender=ttk.Combobox(manage_frame,textvariable=self.Gender_Var,font=('times new roman',20),state='readonly')
        self.combogender['values']=('Male','Female')
        self.combogender.place(x=200,y=240)

        # === Adding buttons in manage frame === #
        self.addbt=Button(manage_frame,text='Add',command=self.add,bg='pink',fg='brown',font=20)
        self.addbt.place(x=20,y=480,width=100)

        self.updatebt=Button(manage_frame,text='Update',bg='pink',fg='brown',font=20)
        self.updatebt.place(x=125,y=480,width=100)

        self.deletebt=Button(manage_frame,text='Delete',bg='pink',fg='brown',font=20)
        self.deletebt.place(x=230,y=480,width=100)

        self.clearbt=Button(manage_frame,text='Clear',command=self.clear,bg='pink',fg='brown',font=20)
        self.clearbt.place(x=340,y=480,width=100)

        # === Details Frame === #
        detail_frame=Frame(self.window,bg='crimson')
        detail_frame.place(x = 600 ,y = 100, height=670,width=850 )

        # === Search By label === #
        search_label=Label(detail_frame,text='Search By',bg='crimson',fg='white',font=('times new roman',25))
        search_label.place(x=20,y=10)

        # Select options combobox === #
        select_combo=ttk.Combobox(detail_frame,font=('times new roman',20),state='readonly')
        select_combo['values']=('Roll No.','Name','Email','Contact No.','D.O.B','Address')
        select_combo.place(x=180,y=10,width=180)

        # === Entry for detail frame === #
        detail_entry=Entry(detail_frame,font=('times new roman',20))
        detail_entry.place(x=380,y=10,width=180)

        # === Detail Frame search button === #
        searchbt=Button(detail_frame,text='Search',font=('times new roman',20))
        searchbt.place(x=580,y=10,height=40)

        show_all_bt=Button(detail_frame,text='Show all',font=('times new roman',20))
        show_all_bt.place(x=700,y=10,height=40)

        # === Table Frame === #
        table_frame=Frame(detail_frame,bd=4,bg='crimson')
        table_frame.place(x=20,y=80,width=800,height=550)
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(table_frame,columns=('rollno','name','email','gender','contact','dob','address'), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading('rollno',text='Roll no.')
        self.Student_table.heading('name',text='Name')
        self.Student_table.heading('email',text='Email')
        self.Student_table.heading('gender',text='Gender')
        self.Student_table.heading('dob',text='D.O.B')
        self.Student_table.heading('address',text='Address')
        self.Student_table.heading('contact',text='Contact')
        self.Student_table['show']='headings'
        self.Student_table.pack(fill=BOTH,expand=TRUE)
        self.Student_table.pack()

    def add(self):
        connection=pymysql.connect(host='localhost',user='window',password='',database='stu')
        cursor = connection.cursor()
        cursor.execute("insert into student(roll_no,name,email,gender,contact,dob,address) values(%s,%s,%s,%s,%s,%s,%s)",
                       (self.Roll_no_Var.get(),
                        self.Name_Var.get(),
                        self.Email_Var.get(),
                        self.Gender_Var.get(),
                        self.Contact_Var.get(),
                        self.Date_of_birth_Var.get(),
                        self.Address_Var.get()
                       ))
        connection.commit()
        self.fetch()
        self.clear()
        connection.close()

    def fetch(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stu")
        cur = con.cursor()
        cur.execute("select* from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
            self.clear()
            con.close()

    def clear(self):
        self.Roll_no_Var.set(''),
        self.Name_Var.set(''),
        self.Email_Var.set(''),
        self.Gender_Var.set(''),
        self.Contact_Var.set(''),
        self.Date_of_birth_Var.set(''),
        self.Address_Var.set('')


window=Tk()
s1=Student(window)
window.mainloop()
