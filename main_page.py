from tkinter import *



def guesser():
    import guesser_page


def clinic():
    import clinic


def restaurant():
    import restaurant






#start step
root_1=Tk()
root_1.title("Main page")
root_1.geometry("450x300")
root_1.config(bg="light blue")



#button
btn_guesser=Button(root_1,text="guesser",bg="green",font=("Times",15),width=7,height=1,command=guesser)
btn_clinic=Button(root_1,text="clinic",bg="skyblue",font=("Times",15),width=7,height=1,command=clinic)
btn_restaurant=Button(root_1,text="restaurant",bg="#86A788",font=("Times",15),width=7,height=1,command=restaurant)




#place
btn_guesser.place(x=100,y=100)
btn_clinic.place(x=200,y=100)
btn_restaurant.place(x=300,y=100)

#mainloop
root_1.mainloop()