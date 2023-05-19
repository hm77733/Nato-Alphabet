import tkinter



window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=150, pady=100)

is_equql_to_lable = tkinter.Label(text="is equal to", font=('Arial', 12, 'italic'))
is_equql_to_lable.grid(column=0, row=2)

km = tkinter.Label(text="KM", font=('Arial', 12, 'italic'))
km.grid(column=2, row=2)

result = tkinter.Label(text='0', font=('Arial', 12, 'italic'))
result.grid(column=1, row=2)

mile = tkinter.Label(text='Miles', font=('Arial', 12, 'italic'))
mile.grid(column=2, row=0)


def button_clicked():
    result['text'] = str(round(float(user_input.get())*1.609))


button = tkinter.Button(text="Submit", command=button_clicked)
button.grid(column=1, row=3)


# new_button = tkinter.Button(text="new_button", command=button_clicked)
# new_button.grid(column=2, row=0)

user_input = tkinter.Entry(width=10, )
user_input.grid(row=0, column=1)
user_entry = user_input.get()





window.mainloop()