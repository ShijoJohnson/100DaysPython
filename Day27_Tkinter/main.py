import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width = 500, height = 300)

my_label = tkinter.Label(text="my Label", font = ("Arial", 24, "bold"))
#my_label.pack(side = "left")
my_label.pack()

#updating properties of an object
my_label["text"] = "New Text"
#or use this for above my_label.config(text = "new Text")

#Entry
input = tkinter.Entry(width =  10)
input.pack()
print(input.get())


#button
def button_clicked():
    # my_label.config(text = "I was clicked")
    my_label.config(text=input.get())
    print("I was clicked!")

button = tkinter.Button(text = "Click me", command = button_clicked)
button.pack()









window.mainloop()