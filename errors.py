from tkinter import Button, Label, Toplevel


def error(title,message):
    '''Created TopLevel as WIN_top,providing its geometry and title.'''
    WIN_top = Toplevel(bg='#E0D9EF')
    WIN_top.title(title)
    WIN_top.geometry('300x150')

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)


    #function named no which when called destroys Toplevel
    def no():
        WIN_top.destroy()

    #Message to be Displayed at Toplevel
    message = Label(WIN_top, bg='#E0D9EF', text=message, font=tfont_tup, justify="center",
                        foreground="#000000")
    message.pack()


    #No Button which when pressed calls no function
    no_button = Button(WIN_top, bg='#FFFFFF', text=" Ok ", background='Red', foreground="Black", font=("Comic Sans MS", 12), command=no)
    no_button.place(x=108, y=80)

    #Places all GUI of Toplevel into it
    WIN_top.mainloop()
