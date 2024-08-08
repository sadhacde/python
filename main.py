from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=40, height=30)
window.config(padx=30, pady=20)

def miles_to_km():
    km = round(float(miles_input.get()) * 1.609)
    label.config(text=f"{km}")

# label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

label = Label(text="0")
label.grid(column=1, row=1)
# OR my_label.config(text="New Text")

# button
calc = Button(text="Calculate", command=miles_to_km)
calc.grid(column=1, row=2)

# entry
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.get()
miles_input.grid(column=1, row=0)


window.mainloop()
