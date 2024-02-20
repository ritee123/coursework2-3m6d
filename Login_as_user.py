#Imported Necessary Modules
from tkinter import *
import json
from PIL import Image
from stegano import lsb

# Created a function named adminlogin_validation
def adminlogin_validation(username, password):
    '''Checks Whether Username and Password Entry is Entered or not
    and Returns True if Username and Password is entered or Flase if not.'''
    return len(username) != 0 and username != "User Name" and len(password) != 0 and password != "Password"
    
#Created Function namedvoterlogin_error
def userlogin_data_error():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Error"
    message = "Recheck Your Input\n Values"
    from errors import error as show_error
    show_error(title,message)
    
def userlogin_validation(WIN, phonenumber, password):
    image_path = "images/profileimg.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)

    print("Decoded Data: ", decoded_data)

    for i in decoded_data["users"]:
        if i[2] == phonenumber and str(i[6]) == password:
            print("User Login Success")
            WIN.destroy()
            from user_dashboard import homepage
            homepage()
            return True
    
    print("User Login Failed")
    return False
    

def confirm_voter(WIN,user_idtemp_user_id):
    record = []  # Define the variable record

    if userlogin_validation(user_idtemp_user_id):
        # Destroys the tkinter window and call open_profile function i.e. profile_view function from a profile page
        WIN.destroy()
        from adduser import viewcandidate
        viewcandidate()
    else:
        userlogin_data_error()

#Created a Function Named voterlogin Which Stores all the Codes of voterlogin Page
# so it can be called later from another program
def userlogin():
    # Created a Tkinter Window named WIN
    WIN = Tk()
    # Placed Image as Iconphoto on Window
    logo_image = PhotoImage(file="images/fish2.png")
    WIN.iconphoto(False, logo_image)
    #Named Tkinter Window
    WIN.title('Online Banking System')
    #Set size of Tkinter Window
    WIN.geometry('360x640')

    # Placed backround.png image as BAckground to a TKinter Window
    background = PhotoImage(file="images/userlogin.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 350 and 300 respectively.
    w = Canvas(WIN, width=350, height=280, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 350 and 300
    w.create_rectangle(0, 0, 350, 300, fill="#FFFFFF", outline='#000000')
    w.pack(padx=40, pady=(310,0))
   

    #Function named temp_voter_id with one parameter i.e. 'e'
    def temp_user_id(e):
        user_id_entry.delete(0, "end")

    #Entry Box to  take voter_idtemp_voter_id Input from user
    user_id_entry = Entry(WIN, font=("Comic Sans MS", 14) , justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    user_id_entry.insert(2, "Mobile Number")
    #Bind Entry so that when Clicked for Input it calls temp_voter_id
    user_id_entry.bind("<FocusIn>", temp_user_id)
    user_id_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

    
    #Function named temp_password with one parameter i.e. 'e'
    def temp_password(e):
        '''Clears password_entry to take user input and configured password entry to show * when password is entered.'''
        password_entry.config(show="*")
        password_entry.delete(0, "end")
    #Entry Box to take Password Input from user
    password_entry = Entry(WIN, font=("Comic Sans MS", 14) , justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    password_entry.insert(0, "Password")
    #Bind Entry so that when Clicked for Input it calls temp_password
    password_entry.bind("<FocusIn>", temp_password)
    password_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
    #Log in Which when pressed calls adminlogin_validate by providing userentry as arguments
    userlogin_button = Button(WIN, font=("Comic Sans MS", 14) , justify="center", width=10, borderwidth=0, text="Log In", bg="#645394",command=lambda : userlogin_validate(WIN,user_id_entry.get(),password_entry.get()))
    userlogin_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    #Updates GUI Into TKinter Window
    WIN.mainloop()

def userlogin_validate(WIN,u,p):
    print("WIN: ", WIN)
    print("username_entry.get(): ", u)
    print("password_entry.get(): ", p)
    userlogin_validation(WIN, u, p)

#calls voterlogin function
userlogin()