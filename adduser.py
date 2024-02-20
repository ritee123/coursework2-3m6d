import json
from tkinter import *
import random
from stegano import lsb
import re
import requests
from tkinter import ttk 

def dashboard_call(WIN):
    '''Destroys the tkinter window and call open function i.e. login function from a admin page'''
    WIN.destroy()
    from admin_dashboard import homepage
    homepage()

def is_valid_email(email):
    # Regular expression for validating an email
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def addnewuser_validation(name_entry, citizenship_entry, phone_entry, address_entry, email_entry, account_type_entry):
    print("Name:", name_entry.get())
    print("Citizenship:", citizenship_entry.get())
    print("Phone:", phone_entry.get())
    print("Address:", address_entry.get())
    print("Account Type:", account_type_entry.get())
    print("Email:", email_entry.get())

    # Validation logic for the user inputs including account type
    if (
        len(name_entry.get()) != 0 and isinstance(name_entry.get(), str) and
        len(citizenship_entry.get()) != 0 and citizenship_entry.get().isdigit() and
        len(phone_entry.get()) == 10 and phone_entry.get().isdigit() and
        len(address_entry.get()) != 0 and isinstance(address_entry.get(), str) and
        len(account_type_entry.get()) != 0 and isinstance(account_type_entry.get(), str) and
        is_valid_email(email_entry.get())
    ):
        print("Validation passed")
        return True
    else:
        print(len(name_entry.get()) != 0 and isinstance(name_entry.get(), str))
        print(len(citizenship_entry.get()) != 0 and citizenship_entry.get().isdigit())
        print(len(phone_entry.get()) == 10 and phone_entry.get().isdigit())
        print(len(address_entry.get()) != 0 and isinstance(address_entry.get(), str))
        print(len(account_type_entry.get()) != 0 and isinstance(account_type_entry.get(), str))
        print(is_valid_email(email_entry.get()))
        print("Validation failed")
        return False

    
def send(account_number,PIN,phone):
    try:
        to_phone = phone['phoneNumber']
        # Call an api and send parameter to it
        r = requests.get(
            "http://api.sparrowsms.com/v2/sms/",
            params={
                'token': 'v2_Rri05e6U3XkCcnmjeOnfxdDzAqz.dY9a',
                'from': 'TheAlert',
                'to': to_phone,
                'text': f'Dear User, welcome to Kuber! Your PIN is {PIN}, and your saving account number is {account_number}. Please do not share your banking details with anyone.'
            }
        )
        print("R: ", r)
        status_code = r.status_code
        response = r.text
        response_json = r.json()
    except Exception as e:
        print(f"Error sending message: {str(e)}")    

def create_new_user(WIN, name_entry, citizenship_entry, phone_entry, address_entry, email_entry, account_type_entry):
    # Extracting the data from the entry fields
    name = name_entry.get()
    citizenship = citizenship_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    account_type = account_type_entry.get()
    account_number = random.randint(10000, 99999)
    PIN = random.randint(10000, 99999)
    
    if addnewuser_validation(name_entry, citizenship_entry, phone_entry, address_entry, email_entry, account_type_entry):
        image_path = "images/profileimg.png"
        print("Image Path:", image_path)  # Add this line to print the image path
        decoded_data = ""
        try:
            decoded_data = lsb.reveal(image_path)
        except:
            print("Image Reveal Not Success...")

        if decoded_data != "":
            banking_system = json.loads(decoded_data)
        else:
            banking_system = {}

        # Check if 'users' key exists, if not, initialize it
        if "users" not in banking_system:
            banking_system["users"] = []   

        # Adding the new user data
        new_data = [name, citizenship, phone, address, email, account_type ,account_number, PIN]
        banking_system["users"].append(new_data)

        phone_data = {'phoneNumber': '+977' + phone}
        send(PIN,account_number,phone_data)
        json_data = json.dumps(banking_system)
        # Encode the JSON data into the image using least significant bit (LSB) method
        encoded_image = lsb.hide(image_path, json_data)
        # Save the output image
        encoded_image.save(image_path)
        confirm_account_creation(WIN)
    else:
        # If data is not valid, display an error message
        title = "Error"
        message = "Recheck Your Input\n Values"
        from errors import error as show_error
        show_error(title,message)

def confirm_account_creation(WIN):
    WIN_top = Toplevel(bg='#E0D9EF')
    WIN_top.title('Account Confirmation')
    WIN_top.geometry('300x150')

    font_properties = ("Comic Sans MS", 15)

    def close_windows():
        WIN_top.destroy()
        WIN.destroy()
        from admin_dashboard import homepage
        homepage()

    confirmation_message = "Account has been successfully \n created!"
    message_label = Label(WIN_top, bg='#E0D9EF', text=confirmation_message, font=font_properties, justify="center", foreground="#000000")
    message_label.pack()

    ok_button = Button(WIN_top, text=" OK ", bg='#FFFFFF', fg="Black", font=("Comic Sans MS", 12), command=close_windows)
    ok_button.place(x=108, y=80)

    WIN_top.mainloop()


def show_error(title, message):
    WIN_top = Toplevel(bg='#E0D9EF')
    WIN_top.title(title)
    WIN_top.geometry('300x150')

    font_properties = ("Comic Sans MS", 15)

    def close_windows():
        WIN_top.destroy()

    message_label = Label(WIN_top, bg='#E0D9EF', text=message, font=font_properties, justify="center", foreground="#000000")
    message_label.pack()

    ok_button = Button(WIN_top, text=" OK ", bg='#FFFFFF', fg="Black", font=("Comic Sans MS", 12), command=close_windows)
    ok_button.place(x=108, y=80)

    WIN_top.mainloop()


def return_adminhomepage(WIN):
    WIN.destroy()
    from admin_dashboard import homepage
    homepage()

    button_image = PhotoImage(file="images/arrow.png")
    button = Button(WIN, image=button_image, borderwidth=0, width=30, height=30,command = lambda:return_adminhomepage(WIN))
    button.place(x=4, y=5)

 
def add_new_user():
    print("********************* Add New User Page *** Opens Here *********************")
    WIN = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN.iconphoto(False, logo_image)
    WIN.title('Online Banking System')
    WIN.geometry('360x640')
   
    background = PhotoImage(file="images/adduser.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    w = Canvas(WIN, width=280, height=4255, borderwidth=0, highlightthickness=0)
    w.create_rectangle(0, 0, 280, 500, fill="#9867C5", outline='#6E0042')
    w.pack(padx=30, pady=(170,3))
    button_image = PhotoImage(file="images/arrow.png")
    button = Button(WIN, image=button_image, borderwidth=0, width=30, height=30,command = lambda:dashboard_call(WIN))
    button.place(x=4, y=5)


    def temp_name(e):
        name_entry.delete(0, "end")

    # Entry Box to take name Input from user
    name_entry = Entry(WIN, font=("Comic Sans MS", 15), justify="center", width=18, foreground="#AFAFAF")
    name_entry.insert(0, "Full Name")
    name_entry.bind("<FocusIn>",temp_name)
    name_entry.place(relx=0.5, rely=0.3, anchor=CENTER)
   

    def temp_citizenship(e):
        '''Clears citizenship_entry to take user input'''
        citizenship_entry.delete(0, "end")

    citizenship_entry = Entry(WIN, font=("Comic Sans MS", 15), justify="center", width=18, foreground="#AFAFAF")
    citizenship_entry.insert(1, "Citizenship Number")
    citizenship_entry.bind("<FocusIn>",temp_citizenship)
    citizenship_entry.place(relx=0.5, rely=0.4, anchor=CENTER)


    def temp_phone(e):
        '''Clears phone_entry to take user input'''
        phone_entry.delete(0, "end")

    phone_entry = Entry(WIN, font=("Comic Sans MS", 15), justify="center", width=18, foreground="#AFAFAF")
    phone_entry.insert(2, "Phone Number")
    phone_entry.bind("<FocusIn>",temp_phone)
    phone_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

    
    def temp_address(e):
        '''Clears citizenship_entry to take user input'''
        address_entry.delete(0, "end")

    address_entry = Entry(WIN, font=("Comic Sans MS", 15), justify="center", width=18, foreground="#AFAFAF")
    address_entry.insert(3, "Address")
    address_entry.bind("<FocusIn>",temp_address)
    address_entry.place(relx=0.5, rely=0.6, anchor=CENTER)
    
    def temp_email(e):
        '''Clears DOB entry to take user input'''
        email_entry.delete(0, "end")


    email_entry = Entry(WIN, font=("Comic Sans MS", 15), justify="center", width=18, foreground="#AFAFAF")
    email_entry.insert(4, "Email")
    email_entry.bind("<FocusIn>",temp_email)
    email_entry.place(relx=0.5, rely=0.7, anchor=CENTER)

    def temp_account_type(e):
        '''Clears account_type_entry to take user input'''
        account_type_entry.delete(0, "end")

    # Define the options for account type
    account_types = ['Saving Account', 'Checking Account']  # Add more account types as needed
    account_type_entry = ttk.Combobox(WIN, values=account_types, font=("Comic Sans MS", 14), justify="center", width=18, foreground="#AFAFAF")
    account_type_entry.set('Select Account Type')  # Default placeholder text

    account_type_entry.place(relx=0.5, rely=0.8, anchor=CENTER)  
    
    # created a add_new_voter Button which calls add_new_voter_page function when pressed
    add_new_user_button = Button(WIN,text="Add User",padx=13,borderwidth=0,
                                 font=("Comic Sans MS", 14),background= '#645394', 
                                 foreground= 'white',
                                 command=lambda:create_new_user(WIN,name_entry,citizenship_entry,
                                                                phone_entry,address_entry, 
                                                                email_entry, account_type_entry))
    add_new_user_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    def on_enter_add_new_user_button(e):
        '''Changed Background and Foreground of add_new_voter Button named add_new_voter_button
        to #ABBC41 and white respectively when function is called.'''
        add_new_user_button.config(background='#7409EB',foreground= "white")

    def on_leave_add_new_user_button(e):
        add_new_user_button.config(background= '#645394', foreground= 'white')
    add_new_user_button.bind('<Enter>',on_enter_add_new_user_button)
    add_new_user_button.bind('<Leave>',on_leave_add_new_user_button)
    
    # places all GUI into Tkinter Window
    WIN.mainloop()


add_new_user()