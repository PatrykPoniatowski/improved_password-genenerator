from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:
            {
                "email": email,
                "password": password,
            }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    user_input = website_entry.get()
    if len(user_input) == 0:
        messagebox.showinfo(title="Oops", message="The field is empty, please sure to add searched website")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                website_data = data[user_input]
        except FileNotFoundError:
            messagebox.showinfo(title="File not found", message="The data file is not found")
        except KeyError:
            messagebox.showinfo(title="Website not found", message="The website is not found")
        else:
            email = website_data["email"]
            password = website_data["password"]
            messagebox.showinfo(title=f"{user_input}", message=f"Email: {email}\nPassword: {password}")
        finally:
            website_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0, sticky=W)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0, sticky=W)
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, sticky=W)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=W)

# Buttons
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=2, sticky=E)
generate_password_button = Button(text="Generate Password", width=17, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky=E)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

window.mainloop()
