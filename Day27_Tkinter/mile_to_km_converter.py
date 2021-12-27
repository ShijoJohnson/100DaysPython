import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width = 300, height = 200)
window.config(padx = 20, pady = 20)

def button_clicked():
    result = tkinter.Label(font=("Arial", 12, "bold"))
    new_text = int(input.get()) * 1.6
    result.config(text = new_text)
    result.grid(column=1, row=1)


my_label = tkinter.Label(text="is equal to", font = ("Arial", 12, "bold"))
my_label.grid(column=0, row = 1)
input = tkinter.Entry(width =  10)
input.grid(column = 1, row = 0)
my_label = tkinter.Label(text="Miles", font = ("Arial", 12, "bold"))
my_label.grid(column=2, row = 0)
my_label = tkinter.Label(text="Km", font = ("Arial", 12, "bold"))
my_label.grid(column=2, row = 1)
button = tkinter.Button(text = "Calculate", command = button_clicked)
button.grid(column = 1, row = 2)



window.mainloop()
