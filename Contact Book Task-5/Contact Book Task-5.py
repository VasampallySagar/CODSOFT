import tkinter as tk
from tkinter import ttk, messagebox
contacts = [
    {"name": "Sagar", "phone": "9014352192", "address": "Hyderabad", "email": "sagar@gamil.com"},
    {"name": "venkat", "phone": "6304761707", "address": "Hyderabad", "email": "venkat@gmail.com"}
]
def display_contacts():
    for row in contact_list.get_children():
        contact_list.delete(row)
    for contact in contacts:
        contact_list.insert("", "end", values=(contact['name'], contact['phone'], contact['address'], contact['email']))
def add_contact():
    name = new_name.get()
    phone = new_phone.get()
    address = new_address.get()
    email = new_email.get()
    contacts.append({"name": name, "phone": phone, "address": address, "email": email})
    display_contacts()
def delete_contact():
    selected_contact = contact_list.selection()
    if selected_contact:
        for item in selected_contact:
            index = int(contact_list.index(item))
            del contacts[index]
        display_contacts()
def display_search_results(results):
    contact_list.delete(*contact_list.get_children())
    for contact in results:
        contact_list.insert("", "end", values=(contact['name'], contact['phone'], contact['address'], contact['email']))
def search_contact():
    query = search_entry.get().lower()
    search_results = []
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone'] or query in contact['email'].lower():
            search_results.append(contact)
    display_search_results(search_results)
def display_search_results(results):
    for row in contact_list.get_children():
        contact_list.delete(row)
    for contact in results:
        contact_list.insert("", "end", values=(contact['name'], contact['phone'], contact['address'], contact['email']))
def login():
    input_name = username_entry.get()
    input_pass = password_entry.get()
    if input_name == "a" and input_pass == "p":
        messagebox.showinfo("Success", "Login Successful!")
        login_frame.pack_forget()
        main_frame.pack()
        display_contacts()
    else:
        messagebox.showerror("Error", "Invalid credentials")

def logout():
    main_frame.pack_forget()
    login_frame.pack()
root = tk.Tk()
root.title("Contact Book")
login_frame = tk.Frame(root)
login_frame.pack(expand=True)
tk.Label(login_frame, text="Username: ").pack(anchor="center")
username_entry = tk.Entry(login_frame)
username_entry.pack(anchor="center")
tk.Label(login_frame, text="Password: ").pack(anchor="center")
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(anchor="center")
login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(anchor="center")

main_frame = tk.Frame(root)

contact_list = ttk.Treeview(main_frame, columns=('Name', 'Phone', 'Address', 'Email'), show='headings')
contact_list.heading('Name', text='Name')
contact_list.heading('Phone', text='Phone')
contact_list.heading('Address', text='Address')
contact_list.heading('Email', text='Email')
contact_list.pack()

logout_button = tk.Button(main_frame, text="Logout", command=logout)
logout_button.pack()

add_frame = tk.Frame(main_frame)
add_frame.pack()

tk.Label(add_frame, text="Name: ").grid(row=0, column=0)
new_name = tk.Entry(add_frame)
new_name.grid(row=0, column=1)

tk.Label(add_frame, text="Phone: ").grid(row=1, column=0)
new_phone = tk.Entry(add_frame)
new_phone.grid(row=1, column=1)

tk.Label(add_frame, text="Address: ").grid(row=2, column=0)
new_address = tk.Entry(add_frame)
new_address.grid(row=2, column=1)

tk.Label(add_frame, text="Email: ").grid(row=3, column=0)
new_email = tk.Entry(add_frame)
new_email.grid(row=3, column=1)

add_button = tk.Button(add_frame, text="Add Contact", command=add_contact)
add_button.grid(row=4, columnspan=2)

delete_frame = tk.Frame(main_frame)
delete_frame.pack()

delete_button = tk.Button(delete_frame, text="Delete Contact", command=delete_contact)
delete_button.pack()

search_frame = tk.Frame(main_frame)
search_frame.pack()

tk.Label(search_frame, text="Search: ").pack(side=tk.LEFT)
search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT)

search_button = tk.Button(search_frame, text="Search", command=search_contact)
search_button.pack(side=tk.LEFT)

root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
contacts = [
    {"name": "Venkat", "phone": "6304761707", "address": "Hyderabad", "email": "venkatvalluri@gamil.com"},
    {"name": "Shravan", "phone": "9262104328", "address": "Hyderabad", "email": "shravan@gmail.com"}
]
def display_contacts():
    for row in contact_list.get_children():
        contact_list.delete(row)
    for contact in contacts:
        contact_list.insert("", "end", values=(contact['name'], contact['phone'], contact['address'], contact['email']))
def add_contact():
    name = new_name.get()
    phone = new_phone.get()
    address = new_address.get()
    email = new_email.get()
    contacts.append({"name": name, "phone": phone, "address": address, "email": email})
    display_contacts()
def delete_contact():
    selected_contact = contact_list.selection()
    if selected_contact:
        for item in selected_contact:
            index = int(contact_list.index(item))
            del contacts[index]
        display_contacts()
def display_search_results(results):
    contact_list.delete(*contact_list.get_children())
    for contact in results:
        contact_list.insert("", "end", values=(contact['name'], contact['phone'], contact['address'], contact['email']))
def search_contact():
    query = search_entry.get().lower()
    search_results = []
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone'] or query in contact['email'].lower():
            search_results.append(contact)
    display_search_results(search_results)
def display_search_results(results):
    for row in contact_list.get_children():
        contact_list.delete(row)
    for contact in results:
        contact_list.insert("", "end", values=(contact['name'], contact['phone'], contact['address'], contact['email']))
def login():
    input_name = username_entry.get()
    input_pass = password_entry.get()
    if input_name == "a" and input_pass == "p":
        messagebox.showinfo("Success", "Login Successful!")
        login_frame.pack_forget()
        main_frame.pack()
        display_contacts()
    else:
        messagebox.showerror("Error", "Invalid credentials")

def logout():
    main_frame.pack_forget()
    login_frame.pack()
root = tk.Tk()
root.title("Contact Book")
login_frame = tk.Frame(root)
login_frame.pack(expand=True)
tk.Label(login_frame, text="Username: ").pack(anchor="center")
username_entry = tk.Entry(login_frame)
username_entry.pack(anchor="center")
tk.Label(login_frame, text="Password: ").pack(anchor="center")
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(anchor="center")
login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(anchor="center")

main_frame = tk.Frame(root)

contact_list = ttk.Treeview(main_frame, columns=('Name', 'Phone', 'Address', 'Email'), show='headings')
contact_list.heading('Name', text='Name')
contact_list.heading('Phone', text='Phone')
contact_list.heading('Address', text='Address')
contact_list.heading('Email', text='Email')
contact_list.pack()

logout_button = tk.Button(main_frame, text="Logout", command=logout)
logout_button.pack()

add_frame = tk.Frame(main_frame)
add_frame.pack()

tk.Label(add_frame, text="Name: ").grid(row=0, column=0)
new_name = tk.Entry(add_frame)
new_name.grid(row=0, column=1)

tk.Label(add_frame, text="Phone: ").grid(row=1, column=0)
new_phone = tk.Entry(add_frame)
new_phone.grid(row=1, column=1)

tk.Label(add_frame, text="Address: ").grid(row=2, column=0)
new_address = tk.Entry(add_frame)
new_address.grid(row=2, column=1)

tk.Label(add_frame, text="Email: ").grid(row=3, column=0)
new_email = tk.Entry(add_frame)
new_email.grid(row=3, column=1)

add_button = tk.Button(add_frame, text="Add Contact", command=add_contact)
add_button.grid(row=4, columnspan=2)

delete_frame = tk.Frame(main_frame)
delete_frame.pack()

delete_button = tk.Button(delete_frame, text="Delete Contact", command=delete_contact)
delete_button.pack()

search_frame = tk.Frame(main_frame)
search_frame.pack()

tk.Label(search_frame, text="Search: ").pack(side=tk.LEFT)
search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT)

search_button = tk.Button(search_frame, text="Search", command=search_contact)
search_button.pack(side=tk.LEFT)

root.mainloop()
