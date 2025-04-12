from tkinter import *


def number_guess():
    import number_guess

def color_guess():
    import color_guess





#start step
root_2=Tk()
root_2.title("guesser page")
root_2.geometry("450x300")
root_2.config(bg="light blue")



#button
btn_color_guess=Button(root_2,text="color guess",bg="green",font=("Times",15),width=8,height=1,command=color_guess)
btn_number_guess=Button(root_2,text="number guess",bg="green",font=("Times",15),width=9,height=1,command=number_guess)





#place
btn_color_guess.place(x=100,y=100)
btn_number_guess.place(x=250,y=100)



#mainloop
root_2.mainloop()