#Imported Necessary Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from stegano import lsb
import json


def dashboard_call(WIN):
    '''Destroys the tkinter window and call open function i.e. login function from a admin page'''
    WIN.destroy()
    from adminloginfirst import adminlogin
    adminlogin()


def homepage():
    WIN = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN.iconphoto(False, logo_image)
    WIN.title('Online Banking System')
    WIN.geometry('360x640')

    bg_img = Image.open('images/Adminfirst.png')
    bg_img = ImageTk.PhotoImage(bg_img)
    canvas = Canvas(WIN, width=bg_img.width(), height=bg_img.height())
    canvas.pack()
    canvas.create_image(0, 0, image=bg_img, anchor='nw')
    canvas.create_text(105, 445, text="Total Users", fill="white", font=("Comic Sans MS", 12))

    image_path = "images/profileimg.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)
    detailedlist = decoded_data['users']
    user_counts = str(len(detailedlist))

    canvas.create_text(185, 515, text=user_counts, fill="white", font=("Arial", 90))
    
    button_image = PhotoImage(file="images/arrow.png")
    button = Button(WIN, image=button_image, borderwidth=0, width=30, height=30,command = lambda:dashboard_call(WIN))
    button.place(x=4, y=5)

    
    # created a function named login_page
    def add_user_page():
        print("************************Login Page opens here...")
        WIN.destroy()
        from adduser import add_new_user
        add_new_user()
        
    def user_list_page():
        WIN.destroy()
        from user_list import view_users
        view_users()
    
    def detail_users_page():
         WIN.destroy()
         from userdetail import viewusers
         viewusers()


    def on_enter_add_user(e):
        add_user.config(background='#7409EB',foreground= "white")


    def on_leave_add_user(e):
        add_user.config(background= '#645394', foreground= 'white')

   
    add_user = Button(WIN,text="Register User",padx=13,borderwidth=0,font=("Comic Sans MS", 12),background='#645394',foreground='white',command=lambda:add_user_page())
    add_user.place(relx=0.3, rely=0.5, anchor=CENTER)
    add_user.bind('<Enter>',on_enter_add_user)
    add_user.bind('<Leave>',on_leave_add_user)

    def on_enter_detail_users(e):
        detail_users.config(background='#7409EB',foreground= "white")

    # Created a Function named on_leave_view_voter with 'e' as one parameter
    def on_leave_detail_users(e):
        detail_users.config(background= '#645394', foreground= 'white')

    detail_users= Button(WIN,text="User Detail",padx=13,borderwidth=0,font=("Comic Sans MS", 12),background= '#645394', foreground= 'white',command=lambda:detail_users_page())
    detail_users.place(relx=0.7, rely=0.5, anchor=CENTER)
    detail_users.bind('<Enter>',on_enter_detail_users)
    detail_users.bind('<Leave>',on_leave_detail_users)



    def on_enter_user_list(e):
        user_list.config(background='#7409EB',foreground= "white")
    def on_leave_user_list(e):
         user_list.config(background= '#645394', foreground= 'white')

    user_list= Button(WIN,text="User list",padx=13,borderwidth=0,font=("Comic Sans MS", 12),background= '#645394', foreground= 'white',command=lambda:user_list_page())
    user_list.place(relx=0.5, rely=0.6, anchor=CENTER)
    user_list.bind('<Enter>',on_enter_user_list)
    user_list.bind('<Leave>',on_leave_user_list)


    #Updates all Into TKinter Window
    WIN.mainloop()

#calls homepage Function
homepage()