import tkinter as tk
# import PIL.Image
# import PIL.ImageTk
# import cv2
# from functools import partial
import threading
# import imutils
import web
import portscanner
import dir_search
import waybackurl
from tkinter import ttk
import os
from tkinter import *

# from functools import partial

set_width = 900
set_height = 600

root = tk.Tk()
root.title('Web Enumeration')
root.geometry("900x600")
root.minsize(800, 500)
background = PhotoImage(file="images/WEB ENUMERATION.png")
label_background = Label(root,image=background,borderwidth=0)
label_background.place(x=0,y=0)
# root.configure()

def print_search():
    l1.config(text=f"Target: {search.get()}")
    target = search.get()
    target = target.replace("http://", "").replace("www.", "").replace("https://", "")

    # Remove invalid characters from the target
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in invalid_chars:
        target = target.replace(char, '_')

    result_directory = os.path.join(os.getcwd(), "result")
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)
    target_directory = os.path.join(result_directory, target)
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)


search = tk.StringVar()
f1 = tk.Frame(root)  
entry_search = tk.Entry(f1, textvariable=search, width=55, font="comicsansms 13 italic")
entry_search.pack(side='left', padx = 6)  
button_print = tk.Button(f1, text="Print", command=print_search, font="comicsansms 9 italic",fg='white',bg='#721417', borderwidth=0.5, highlightthickness=0.5)
button_print.pack(side='left', padx=6)  
l1 = tk.Label(root, text="Target:", font="comicsansms 13 italic",fg='white',bg='#721417',borderwidth=0, highlightthickness=0)
f1.place(relx=0.5, rely=0.11, anchor='n')
l1.place(relx=0.2, rely=0.19, anchor='w')



from1 = tk.StringVar()
to1 = tk.StringVar()
thread1 = tk.StringVar()
email_link = tk.StringVar()
Checkbutton1 = tk.IntVar()
x11 = 0
x12 = 0
x13 = 0
x14 = 0
x15 = 0
x16 = 0


def port_scanner_btn():
    s = search.get()
    if s.startswith("http://"):
        s = s[7:]
    if s.startswith("https://"):
        s = s[8:]
    # print(s)
    portscanner.target = s
    a = int(from1.get())
    b = int(to1.get())
    x = int(thread1.get())
    t1 = threading.Thread(target=portscanner.portscanner, args=(x, a, b))
    # portscanner.portscanner(x, a, b)  # port scanning
    # t1.start()

    global x11
    if x11 == 0:
        x11 = 0
        t1.start()
        # portscanner.portscanner(x, a, b)

def Port_Scan():
    port_scan_frame = tk.Frame(root, bg='#721417') 
    tk.Label(port_scan_frame, text="PORT SCAN", font="comicsansms 16 bold",fg='white', bg='#721417').pack(pady=(10, 5))
    port_range_frame = tk.Frame(port_scan_frame, bg='#721417')
    tk.Label(port_range_frame, text="Port Range:", font="comicsansms 13", fg='white',bg='#721417').pack(side='left', padx=10)
    tk.Label(port_range_frame, text="From=", font="comicsansms 13", fg='white',bg='#721417').pack(side='left')
    tk.Entry(port_range_frame, textvariable=from1, width=15, font="comicsansms 13 italic").pack(side='left', padx=10)
    tk.Label(port_range_frame, text="To=", font="comicsansms 13",fg='white', bg='#721417').pack(side='left')
    tk.Entry(port_range_frame, textvariable=to1, width=15, font="comicsansms 13 italic").pack(side='left', padx=10)
    tk.Label(port_range_frame, text="Threads=", font="comicsansms 13", fg='white',bg='#721417').pack(side='left', padx=10)
    tk.Entry(port_range_frame, textvariable=thread1, width=15, font="comicsansms 13 italic").pack(side='left')
    port_range_frame.pack(fill='x', pady=(0, 10))  
    tk.Button(port_range_frame, text="Scan", command=port_scanner_btn, font="comicsansms 13 italic", fg="white", bg='#721417').pack(side='left', pady=10)
    port_scan_frame.place(relx=0.5, rely=0.25, anchor='n') 


def email_btn():
    # print(email_link.get())
    web.a1 = search.get()
    web.argument = int(email_link.get())
    t1 = threading.Thread(target=web.scrap_emails)  # email scraping
    global x12
    if x12 == 0:
        x12 = 0
        t1.start()   
        # web.scrap_emails()

def email():
    global email_link
    email_scraper_frame = tk.Frame(root, bg='#721417') 
    tk.Label(email_scraper_frame, text="EMAIL SCRAPER", font="comicsansms 16 bold", fg='white', bg='#721417').pack(pady=(10, 5))
    email_input_frame = tk.Frame(email_scraper_frame, bg='#721417')
    tk.Label(email_input_frame, text="Number of Links:", font="comicsansms 13", fg='white', bg='#721417').pack(side='left', padx=10)
    tk.Entry(email_input_frame, textvariable=email_link, width=15, font="comicsansms 13 italic").pack(side='left', padx=10)
    email_input_frame.pack(fill='x', pady=(0, 10)) 
    tk.Button(email_input_frame, text="Search", command=email_btn, font="comicsansms 13 italic", fg="white", bg='#721417').pack(side='left', pady=10)
    email_scraper_frame.place(relx=0.5, rely=0.48, anchor='n')  
    


def cert():
    s = search.get()
    if s.startswith("http://"):
        s = s[7:]
    if s.startswith("https://"):
        s = s[8:]
    web.a1 = s
    t1 = threading.Thread(target=web.subdomain_crtsh) 
    global x13
    if x13 == 0:
        x13 = 0
        t1.start()
      


def dns_dumpster():
    s = search.get()
    if s.startswith("http://"):
        s = s[7:]
    if s.startswith("https://"):
        s = s[8:]
    if s.startswith("www."):
        s = s[4:]
    web.a1 = s
    t1 = threading.Thread(target=web.dns_dumpster) 
    global x14
    if x14 == 0:
        x14 = 0
        t1.start()
        # web.dns_dumpster()


def subdomain():
    subdomain_frame = tk.Frame(root, bg='#721417')  
    tk.Label(subdomain_frame, text="FIND SUBDOMAIN", font="comicsansms 16 bold", fg='white', bg='#721417').pack(pady=(10, 5))
    subdomain_button_frame = tk.Frame(subdomain_frame, bg='#721417')
    tk.Button(subdomain_button_frame, text="Find from cert.sh", command=cert, font="comicsansms 13 italic", fg="white", bg='#721417').pack(side='left', padx=10)
    tk.Button(subdomain_button_frame, text="Find from DNSDumpster", command=dns_dumpster, font="comicsansms 13 italic", fg="white", bg='#721417').pack(side='left', padx=10)
    subdomain_button_frame.pack(pady=(0, 10)) 
    subdomain_frame.place(relx=0.25, rely=0.7, anchor='n')  



def way_back_btn():
    waybackurl.a1 = search.get()
    t1 = threading.Thread(target=waybackurl.way_back_url)  # web.archive.org  way back urls
    global x15
    if x15 == 0:
        x15 = 0
        t1.start()
        # waybackurl.way_back_url()


def way_back():
    way_back_frame = tk.Frame(root, bg='#721417')  
    tk.Label(way_back_frame, text="WAY BACK URLs:", font="comicsansms 16 bold", fg='white', bg='#721417').pack(side='left', pady=10)
    tk.Button(way_back_frame, text="Find", command=way_back_btn, font="comicsansms 13 italic", fg="white", bg='#721417').pack(side='left', padx=10)
    way_back_frame.place(relx=0.5, rely=0.9, anchor='n')  


directory_lists = [
    "apache-user-enum-1.0",
    "directory-list-1.0",
    "directory-list-2.3-medium",
    "directory-list-2.3-small_edited",
    "directory-list-2.3-small_original",
    "directory-list-lowercase-2.3-medium",
    "directory-list-lowercase-2.3-small"
]

def dirsearch_btn():
    dir_search.url = search.get()
    selected_index = directory_lists.index(dropdown_var.get())
    
    if 0 <= selected_index < len(directory_lists):
        s = directory_lists[selected_index]
    else:
        s = "directory-list-2.3-small_edited"
    
    dir_search.s = s
    dir_search.run()

def dir_search11():
    dir_search_frame = tk.Frame(root, bg='#721417') 
    tk.Label(dir_search_frame, text="DIRECTORY S", font="comicsansms 16 bold", fg='white', bg='#721417').pack(pady=10)
    dir_search_subframe = tk.Frame(dir_search_frame, bg='#721417')
    tk.Label(dir_search_subframe, text="Wordlist:", font="comicsansms 13", fg='white', bg='#721417').pack(side='left', padx=10)
    global dropdown_var
    dropdown_var = tk.StringVar()
    dropdown = ttk.Combobox(dir_search_subframe, textvariable=dropdown_var, values=directory_lists, state="readonly")
    dropdown.set("Select Directory List")
    dropdown.pack(side='left', fill='x', expand=True, padx=10)
    tk.Button(dir_search_subframe, text="Dirsearch", command=dirsearch_btn, font="comicsansms 13 italic", fg="white", bg='#721417').pack(side='left', padx=10)
    dir_search_subframe.pack(fill='x', pady=(0, 10))
    dir_search_frame.place(relx=0.8, rely=0.7, anchor='n') 





Port_Scan()
email()
subdomain()
way_back()
dir_search11()
root.mainloop()
