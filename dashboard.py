from tkinter import *

def dashboard():
    WIN = Tk()
    WIN.title('Online Banking System')
    WIN.geometry('360x640')
    background = PhotoImage(file="images/DaBank.png")
    label_background = Label(WIN,image=background,borderwidth=0)
    label_background.place(x=0,y=0)

    # created a function named admin_page
    def admin_page():
        '''Destroys the tkinter window and call open function i.e. login function from a admin page'''
        WIN.destroy()
        from adminloginfirst import adminlogin as adminlogin
        adminlogin()

    # created a function named user_page
    def user_page():
        '''Destroys the tkinter window and call open_register function i.e. register function from a register page'''
        WIN.destroy()
        from Login_as_user import userlogin as open_register
        open_register()

    #Created a Function named on_enter_admin_login with 'e' as one parameter
    def on_enter_admin_login(e):
        '''Changed Background and Foreground of Login Button named admin_login_button
        to #ABBC41 and white respectively when function is called.'''
        admin_login_button.config(background='#7409EB')

    #Created a Function named on_leave_admin_login with 'e' as one parameter
    def on_leave_admin_login(e):
        '''Changed Background and Foreground of Login Button named admin_login_button to
        pink and black respectively when function is called.'''
        admin_login_button.config(background= '#645394')

    #created a Login Button which calls admin_page function when pressed
    admin_login_button = Button(WIN,text="Login as Admin",
                                padx=15,borderwidth=0,  font=("Comic Sans MS", 16),
                                 background='#645394', foreground= 'white',command=admin_page)
    admin_login_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    admin_login_button.bind('<Enter>',on_enter_admin_login)
    admin_login_button.bind('<Leave>',on_leave_admin_login)

    # Created a Function named on_enter_user_login with 'e' as one parameter
    def on_enter_user_login(e):
        user_login_button.config(background='#7409EB')

    # Created a Function named on_leave_user_login with 'e' as one parameter
    def on_leave_user_login(e):
        user_login_button.config(background= '#645394')
     
    # created a Register Button which calls user_page function 
    # when pressed
    user_login_button = Button(WIN,text="Login as User",padx=15, borderwidth=0,
                                font=("Comic Sans MS", 16), background='#645394',
                                 foreground= 'white',command=user_page)
    user_login_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    user_login_button.bind('<Enter>',on_enter_user_login)
    user_login_button.bind('<Leave>',on_leave_user_login)

    #Updates all Into TKinter Window
    WIN.mainloop()

#calls dashboard Function
dashboard()
