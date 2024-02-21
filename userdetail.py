from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from stegano import lsb
import json 

def return_adminhomepage(WIN):
    WIN.destroy()
    from admin_dashboard import homepage
    homepage()

def show_error(title, message):
    messagebox.showerror(title, message)

def viewusers():
    WIN_viewvuser = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN_viewvuser.iconphoto(False, logo_image)
    WIN_viewvuser.title('Online Banking System')
    WIN_viewvuser.geometry('360x640')

    background = PhotoImage(file="images/user detail.png")  # Assuming you have a background for user details
    label_background = Label(WIN_viewvuser, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    tv = ttk.Treeview(WIN_viewvuser, show='tree', height=16)
    # Set theme of TreeView as Default
    ttk.Style().theme_use("default")
    # Configured Properties of Tree View
    ttk.Style().configure("Treeview", background="#645394", foreground="white", fieldbackground="#645394",
                          rowheight=35, font=("Comic Sans MS", 15), highlightthickness=0, bd=0, padding=10, columns=1)
 
    tv = ttk.Treeview(WIN_viewvuser, columns=('Name', 'Phone'), show='headings', height=10)
    tv.pack(padx=20, pady=(230,0))

    def show_user_details(event):
        selected_item = tv.selection()[0]  # Get selected item
        user_data = tv.item(selected_item)['values']

        # Assuming the user details are in the same order as your print statement
        detail_message = f"Name: {user_data[0]}\nCitizenship: {user_data[1]}\nPhone: {user_data[2]}\nAddress: {user_data[3]}\nEmail: {user_data[4]}\nAccount Type: {user_data[5]}\nAccount Number: {user_data[6]}"
        messagebox.showinfo("User Details", detail_message)

    tv.bind("<Double-1>", show_user_details)

    image_path = "images/profileimg.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)

    detailedlist = decoded_data['users']

    for user in detailedlist:
        tv.insert('', 'end', values=user)

    return_button = Button(WIN_viewvuser, borderwidth=0, command=lambda: return_adminhomepage(WIN_viewvuser))
    return_button.place(x=4, y=5)

    WIN_viewvuser.mainloop()

viewusers()
