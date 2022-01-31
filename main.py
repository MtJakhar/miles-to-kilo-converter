from tkinter import *

window = Tk()
window.title("Mile to km Converter")

window.config(padx=30, pady=30)

milesEntry = Entry(width=15)
milesEntry.grid(column=1, row=0)

milesText = Label(text="Miles")
milesText.grid(column=2, row=0)

equalText = Label(text="is equal to")
equalText.grid(column=0, row=1)

convertText = Label(text="0")
convertText.grid(column=1, row=1)

kmText = Label(text="Km")
kmText.grid(column=2, row=1)


def button_clicked():
    miles = float(milesEntry.get())
    km = str(round(miles * 1.609344, 2))
    convertText.config(text=km)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)




window.mainloop()