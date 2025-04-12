from tkinter import *

def main():
    import main_page

def stock1():
    import stock1


user=Tk()
user.title("user page")
user.resizable(0,0)
user.geometry("250x100")
user.config(bg="light blue")



main_btn=Button(user,text="game page",bg="purple",font=("Times",13),width=8,height=1,command=main)
stock_btn=Button(user,text="stock page",bg="purple",font=("Times",13),width=8,height=1,command=stock1)


main_btn.grid(row=0,column=0,padx=10,pady=10)
stock_btn.grid(row=0,column=1,padx=10,pady=10)


user.mainloop()