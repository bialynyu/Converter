from tkinter import *
FONT = ("Arial", 13)
WIDTH = 250
HEIGHT = 150


window = Tk()
window.title("GUI")
window.minsize(width=WIDTH, height=HEIGHT)



#Radiobuttons

radio_state = IntVar()

miles = Radiobutton(text="Miles", value=0, variable=radio_state)
miles.grid(column=2, row=0)

kilometers = Radiobutton(text="Kilometers", value=1, variable=radio_state)
kilometers.grid(column=2, row=1)


#Labels
result = Label(text="0", font=FONT)
result.grid(column=1, row=1)


equal = Label(text="is equal to", font=FONT)
equal.grid(column=0,row=1)

# Entry

my_entry = Entry(width=15)
my_entry.grid(column=1,row=0)


def calculate():
    if radio_state.get() == 0:
        mil = int(my_entry.get())
        km = float(mil * 1.6)
        result.config(text=f"{str(km)} km")
    else:
        km = int(my_entry.get())
        mil = float(km * 0.62)
        result.config(text=f"{str(mil)} miles")

#Button
button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)



window.mainloop()
