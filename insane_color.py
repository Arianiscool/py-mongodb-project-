from tkinter.ttk import Combobox
from tkinter import *
import random







insane_color_list=["red","cherry red","rose","jam","merlot","garnet","orange","tangerine","nerigold","cider","rust","ginger","tan","beige","macaroon","hazel wood","granola","oat","green","chartreuse","juniper","sage","lime","fern","blue","slate","navy","indigo","cobalt","purple","mauve","dark violet","boysenberry","electric lavender","plum","pink","hot pink","french fuchsia","punch","blush pink","watermelon","brown oil","roasted coffee","mocha","peanut brown","carob","hickory","black","ebony","crow","charcoal","midnight","ink","gray","shadow","graphite","iron","pewter","cloud"]
def insane_color():   
    pc_insane_color=random.choice(insane_color_list)
    user_insane_color=combo_list_insane_color.get()
    print(f"pc: {pc_insane_color}")
    print(f"you: {user_insane_color}")
    if user_insane_color == pc_insane_color:
        win_color_insane=Toplevel()
        win_color_insane.geometry("500x500")
        win_color_insane.title("WIN")
        win_color_insane.config(bg="light green")
        lbl_win_color_insane=Label(win_color_insane,text="WIN",bg="light green",fg="green",font=("Times",20))
        lbl_pc_win_color_insane=Label(win_color_insane,text=pc_insane_color,bg="light green",fg="green",font=("Times",15))
        lbl_user_win_color_insane=Label(win_color_insane,text=user_insane_color,bg="light green",fg="green",font=("Times",15))
        lbl_win_color_insane.pack(padx=10,pady=10)
        lbl_user_win_color_insane.pack(padx=10,pady=10)
        lbl_pc_win_color_insane.pack()
        print(insane_color_list)
    else:
        lose_color_insane=Toplevel()
        lose_color_insane.geometry("500x500")
        lose_color_insane.title("LOSE")
        lose_color_insane.config(bg="light pink")
        lbl_lose_color_insane=Label(lose_color_insane,text="LOSE",bg="light pink",fg="red",font=("Times",20))
        lbl_pc_lose_color_insane=Label(lose_color_insane,text=pc_insane_color,bg="light pink",fg="red",font=("Times",15))
        lbl_user_lose_color_insane=Label(lose_color_insane,text=user_insane_color,bg="light pink",fg="red",font=("Times",15))
        lbl_lose_color_insane.pack(padx=10,pady=10)
        lbl_pc_lose_color_insane.pack(padx=10,pady=10)
        lbl_user_lose_color_insane.pack()
        print(insane_color_list)




#start step
root_7=Tk()
root_7.title("insane level")
root_7.geometry("450x300")
root_7.config(bg="skyblue")

#label
lbl_list_insane_color=Label(root_7,text="look at the terminal",bg="skyblue",font=("Times",15))

#combobox
combo_list_insane_color=Combobox(root_7,value=["red","cherry red","rose","jam","merlot","garnet","orange","tangerine","nerigold","cider","rust","ginger","tan","beige","macaroon","hazel wood","granola","oat","green","chartreuse","juniper","sage","lime","fern","blue","slate","navy","indigo","cobalt","purple","mauve","dark violet","boysenberry","electric lavender","plum","pink","hot pink","french fuchsia","punch","blush pink","watermelon","brown oil","roasted coffee","mocha","peanut brown","carob","hickory","black","ebony","crow","charcoal","midnight","ink","gray","shadow","graphite","iron","pewter","cloud"],font=("Times",15))

#button
btn_guess_insane_color=Button(root_7,text="guess",bg="green",font=("Times",15),command=insane_color)

#packs
lbl_list_insane_color.pack(padx=10,pady=10)
combo_list_insane_color.pack(padx=10,pady=10)
btn_guess_insane_color.pack()




print(insane_color_list)
root_7.mainloop()