from tkinter import *
from tkinter.ttk import Combobox
def check ():
    topic=ent_topic.get()
    time=ent_time.get()
    day=ent_day.get()
    doctor=ent_doctors.get()
    if topic != "" and time !=""and day !="":
        cf=open(f"clinic.txt","a")
        cf.write(f"Topic :{topic}\nTime: {time} \nDay: {day} \nDoctor:{doctor} \n *************")
        empty_lbl.config(text="complete good jub^_^",fg="green")
    else:
        empty_lbl.config(text="complete it bruuuue...(*￣０￣)ノ",fg="red")


win=Tk()
win.geometry("790x500")
win.resizable(0,0)
win.config(bg="skyblue")
win.title("user information")

lbl_hello=Label(win,text="Hi , welcome to poulstar clinic",fg="#3244a8",bg="skyblue",font=("times",17))
lbl_topic=Label(win,text="choese one of the topics:",fg="black",font=("Times",17),bg="skyblue")
lbl_time=Label(win,text="choese one of the times:",fg="black",font=("Times",17),bg="skyblue")
lbl_day=Label(win,text="choese one of the days:",fg="black",font=("Times",17),bg="skyblue")
lbl_doctor=Label(win,text="chose on of the doctors :",fg="black",font=("Times",17),bg="skyblue")


ent_topic=Combobox(win,values=("dentistry","physiotherapy","vetrinary medicine","professional","laboratory"),font=("",12))
ent_day=Combobox(win,values=('saturday','sunday','monday','tusday','wednesday','thursday','friday'),font=("",12))
ent_time=Combobox(win,values=("12:30","14:50","15:20","17:30","19:40","20:10"),font=("",12))
ent_doctors=Combobox(win,values=("mr frotan","mrs nasir zadeh","mr nick","mrs gholi por","ms hasan por","ms jahani","mrs hosseini","ms golestani","mrs mousavi"),font=("",12))

btn_save=Button(win,text="Save",bg="lightgreen",font=("Arial",15),width=8,height=2,command=check)
empty_lbl=Label(win,text="",font=("",17),bg="skyblue")

lbl_hello.grid(row=0,column=0,padx=50)
lbl_topic.grid(row=1,column=0)
lbl_day.grid(row=2,column=0)
lbl_time.grid(row=3,column=0)
lbl_doctor.grid(row=4,column=0)

ent_topic.grid(row=1,column=1,pady=20)
ent_day.grid(row=2,column=1,pady=20,)
ent_time.grid(row=3,column=1,pady=20)
ent_doctors.grid(row=4,column=1,pady=20)

btn_save.grid(row=5,column=1)
empty_lbl.grid(row=6,column=3)



win.mainloop()