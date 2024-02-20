from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from stegano import lsb
import json 


def data_not_found():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Username Not Found"
    message = "Input Username was\n not Found"
    from errors import error as show_error
    show_error(title, message)


def return_adminhomepage(WIN):
    WIN.destroy()
    from admin_dashboard import admin_homepage
    admin_homepage()


def viewuser():
    '''Created a Tkinter Window named WIN_viewvoter and placed logo_image as icon photo.
    Similarly,Adding Title to the window and Providing Geometry to the window.'''
    WIN_viewvuser = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN_viewvuser.iconphoto(False, logo_image)
    WIN_viewvuser.title('Online Banking System')
    WIN_viewvuser.geometry('360x640')

    # Placed backround_top.png image as Background to a Tkinter Window
    background = PhotoImage(file="images/removeuser.png")
    label_background = Label(WIN_viewvuser, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    # Created a Canvas with width and height of 240 and 400 respectively.
    w = Canvas(WIN_viewvuser, width=320, height=430, borderwidth=0, highlightthickness=0)
    # Created a Rectangle in a Canvas with width and height of 240 and 400
    w.create_rectangle(0, 0, 320, 600, fill="#645394", outline='#edd09f')
    w.pack(padx=(20), pady=(190, 0))

    tv = ttk.Treeview(WIN_viewvuser, show='tree', height=9)
    # Set theme of TreeView as Default
    ttk.Style().theme_use("default")
    # Configured Properties of Tree View
    ttk.Style().configure("Treeview", background="#645394", foreground="white", fieldbackground="#645394",
                          rowheight=31, font=("Comic Sans MS", 12), highlightthickness=0, bd=0, padding=10, columns=1)
    ttk.Style().map("Treeview", background=[('selected', '#645394')], foreground=[('selected', 'white')])
    tv['columns'] = ('Name', 'Age')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Name', anchor=W, width=140)
    tv.column('Age', anchor=E, width=98)

    def search():
        try:
            # for loop which runs till there is a value in orginal_voterlist list
            for value in orginal_userlist:
                # looks if user entered username is there in list
                if username_search.get() == value[0]:
                    # deletes all data shown in viewvoter
                    for item in tv.get_children():
                        tv.delete(item)
                    # show Data of Found User Only
                    tv.insert(parent='', index=1, iid=1, text='', values=value)
                    # breaks the loop
                    break
                # if entered username is not matched with value and is blank then this executes
                elif username_search.get() == "":
                    # Deletes All Data of voterlist
                    for item in tv.get_children():
                        tv.delete(item)
                    b = 1
                    for data in userlist:
                        tv.insert(parent='', index=b, iid=b, text='', values=data)
                        b = b + 1
                    # breaks loop
                    break
            # if value is not found in orginal_voterlist list
            else:
                # raises a Error
                raise ValueError('Value Not found')
        # runs this part of code if error occurred
        except:
            # Calls data_not_found
            data_not_found()

    def remove_user():
        # Get the selected item from the TreeView
        selected_item = tv.selection()
        if selected_item:
            # Get the index of the selected item
            index = int(selected_item[0])
            
            # Remove the selected user from orginal_userlist and tv
            del orginal_userlist[index]
            tv.delete(selected_item)
            
            # Update userlist to match orginal_userlist
            userlist.clear()
            userlist.extend(orginal_userlist)
            
        else:
            messagebox.showinfo("Error", "Please select a user to remove.")

    username_search = Entry(WIN_viewvuser, font=("Comic Sans MS", 11), justify="center", width=15, foreground="#AFAFAF")
    username_search.place(relx=0.4, rely=0.4, anchor=CENTER)

    def temp_username(e):
        '''Clears phone_entry to take user input'''
        username_search.delete(0, "end")

    username_search.bind("<FocusIn>", temp_username)
    # Text Displayed in Entry bar so User Know What to look for
    username_search.insert(1, "Enter User Name")
    # Search button which when pressed calls search
    search_button = Button(WIN_viewvuser, text="Search", padx=9, borderwidth=0, font=("Comic Sans MS", 9), width=6,
                           background='#d98d0b', foreground='black', command=search)
    search_button.place(relx=0.7, rely=0.4, anchor=CENTER)

    image_path = "images/profileimg.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)

    # Created voterlist as blank list
    detailedlist = decoded_data['Voter']

    userlist = []
    # for loop to go through every value of detailedlist
    for voter in reversed(detailedlist):
        name = (voter[0], voter[1])
        # append it into voterlist
        userlist.append(name)

    # duplicates voterlist list into original_voterlist
    orginal_userlist = userlist.copy()
    # Calculated length of list
    orginal_length = len(userlist)
    # Check if Statement is Correct or not
    if orginal_length > 7:
        # stores new length as how much orginal_length is more than 7
        new_length = orginal_length - 7
        # Calls for loop to pop all items after index 7
        for i in range(new_length):
            userlist.pop()

    a = 0
    # insert Data from a list of voterlist
    for data in userlist:
        tv.insert(parent='', index=a, iid=a, text='', values=data)
        a = a + 1
    tv.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Load the image (ensure the image is in the same directory as your script or provide a full path)
    return_image = PhotoImage(file="images/arrow.png")
    return_button = Button(WIN_viewvuser, image=return_image, borderwidth=0,
                           command=lambda: return_adminhomepage(WIN_viewvuser))
    return_button.image = return_image
    return_button.place(x=4, y=5)

    remove_button = Button(WIN_viewvuser, text="Remove", padx=9, borderwidth=0, font=("Comic Sans MS", 9),
                           background='#d98d0b', foreground='black', command=remove_user)
    remove_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    # Places all GUI of Tkinter Window into it.
    WIN_viewvuser.mainloop()


# Calls viewvoter Function
viewuser()
