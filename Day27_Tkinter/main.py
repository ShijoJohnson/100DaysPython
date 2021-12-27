import tkinter

#button
def button_clicked():
    print("I was clicked!")
    # my_label.config(text = "I was clicked")
    my_label.config(text=input.get())


window = tkinter.Tk()
window.title("First GUI")
window.minsize(width = 500, height = 300)
window.config(padx = 50, pady = 50)

my_label = tkinter.Label(text="my Label", font = ("Arial", 24, "bold"))
#my_label.pack(side = "left")
# my_label.pack()
my_label.grid(column=0, row = 0)

button = tkinter.Button(text = "Click me", command = button_clicked)
# button.pack()
button.grid(column = 1, row = 1)

button1 = tkinter.Button(text = "Click me", command = button_clicked)
# button.pack()
button1.grid(column = 2, row = 0)

#updating properties of an object
#my_label["text"] = "New Text"
#or use this for above my_label.config(text = "new Text")

#Entry
# input = tkinter.Entry(width =  10)
# # input.pack()
# input.grid(column = 3, row = 2)
# print(input.get())

input1 = tkinter.Entry(width =  10)
# input.pack()
input1.place(x=0, y=0)
print(input1.get())

# input2 = tkinter.Entry(width =  10)
# # input.pack()
# input2.grid(column=0, row=10)
#grid and pack cannot be used in same
# print(input2.get())

#pack, place and grid decide where the object shows up in the screen



window.mainloop()
