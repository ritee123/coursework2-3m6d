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
    
def userlogin_validation(voter_idtemp_voter_id):
    image_path = "images/profileimg.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)



    voter_idtemp_voter_id = int(voter_idtemp_voter_id)
    
    for i in decoded_data["users"]:
        if i[5] == voter_idtemp_voter_id and i[6] == True:
            title = "Error"
            message = "You have \n Already Voted"
            from errors import error as show_error
            show_error(title,message)
            return False
        elif i[5] == voter_idtemp_voter_id and i[6] == False:
            i[6] = True
            json_data = json.dumps(decoded_data)
            encoded_image = lsb.hide(image_path, json_data)
            # Save the output image
            encoded_image.save(image_path)
            return True
    
    return False
    

def confirm_voter(WIN,voter_idtemp_voter_id):
    record = []  # Define the variable record

    if userlogin_validation(voter_idtemp_voter_id):
        # Destroys the tkinter window and call open_profile function i.e. profile_view function from a profile page
        WIN.destroy()
        from addvote import viewcandidate
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
    background = PhotoImage(file="images/Additionaluser.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 350 and 300 respectively.
    w = Canvas(WIN, width=350, height=280, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 350 and 300
    w.create_rectangle(0, 0, 350, 300, fill="#FFFFFF", outline='#000000')
    w.pack(padx=40, pady=(290,0))
   

    #Function named temp_voter_id with one parameter i.e. 'e'
    def temp_voter_id(e):
        '''Clears voter_idtemp_voter_id_entry to take user input'''
        voter_idtemp_voter_id_entry.delete(0, "end")

    #Entry Box to  take voter_idtemp_voter_id Input from user
    voter_idtemp_voter_id_entry = Entry(WIN, font=("Comic Sans MS", 14) , justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    voter_idtemp_voter_id_entry.insert(2, "Mobile Number")
    #Bind Entry so that when Clicked for Input it calls temp_voter_id
    voter_idtemp_voter_id_entry.bind("<FocusIn>", temp_voter_id)
    voter_idtemp_voter_id_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

    
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
    userlogin_button = Button(WIN, font=("Comic Sans MS", 14) , justify="center", width=10, borderwidth=0, text="Log In", bg="#645394",command=lambda : userlogin_validate(WIN,username_entry.get(),password_entry.get()))
    userlogin_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    #Updates GUI Into TKinter Window
    WIN.mainloop()

#calls voterlogin function
userlogin()