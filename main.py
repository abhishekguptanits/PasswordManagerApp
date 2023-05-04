from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    generated_password = "".join(password_list)
    pyperclip.copy(generated_password)
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_dict = {
        website: {
            "email": email,
            "password": password
        }
    }

    # if len(website) <= 0 or len(email) <= 0 or len(password) <= 0:
    #     messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    # else:
    #     with open("data.json", mode="w") as file:
    #         # # Write json data to file
    #         # json.dump(obj=new_dict, fp=file, indent=4)
    #
    #         # # Read json data from file
    #         # data = json.load(fp=file)
    #         # print(data)
    #         # print(type(data))
    #
    #         # Update json data in a file
    #         data = json.load(fp=file)
    #         data.update(new_dict)
    #         json.dump(obj=data, fp=file, indent=4)

    if len(website) <= 0 or len(email) <= 0 or len(password) <= 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(fp=file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(obj=new_dict, fp=file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_dict)
            with open("data.json", mode="w") as file:
                # Saving updated data
                json.dump(obj=data, fp=file, indent=4)
        finally:
            messagebox.showinfo(title="Credentials Saved", message="Your credentials are saved successfully")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "aryan@gmail.com")
            password_entry.delete(0, END)


# ---------------------------- Search Password ------------------------------- #

# def search():
#     website = website_entry.get()
#     try:
#         with open("data.json", 'r') as file:
#             data = json.load(fp=file)
#             try:
#                 credentials = data[website]
#             except KeyError as error_msg:
#                 messagebox.showerror(title="Record not found", message=f"Key {error_msg} doesn't exist, Try again "
#                                                                        f"with different input OR add new details")
#             else:
#                 messagebox.showinfo(title=f"{website}",
#                                     message=f"Email: {credentials['email']}\nPassword: {credentials['password']}")
#     except FileNotFoundError:
#         messagebox.showerror(title="No data exist", message="No data has been saved yet. "
#                                                             "Try with adding new data first")


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data has been saved yet. Try with adding new data first")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No data found for '{website}', "
                                                       f"Try again with different input OR add new details")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entrys / Inputs
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=38)
email_entry.insert(0, "aryan@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", bg="#654E92", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
