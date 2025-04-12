from tkinter import *
from pymongo import MongoClient


client=MongoClient("localhost",27017)
db=client.get_database("project_mongodb")
coll=db.get_collection("mongodb_coll")

#def


def reg():
    username=ent_username.get()
    password=ent_password.get()

    de = {
        "username":username,
        "password":password
    }
    data=coll.find_one({"username":username})

    if len(username)<3 and len(password)<4:
        print("error404")
    elif not data:
        coll.insert_one(de)
        print("fine")
    else:
        print("error 404")
    

def login():
    username=ent_username.get()
    password=ent_password.get()
    data=coll.find_one({"username":username,"password":password})
    if data:
        print("fine")
        import user
    else:
        print("error 404")






#start step
signup=Tk()
signup.title("enter page")
signup.geometry("500x350")
signup.config(bg="cyan")

#label
lbl_username=Label(signup,text="username: ",bg="cyan",font=("Ariel",15))
lbl_password=Label(signup,text="password: ",bg="cyan",font=("Ariel",15))

#entry
ent_username=Entry(signup,font=("Ariel",15),fg="#02faee")
ent_password=Entry(signup,font=("Ariel",15),fg="#02faee")


#button
btn_login=Button(signup,text="login",bg="red",font=("Ariel",15),width=10,height=1,command=login)
btn_register=Button(signup,text="register",bg="green",font=("Ariel",15),width=10,height=1,command=reg)




lbl_username.grid(row=0,column=0,padx=10,pady=10)
lbl_password.grid(row=1,column=0,padx=10,pady=10)

ent_username.grid(row=0,column=1,padx=10,pady=10)
ent_password.grid(row=1,column=1,padx=10,pady=10)

btn_login.grid(row=2,column=0,padx=10,pady=30)
btn_register.grid(row=2,column=1,padx=10,pady=30)

signup.mainloop()