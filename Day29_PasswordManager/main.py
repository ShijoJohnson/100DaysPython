from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
T = Text(window, height=2, width=35)
T.grid(column=1, row = 1, columnspan = 2)
T1 = Text(window, height=2, width=35)
T1.grid(column=1, row = 2, columnspan = 2)
T1 = Text(window, height=2, width=21)
T1.grid(column=1, row = 3)

#Button
generate_pwd_button = Button(text="Generate Password")
generate_pwd_button.grid(column=2, row = 3)
Add_button = Button(text="Add", width = 36)
Add_button.grid(column=1, row = 4, columnspan= 2)

window.mainloop()
