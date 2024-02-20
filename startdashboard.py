from tkinter import *


def dashboard():
    # Create a Tkinter Window
    WIN = Tk()
    WIN.title('Online Banking System')
    WIN.geometry('360x640')
    
    def admin_page():
        '''Destroys the tkinter window and call open function i.e. login function from a admin page'''
        WIN.destroy()
        from dashboard import dashboard
        dashboard()

    # Set background image
    background = PhotoImage(file="images/DaBank.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)

    # Function to handle mouse entering the button
    def on_enter_get_started(e):
        get_started_button.config(background='#7409EB')

    # Function to handle mouse leaving the button
    def on_leave_get_started(e):
        get_started_button.config(background='#645394')

    # Function to proceed to the user page
    def user_page():
        WIN.destroy()
        from Login_as_user import userlogin
        userlogin()

    get_started_button = Button(WIN, text="Get Started", padx=15, borderwidth=0,
                                font=("Comic Sans MS", 16), background='#645394',
                                foreground='white', command=admin_page)
    get_started_button.place(relx=0.5, rely=0.75, anchor=CENTER)

    
    get_started_button.bind('<Enter>', on_enter_get_started)
    get_started_button.bind('<Leave>', on_leave_get_started)

    WIN.mainloop()

dashboard()
