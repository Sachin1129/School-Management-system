def addstudent():
    def submitadd():
        id =idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate =time.strftime("%d/%m/%Y")
        print(addeddate)
        print(addedtime)
        
        try:
           strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
           mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
           con.commit()
           res = messagebox.askyesnocancel('Notifications','Id{} Name{} Added sucessfully..and want to clean the form'.format(id,name),parent=addroot)
           if(res==TRUE):
               idval.set('')
               nameval.set('')
               mobileval.set('')
               emailval.set('')
               addressval.set('')
               genderval.set('')
               dobval.set('')
        except:
            messagebox.showerror('Notifications','Id Already Exist try another one...',parent=addroot)
        strr='select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)
        
           
       
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.resizable(False,False)
    ##################addstudentslabel_and_entryboxes
    idlabel = Label(addroot,text='Enter Id : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    ###########entrybox
    idval = StringVar()
    identry = Entry(addroot,font=('times',13,'bold'),bd=3,textvariable=idval)
    identry.place(x=250,y=10)
    
    namelabel = Label(addroot,text='Enter Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)
    
    ###########entrybox
    nameval=StringVar()
    nameentry = Entry(addroot,font=('times',13,'bold'),bd=3,textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    mobilelabel = Label(addroot,text='Enter Mobile : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    ###########entrybox
    mobileval=StringVar()
    mobileentry = Entry(addroot,font=('times',13,'bold'),bd=3,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    
    emaillabel = Label(addroot,text='Enter Email : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    ###########entrybox 
    emailval=StringVar()
    emailentry = Entry(addroot,font=('times',13,'bold'),bd=3,textvariable=emailval)
    emailentry.place(x=250,y=190)
    
    addresslabel = Label(addroot,text='Enter Address : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    ###########entrybox
    addressval=StringVar()
    addressentry = Entry(addroot,font=('times',13,'bold'),bd=3,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderlabel = Label(addroot,text='Enter Gender : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
    
    ###########entrybox
    genderval=StringVar()
    genderentry = Entry(addroot,font=('times',13,'bold'),bd=3,textvariable=genderval)
    genderentry.place(x=250,y=310)

    doblabel = Label(addroot,text='Enter D.O.B : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
    
    ###########entrybox
    dobval=StringVar()
    dobentry = Entry(addroot,font=('times',13,'bold'),bd=3,textvariable=dobval)
    dobentry.place(x=250,y=370)
    ##################################submit_button
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)
    
    addroot.mainloop()

def searchstudent():
    def search():
        id =idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate =time.strftime("%d/%m/%Y")
        if(id!=''):
            strr='select * from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif(name!=''):
            strr='select * from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif(mobile!=''):
            strr='select * from studentdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        
        elif(email!=''):
            strr='select * from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif(address!=''):
            strr='select * from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif(gender!=''):
            strr='select * from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif(addeddate!=''):
            strr='select * from studentdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif(dob!=''):
            strr='select * from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
                
        
            
        
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='blue')
    searchroot.resizable(False,False)
    ##################addstudentslabel_and_entryboxes
    idlabel = Label(searchroot,text='Enter Id : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    ###########entrybox
    idval = StringVar()
    identry = Entry(searchroot,font=('times',13,'bold'),bd=3,textvariable=idval)
    identry.place(x=250,y=10)
    ##################searchstudentslabel_and_entryboxes
    namelabel = Label(searchroot,text='Enter Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)
    
    ###########entrybox
    nameval=StringVar()
    nameentry = Entry(searchroot,font=('times',13,'bold'),bd=3,textvariable=nameval)
    nameentry.place(x=250,y=70)
    ##################mobilestudentslabel_and_entryboxes
    mobilelabel = Label(searchroot,text='Enter Mobile : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    ###########entrybox
    mobileval=StringVar()
    mobileentry = Entry(searchroot,font=('times',13,'bold'),bd=3,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    ##################emailstudentslabel_and_entryboxes
    emaillabel = Label(searchroot,text='Enter Email : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    ###########entrybox 
    emailval=StringVar()
    emailentry = Entry(searchroot,font=('times',13,'bold'),bd=3,textvariable=emailval)
    emailentry.place(x=250,y=190)
    ##################addressstudentslabel_and_entryboxes
    addresslabel = Label(searchroot,text='Enter Address : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    ###########entrybox
    addressval=StringVar()
    addressentry = Entry(searchroot,font=('times',13,'bold'),bd=3,textvariable=addressval)
    addressentry.place(x=250,y=250)
     ##################genderstudentslabel_and_entryboxes
    genderlabel = Label(searchroot,text='Enter Gender : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
    
    ###########entrybox
    genderval=StringVar()
    genderentry = Entry(searchroot,font=('times',13,'bold'),bd=3,textvariable=genderval)
    genderentry.place(x=250,y=310)
     ##################dobstudentslabel_and_entryboxes
    doblabel = Label(searchroot,text='Enter D.O.B : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
    
    ###########entrybox
    dobval=StringVar()
    dobentry = Entry(searchroot,font=('times',13,'bold'),bd=3,textvariable=dobval)
    dobentry.place(x=250,y=370)
    ##################datestudentslabel_and_entryboxes
    datelabel = Label(searchroot,text='Enter Date : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
    ###########entrybox
    dateval=StringVar()
    dateentry = Entry(searchroot,font=('times',13,'bold'),bd=3,textvariable=dateval)
    dateentry.place(x=250,y=430)
    ##################################submit_button
    submitbtn = Button(searchroot,text='Search',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=search)
    submitbtn.place(x=150,y=490)
    
    searchroot.mainloop()



def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr='select * from studentdata1'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('', END,values=vv)
    

def updatestudent():
    def update():
        id =idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications','Id {} Updated sucessfully...'.format(id),parent=updateroot)
        strr='select * from studentdata1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('', END,values=vv)
        
        

        
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+100')
    updateroot.title('Student Management System')
    updateroot.config(bg='blue')
    updateroot.resizable(False,False)
    ##################addstudentslabel_and_entryboxes
    idlabel = Label(updateroot,text='Enter Id : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    ###########entrybox
    idval = StringVar()
    identry = Entry(updateroot,font=('times',13,'bold'),bd=3,textvariable=idval)
    identry.place(x=250,y=10)
    ##################searchstudentslabel_and_entryboxes
    namelabel = Label(updateroot,text='Enter Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)
    
    ###########entrybox
    nameval=StringVar()
    nameentry = Entry(updateroot,font=('times',13,'bold'),bd=3,textvariable=nameval)
    nameentry.place(x=250,y=70)
    ##################mobilestudentslabel_and_entryboxes
    mobilelabel = Label(updateroot,text='Enter Mobile : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    ###########entrybox
    mobileval=StringVar()
    mobileentry = Entry(updateroot,font=('times',13,'bold'),bd=3,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    ##################emailstudentslabel_and_entryboxes
    emaillabel = Label(updateroot,text='Enter Email : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    ###########entrybox 
    emailval=StringVar()
    emailentry = Entry(updateroot,font=('times',13,'bold'),bd=3,textvariable=emailval)
    emailentry.place(x=250,y=190)
    ##################addressstudentslabel_and_entryboxes
    addresslabel = Label(updateroot,text='Enter Address : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    ###########entrybox
    addressval=StringVar()
    addressentry = Entry(updateroot,font=('times',13,'bold'),bd=3,textvariable=addressval)
    addressentry.place(x=250,y=250)
     ##################genderstudentslabel_and_entryboxes
    genderlabel = Label(updateroot,text='Enter Gender : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
    
    ###########entrybox
    genderval=StringVar()
    genderentry = Entry(updateroot,font=('times',13,'bold'),bd=3,textvariable=genderval)
    genderentry.place(x=250,y=310)
     ##################dobstudentslabel_and_entryboxes
    doblabel = Label(updateroot,text='Enter D.O.B : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
    
    ###########entrybox
    dobval=StringVar()
    dobentry = Entry(updateroot,font=('times',13,'bold'),bd=3,textvariable=dobval)
    dobentry.place(x=250,y=370)
    ##################datestudentslabel_and_entryboxes
    datelabel = Label(updateroot,text='Enter Date : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
    ###########entrybox
    dateval=StringVar()
    dateentry = Entry(updateroot,font=('times',13,'bold'),bd=3,textvariable=dateval)
    dateentry.place(x=250,y=430)
    ##################timestudentslabel_and_entryboxes
    timelabel = Label(updateroot,text='Enter time : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)
    ###########entrybox
    timeval=StringVar()
    timeentry = Entry(updateroot,font=('times',13,'bold'),bd=3,textvariable=timeval)
    timeentry.place(x=250,y=490)
    ##################################submit_button
    submitbtn = Button(updateroot,text='Update',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=update)
    submitbtn.place(x=150,y=540)
    
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp)!=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

   

def showall():
        strr='select * from studentdata1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('', END,values=vv)
def exportdata():
    print('added')


                         
            
                  
def exit():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res==True):
        root.destroy()
    



###########################################connect_database
def Connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect please try again')
            return
        try:
            strr='create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr='use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr='alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr='alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected to the database...',parent=dbroot)
        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            
            messagebox.showinfo('Notification','Now you are connected to the database...',parent=dbroot)
        dbroot.destroy()

            
            
        
            


        
    dbroot = Toplevel()
    dbroot.geometry('470x250+800+230')
    dbroot.grab_set()
    
    dbroot.config(bg='blue')
    ########################connectdb_labels
    hostlabel = Label(dbroot,text="Enter Host : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel.place(x=10,y=10)
    
    userlabel = Label(dbroot,text="Enter Username : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)
    
    passwordlabel = Label(dbroot,text="Enter Password : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    ##################entrybox
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    
    
    hostentry=Entry(dbroot,font=('times',13,'bold'),bd=3,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry=Entry(dbroot,font=('times',13,'bold'),bd=3,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry=Entry(dbroot,font=('times',13,'bold'),bd=3,textvariable=passwordval)
    passwordentry.place(x=250,y=130)
    ######################submit_button
    submitbutton = Button(dbroot,text='Submit',font=('times',15,'bold'),bd=4,width=20,activebackground='black',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)
    
    dbroot.mainloop()

###########################function_for_clock
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date: '+date_string +"\n"+"Time: "+time_string)
    clock.after(200,tick)
    


###############################function_for_text_animation
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count=0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count=count+1
    SliderLabel.after(200,IntroLabelTick)

from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
import time
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
root = Tk()
root.title('Student Management System')
root.config(bg='gold2')
root.geometry('1174x700+200+50')
#####################################################################################frames
###############################################################dataentry_frame_intro
DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

frontlabel = Label(DataEntryFrame,text='---------------WELCOME---------------',width=30,font=('arial',20,'italic bold'),bg='gold2',)
frontlabel.pack(side=TOP,expand=True)

########################################################################button
addbtn = Button(DataEntryFrame,text='1 Add Student',width=25,font=('arial',15,'bold',),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2 Search Student',width=25,font=('arial',15,'bold',),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3 Delete Student',width=25,font=('arial',15,'bold',),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4 Update Student',width=25,font=('arial',15,'bold',),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5 show All',width=25,font=('arial',15,'bold',),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=showall)
showallbtn.pack(side=TOP,expand=True)

exportdatabtn = Button(DataEntryFrame,text='6 Export Data',width=25,font=('arial',15,'bold',),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exportdata)
exportdatabtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7 Exit ',width=25,font=('arial',15,'bold',),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exit)
exitbtn.pack(side=TOP,expand=True)


ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)
#############################################showdataframe
style=ttk.Style()
style.configure('Treeview.Heading',font=('times',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='cyn')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']="headings"
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)



###########################################################################


ss = 'Welcome to student management system'
count=0
text = ''
SliderLabel = Label(root,text=ss,font=('Times',30,'italic bold'),relief=RIDGE,borderwidth=4,width=30,bg='cyan')
SliderLabel.place(x=200,y=0)
IntroLabelTick()
#####################################################################clock

clock=Label(root,font=('Times',14,'bold'),relief=RIDGE,borderwidth=4,bg='white')
clock.place(x=0,y=0)
tick()
#######################################################connectdatabasebutton
connectbutton = Button(root,text='Connect To Database',width=16,font=('Times',16,'italic bold'),relief=RIDGE,borderwidth=4,bg='white',activebackground='black',activeforeground='white',command=Connectdb)
connectbutton.place(x=940,y=2)


root.mainloop()
