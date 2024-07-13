import tkinter as tk
from functools import partial

def print_number(number):
    codsoft_textbox.configure(state=tk.NORMAL)
    codsoft_textbox.insert(tk.END, str(number))
    codsoft_textbox.configure(state=tk.DISABLED)

def evaluate():
    expression = codsoft_textbox.get()
    result = eval(expression)
    codsoft_textbox.configure(state=tk.NORMAL)
    codsoft_textbox.delete(0, len(expression))
    codsoft_textbox.insert(tk.END, result)
    codsoft_textbox.configure(state=tk.DISABLED)

def clear(event):
    codsoft_textbox.configure(state=tk.NORMAL)
    codsoft_textbox.delete(0, len(codsoft_textbox.get()))
    codsoft_textbox.configure(state=tk.DISABLED)

codsoft_root = tk.Tk()
codsoft_root.title("Calculator using python")
  
#Width x Height
codsoft_root.geometry("500x500")

#Width x Height
codsoft_root.minsize(300,300)

#Width x Height
codsoft_root.maxsize(1200,900)

codsoft_root.bind("<Key-BackSpace>", clear)

codsoft_root.grid_rowconfigure(0, weight=1)
codsoft_root.grid_rowconfigure(1, weight=4)
codsoft_root.grid_columnconfigure(0, weight=1)

codsoft_frame = tk.Frame(codsoft_root, width=500, height=50, background= 'yellow')
codsoft_frame.grid(row=0, column=0, sticky=tk.NSEW)

codsoft_button_frame = tk.Frame(codsoft_root, width=500, height=100, background= 'black')
codsoft_button_frame.grid(row=1, column=0, sticky=tk.NSEW)

for i in range(4):
    codsoft_button_frame.grid_rowconfigure(i, weight=1)
    codsoft_button_frame.grid_columnconfigure(i, weight=1)

codsoft_textbox = tk.Entry(codsoft_frame, font=("Arial", 30), state=tk.DISABLED, disabledbackground='lightgrey', bg='lightgrey', fg='yellow')
codsoft_textbox.pack(fill=tk.BOTH, expand=True)

button_one=tk.Button(codsoft_button_frame, text="1", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_one.configure(command=partial(print_number, 1))
button_one.grid(row=0, column=0, sticky=tk.NSEW)

button_two=tk.Button(codsoft_button_frame, text="2", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_two.configure(command=partial(print_number, 2))
button_two.grid(row=0, column=1, sticky=tk.NSEW)

button_three=tk.Button(codsoft_button_frame, text="3", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_three.configure(command=partial(print_number, 3))
button_three.grid(row=0, column=2, sticky=tk.NSEW)

button_four=tk.Button(codsoft_button_frame, text="4", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_four.configure(command=partial(print_number, 4))
button_four.grid(row=1, column=0, sticky=tk.NSEW)

button_five=tk.Button(codsoft_button_frame, text="5", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_five.configure(command=partial(print_number, 5))
button_five.grid(row=1, column=1, sticky=tk.NSEW)

button_six=tk.Button(codsoft_button_frame, text="6", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_six.configure(command=partial(print_number, 6))
button_six.grid(row=1, column=2, sticky=tk.NSEW)

button_seven=tk.Button(codsoft_button_frame, text="7", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_seven.configure(command=partial(print_number, 7))
button_seven.grid(row=2, column=0, sticky=tk.NSEW)

button_eight=tk.Button(codsoft_button_frame, text="8", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_eight.configure(command=partial(print_number, 8))
button_eight.grid(row=2, column=1, sticky=tk.NSEW)

button_nine=tk.Button(codsoft_button_frame, text="9", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_nine.configure(command=partial(print_number, 9))
button_nine.grid(row=2, column=2, sticky=tk.NSEW)

button_zero=tk.Button(codsoft_button_frame, text="0", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_zero.configure(command=partial(print_number, 0))
button_zero.grid(row=3, column=1, sticky=tk.NSEW)

button_plus=tk.Button(codsoft_button_frame, text="+", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_plus.configure(command=partial(print_number, "+"))
button_plus.grid(row=0, column=3, sticky=tk.NSEW)

button_minus=tk.Button(codsoft_button_frame, text="-", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_minus.configure(command=partial(print_number, "-"))
button_minus.grid(row=1, column=3, sticky=tk.NSEW)

button_multiply=tk.Button(codsoft_button_frame, text="x", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_multiply.configure(command=partial(print_number, "*"))
button_multiply.grid(row=2, column=3, sticky=tk.NSEW)

button_divide=tk.Button(codsoft_button_frame, text="/", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_divide.configure(command=partial(print_number, "/"))
button_divide.grid(row=3, column=3, sticky=tk.NSEW)

button_dot=tk.Button(codsoft_button_frame, text=".", font=("arial", 20),  width=6, bg="black", fg="lightgrey")
button_dot.configure(command=partial(print_number, "."))
button_dot.grid(row=3, column=0, sticky=tk.NSEW)

button_equal=tk.Button(codsoft_button_frame, text="=", font=("arial", 20),  width=6, bg="orange", fg="black")
button_equal.configure(command=evaluate)
button_equal.grid(row=3, column=2, sticky=tk.NSEW)


# codsoft = tk.Label(text="Codsoft")
# codsoft.pack()

 
#GUI logic here
codsoft_root.mainloop()

 