
from tkinter import *


def dashboard_call(WIN):
    '''Destroys the tkinter window and call open function i.e. login function from a admin page'''
    WIN.destroy()
    from dashboard import dashboard
    dashboard()


#Created a Function Named homepage Which Stores all the Codes of Main Page
# so it can be called later from another program
def homepage():
    #Created a Tkinter Window named WIN
    WIN = Tk()
    #Placed Image as Iconphoto on Window
    logo_image = PhotoImage(file="images/fish2.png")
    WIN.iconphoto(False, logo_image)
    #Named Tkinter Window
    WIN.title('Online Banking System')
    #Set size of Tkinter Window
    WIN.geometry('360x640')
    #Placed backround.png image as BAckground to a TKinter Window
    background = PhotoImage(file="images/userdashboard.png")
    label_background = Label(WIN,image=background,borderwidth=0)
    label_background.place(x=0,y=0)
    
    
    button_image = PhotoImage(file="images/arrow.png")
    button = Button(WIN, image=button_image, borderwidth=0, width=30, height=30,command = lambda:dashboard_call(WIN))
    button.place(x=4, y=5)


    # created a function named login_page
    def add_user_page():
        '''Destroys the tkinter window and call open_login function i.e. login function from a login page'''
        WIN.destroy()
        from adduser import add_new_user
        add_new_user()
        
    def user_list_page():
        '''Destroys the tkinter window and call open_login function i.e. login function from a login page'''
        WIN.destroy()
        from user_list import view_users
        view_users()
    
    def remove_users_page():
        '''Destroys the tkinter window and call open_login function i.e. login function from a login page'''
        WIN.destroy()
        from userdetail import viewusers
        viewusers()


    #Created a Function named on_enter_add_voter with 'e' as one parameter
    def on_enter_add_user(e):
        '''Changed Background and Foreground of Login Button named add_voter
        to #edd8ed and red respectively when function is called.'''
        add_user.config(background='#7409EB',foreground= "white")

    #Created a Function named on_leave_add_voter with 'e' as one parameter
    def on_leave_add_user(e):
        '''Changed Background and Foreground of Button named add_voter to
        pink and black respectively when function is called.'''
        add_user.config(background= '#645394', foreground= 'white')

    #created a Login Button which calls login_page function when pressed
    add_user = Button(WIN,text="Deposit Money",padx=13,borderwidth=0,font=("Comic Sans MS", 11),background= '#645394', foreground= 'white',command=lambda:add_user_page())
    add_user.place(relx=0.3, rely=0.5, anchor=CENTER)
    #Created a Bind i.e. When Entered inside add voter button calls on_enter_add_voter function
    #and when leaves the add voter button calls on_leave_add_voter function
    add_user.bind('<Enter>',on_enter_add_user)
    add_user.bind('<Leave>',on_leave_add_user)

    # Created a Function named on_enter_remove_users with 'e' as one parameter
    def on_enter_remove_users(e):
        '''Changed Background and Foreground of Register Button named remove_users
        to #ABBC41 and white respectively when function is called.'''
        remove_users.config(background='#7409EB',foreground= "white")

    # Created a Function named on_leave_view_voter with 'e' as one parameter
    def on_leave_remove_users(e):
        '''Changed Background and Foreground of Register Button named view_votes to
        pink and black respectively when function is called.'''
        remove_users.config(background= '#645394', foreground= 'white')

    # created a view votes Button which calls view_votes function when pressed
    remove_users= Button(WIN,text="Retrieve Money",padx=13,borderwidth=0,font=("Comic Sans MS", 11),background= '#645394', foreground= 'white',command=lambda:remove_users_page())
    remove_users.place(relx=0.7, rely=0.5, anchor=CENTER)
    #Created a Bind i.e. When Entered inside a view votes button calls on_enter_view_votes function
    #and when leaves the view votes button calls on_leave_view_votes function
    remove_users.bind('<Enter>',on_enter_remove_users)
    remove_users.bind('<Leave>',on_leave_remove_users)


    # Created a Function named on_enter_view_voter with 'e' as one parameter
    def on_enter_user_list(e):
        '''Changed Background and Foreground of Button named view_voter
        to #edd8ed and white respectively when function is called.'''
        user_list.config(background='#7409EB',foreground= "white")

    # Created a Function named on_leave_view_voter with 'e' as one parameter
    def on_leave_user_list(e):
        '''Changed Background and Foreground of Button named view_voter to
        pink and black respectively when function is called.'''
        user_list.config(background= '#645394', foreground= 'white')


    # created a view voter list Button which calls view voter function when pressed
    user_list= Button(WIN,text="Request Account Deletion",padx=13,borderwidth=0,font=("Comic Sans MS", 12),background= '#645394', foreground= 'white',command=lambda:user_list_page())
    user_list.place(relx=0.5, rely=0.6, anchor=CENTER)
    #Created a Bind i.e. When Entered inside view voter button calls on_enter_view_voter function
    #and when leaved button calls on_leave_view_voter function
    user_list.bind('<Enter>',on_enter_user_list)
    user_list.bind('<Leave>',on_leave_user_list)

    def get_total_users():
        # Fetch total users from your data source
        # This is a placeholder function, replace it with your actual implementation
        return 100

    def homepage():
        total_users = get_total_users()
        total_users_label = Label(WIN,text="Request Account Deletion",padx=13,borderwidth=0,font=("Comic Sans MS", 12),background= '#645394', foreground= 'white',command=lambda:user_list_page())
        total_users_label(relx=0.5, rely=0.6, anchor=CENTER)

        
    

    #Updates all Into TKinter Window
    WIN.mainloop()

#calls homepage Function
homepage()