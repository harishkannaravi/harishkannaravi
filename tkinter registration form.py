from tkinter import*
from tkcalendar import DateEntry
from tkinter import messagebox as mb
import datetime

root = Tk()
root.geometry('540x540')
root.title("Registration form")
root.config(background='grey')

def msg():
    course = cvar.get()
    gender =var.get()
    if(gender == 1 or gender ==2):
        if(e1.index("end") ==0):
            mb.showwarning('missing details','enter your name')
        elif(e2.index("end") ==0):
            mb.showwarning('missing details','enter your email id')
        elif(e3.index("end") ==0):
            mb.showwarning('missing details','enter your contact number')
        else:
            mb.showinfo('success','Registration done successfully for the course ' + course)
    else:
        mb.showinfo('missing details','enter your gender')

def save():
    g= var.get()
    course=cvar.get()
    db=dob.get_date()
    d = db.strftime('%d/%m/%Y')
    now=datetime.datetime.now()
    if(g==1):
        gender='male'
    else:
        gender='female'

    
    s= '\n' + now.strftime("%d-%m-%Y%H%M")+'\t'+e1.get()+'\t'+e2.get()+'\t'+e3.get()+'\t'+d+'\t'+gender+'\t'+course
    f = open(('regdetails.txt'),'a')
    f.write(s)
    f.close()



def saveinfo():
    save()
    msg()


l0=Label(root, text="Course Registration form",width=25,font=("times",20,"bold"),bg='blue', fg='white')
l0.place(x=70,y=50)
l1=Label(root, text="Full Name",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l1.place(x=70,y=130)
e1=Entry(root,width=30,bd=2)
e1.place(x=240,y=130)
l2=Label(root, text="Email Id",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l2.place(x=70,y=180)
e2=Entry(root,width=30,bd=2)
e2.place(x=240,y=180)
l3=Label(root, text="Contact No:",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l3.place(x=70,y=230)
e3=Entry(root,width=30,bd=2)
e3.place(x=240,y=230)

l4=Label(root, text="DOB",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l4.place(x=70,y=280)
dob= DateEntry(root, width=27,background='brown', fg='white', date_pattern='dd/mm/Y',borderwidthh=3)
dob.place(x=240,y=280)

l5=Label(root, text="Gender",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l5.place(x=70,y=330)

var = IntVar()
r1 = Radiobutton(root, text="Male", variable=var, value=1, font=("times",12),bg='grey')
r1.place(x=235,y=330)
r2 = Radiobutton(root, text="Female",variable=var, value=2, font=("times",12),bg='grey')
r2.place(x=315,y=330)


l6=Label(root, text="Select Course",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l6.place(x=70,y=380)

cvar = StringVar()
cvar.set("select course")
option = ("python","javascript","DS","java")
o = OptionMenu(root,cvar, *option)
o.config(font=("times",11),bg='white')
o.place(x=240,y=365,width=190)
    


b1=Button(root, text='submit',command=saveinfo,width=15,bg='green',fg='white',font=("times",12,"bold"))
b1.place(x=120,y=440)
b2=Button(root, text='cancel',command=root.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
b2.place(x=320,y=440)    

root.mainloop()
