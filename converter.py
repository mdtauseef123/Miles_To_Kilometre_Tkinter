from tkinter import *
window = Tk()
window.title("Mile To Km Converter")
#window.minsize(width=300, height=300)
window.config(padx=20, pady=20)


def convert_miles():
    miles = int(user_input.get())
    kilo_metres = miles * 1.609
    result.config(text=kilo_metres)


user_input = Entry(width=10)
user_input.grid(row=0, column=1)
label1 = Label(text="Miles")
label1.grid(row=0, column=2)
label2 = Label(text="is equal to")
label2.grid(row=1, column=0)
result = Label(text="0")
result.grid(row=1, column=1)
km = Label(text="Km")
km.grid(row=1, column=2)
calculate = Button(text="Calculate", command=convert_miles)
calculate.grid(row=2, column=1)
window.mainloop()
