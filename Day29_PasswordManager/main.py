from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)

    pwd_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pwd_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Oops", message="Please make sure you havent left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                pwd_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column = 1, row = 0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row = 1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row = 2)
password_label = Label(text="Password:")
password_label.grid(column=0, row = 3)

#Entries
# web_entry = Text(window, height=2, width=35)
# web_entry.grid(column=1, row = 1, columnspan = 2)
# web_entry.focus()
# email_entry = Text(window, height=2, width=35)
# email_entry.grid(column=1, row = 2, columnspan = 2)
# email_entry.insert(END, "shijo.johnson@yahoo.ca")
# pwd_entry = Text(window, height=2, width=21)
# pwd_entry.grid(column=1, row = 3)
web_entry = Entry(width=35)
web_entry.grid(column=1, row = 1, columnspan = 2)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row = 2, columnspan = 2)
email_entry.insert(0, "shijo.johnson@yahoo.ca")
pwd_entry = Entry(width=21)
pwd_entry.grid(column=1, row = 3)


#Button
generate_pwd_button = Button(text="Generate Password", command=generate_password)
generate_pwd_button.grid(column=2, row = 3)
Add_button = Button(text="Add", width = 36, command = save)
Add_button.grid(column=1, row = 4, columnspan= 2)

window.mainloop()
