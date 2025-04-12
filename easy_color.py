from tkinter import *
from tkinter.ttk import Combobox
import random








easy_color_list=["red","blue","yellow","green"]
def easy_color():   
    pc_easy_color=random.choice(easy_color_list)
    user_easy_color=combo_list_easy_color.get()
    print(f"pc: {pc_easy_color}")
    print(f"you: {user_easy_color}")
    if user_easy_color == pc_easy_color:
        win_color_easy=Toplevel()
        win_color_easy.geometry("500x500")
        win_color_easy.title("WIN")
        win_color_easy.config(bg="light green")
        lbl_win_color_easy=Label(win_color_easy,text="WIN",bg="light green",fg="green",font=("Times",20))
        lbl_pc_win_color_easy=Label(win_color_easy,text=pc_easy_color,bg="light green",fg="green",font=("Times",15))
        lbl_user_win_color_easy=Label(win_color_easy,text=user_easy_color,bg="light green",fg="green",font=("Times",15))
        lbl_win_color_easy.pack(padx=10,pady=10)
        lbl_user_win_color_easy.pack(padx=10,pady=10)
        lbl_pc_win_color_easy.pack()
    else:
        lose_color_easy=Toplevel()
        lose_color_easy.geometry("500x500")
        lose_color_easy.title("LOSE")
        lose_color_easy.config(bg="light pink")
        lbl_lose_color_easy=Label(lose_color_easy,text="LOSE",bg="light pink",fg="red",font=("Times",20))
        lbl_pc_lose_color_easy=Label(lose_color_easy,text=pc_easy_color,bg="light pink",fg="red",font=("Times",15))
        lbl_user_lose_color_easy=Label(lose_color_easy,text=user_easy_color,bg="light pink",fg="red",font=("Times",15))
        lbl_lose_color_easy.pack(padx=10,pady=10)
        lbl_pc_lose_color_easy.pack(padx=10,pady=10)
        lbl_user_lose_color_easy.pack()




#start step
root_4=Tk()
root_4.title("easy level")
root_4.geometry("450x300")
root_4.config(bg="skyblue")

#label
lbl_list_easy_color=Label(root_4,text=easy_color_list,bg="skyblue",font=("Times",15))

#combobox
combo_list_easy_color=Combobox(root_4,value=["red","blue","yellow","green"],font=("Times",15))

#button
btn_guess_easy_color=Button(root_4,text="guess",bg="green",font=("Times",15),command=easy_color)

#packs
lbl_list_easy_color.pack(padx=10,pady=10)
combo_list_easy_color.pack(padx=10,pady=10)
btn_guess_easy_color.pack()

root_4.mainloop()