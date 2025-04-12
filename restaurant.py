from tkinter import * 
from tkinter.ttk import Combobox
import json


def check ():
    addres=ent_addres.get()
    phonenumber=ent_phonenumber.get()
    email=ent_email.get()
    pizza=ent_pizza.get()
    info={
        "addres":addres,
        "phonenumber":phonenumber,
        "email":email,
        "pizza":pizza
    }
    
    if addres != "" and phonenumber !=""and email !="" and pizza !="":
        info_transfer=json.dumps(info)
        with open("restaurant.txt","w") as file:
            data=file.write(info_transfer)
        print(data)
        empty_lbl.config(text="complete good jub^_^",fg="green")
    else:
        empty_lbl.config(text="complete it bruuuue...(*￣０￣)ノ",fg="red")

restaurant=Tk()
restaurant.geometry("500x600")
restaurant.title("restaurant")
restaurant.config(bg="#86A788")


lbl_addres=Label(restaurant,text="your addres :",fg="#FFFDEC",bg="#86A788",font=("Arial",15))
lbl_phonenumber=Label(restaurant,text="your phone number :",fg="#FFFDEC",bg="#86A788",font=("Arial",15))
lbl_email=Label(restaurant,text="your email :",fg="#FFFDEC",bg="#86A788",font=("Arial",15))
lbl_pizza=Label(restaurant,text="choese pizza :",fg="#FFFDEC",bg="#86A788",font=("Arial",15))
empty_lbl=Label(restaurant,text="",font=("",17),bg="#86A788")

ent_addres=Entry(restaurant,font=("",15))
ent_phonenumber=Entry(restaurant,font=("",15))
ent_email=Entry(restaurant,font=("",15))
ent_pizza=Combobox(restaurant,values=("Chicago Style pizza","Brick Oven Pizza","Italian Pizza","Neapolitan Pizza","California Pizza","New York Style Pizza","Sicilian Pizza","Greek Pizza","Detroit Pizza","Bagel Pizza","French Break Pizza"),font=("",15))

btn_save=Button(restaurant,text="Save",bg="#1F4529",font=("Arial",15),width=8,height=2,command=check)
btn_exit=Button(restaurant,text="Exit",bg="#FFCFCF",font=("Arial",15),width=8,height=2,command=restaurant.destroy)

lbl_addres.grid(row=0,column=0,pady=30)
lbl_phonenumber.grid(row=1,column=0,pady=30)
lbl_email.grid(row=2,column=0,pady=30)
lbl_pizza.grid(row=3,column=0,pady=30)

ent_addres.grid(row=0,column=1,pady=20)
ent_phonenumber.grid(row=1,column=1,pady=20)
ent_email.grid(row=2,column=1,pady=20)
ent_pizza.grid(row=3,column=1,pady=20)

btn_save.grid(row=4,column=0,pady=20)
btn_exit.grid(row=4,column=1,padx=20)
restaurant.mainloop()