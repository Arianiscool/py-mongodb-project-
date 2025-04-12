from tkinter import *
from tkinter import font
import requests
from pymongo import MongoClient
from tkinter import ttk



client=MongoClient("localhost",27017)
db=client.get_database("stock")
coll=db.get_collection("stock list")




def update():
    data=requests.get("https://one-api.ir/DigitalCurrency/?token=866342:67eab0a4bc572").json()
    result=data["result"] 
    name=[]
    price=[]
    for d in result:
        name.append(d["key"])
        price.append(d["price"])
    coll.delete_many({})
    for i in range(len(name)):
        coll.insert_one({"key":name[i],"price":price[i]})
    treev.delete(*treev.get_children())
    for a in range(len(name)):
        treev.insert('','end', values=(name[a], price[a]))


def search():
    word=search_entry.get()
    data=coll.find({"key":{"$regex":word, "$options": "i"}},{"_id":0})
    treev.delete(*treev.get_children())
    for d in data:
        treev.insert('',0,values=list(d.values()))











root=Tk()
root.geometry("750x600")
root.title("stock app")
root.config(bg="blue")


frame1=Frame(root)
frame1.config(bg="blue")
frame1.pack()

all_font=font.Font(family="Galdeano",weight="bold")

lbl_wellcome=Label(frame1,text="wellcome to my stock app",bg="blue", font=(all_font,20))
btn_click=Button(frame1,text="click me to update the stock",bg="cyan",font=(all_font,12),command=update)


frame2=Frame(root)
frame2.config(bg="blue")
frame2.pack()

search_entry=Entry(frame2,font=("",14))
search_entry.grid(row=0,column=0,pady=20)

Button(frame2,text="search",bg="black",fg="white",command=search).grid(row=0,column=1)


frame3=Frame(root)
frame3.pack()

treev=ttk.Treeview(frame3,columns=(1,2),show="headings",height=10)
treev.heading(1,text="Name")
treev.column(1,width=400,anchor="c")
treev.heading(2,text="Price")
treev.column(2,width=300,anchor="c")
treev.grid(row=0,column=0,columnspan=10,pady=20)


myscrollbar=Scrollbar(frame3,orient="vertical",command=treev.yview)
treev.config(yscrollcommand=myscrollbar.set)
myscrollbar.grid(row=0,column=11,sticky="ns")

frame4=Frame(root)
frame4.pack()






#pack
lbl_wellcome.pack(pady=20)
btn_click.pack(pady=20)

root.mainloop()

