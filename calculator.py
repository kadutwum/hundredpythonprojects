from tkinter import *


window = Tk() 
window.title("Simple Calculator")

display = Entry(window, width=30, borderwidth = 5)
display.grid(row=0, column=0,  columnspan=5, padx=1, pady=1)



button1 = Button(window, text="1", padx =20, pady=10)
button2 = Button(window, text="2", padx =20, pady=10)
button3 = Button(window, text="3", padx =20, pady=10)
button4 = Button(window, text="4", padx =20, pady=10)
button5 = Button(window, text="5", padx =20, pady=10)
button6 = Button(window, text="6", padx =20, pady=10)
button7 = Button(window, text="7", padx =20, pady=10)
button8 = Button(window, text="8", padx =20, pady=10)
button9= Button(window, text="9", padx =20, pady=10)
button0 = Button(window, text="0", padx =20, pady=10)
button_dot = Button(window, text=" .", padx=20, pady=10)
button_equal = Button(window, text="=", padx=20, pady=10)

button_division = Button(window, text="/", padx =20, pady=10)
button_multiplication = Button(window, text="*", padx =20, pady=10)
button_substraction = Button(window, text="-", padx =20, pady=10)
button_add= Button(window, text="+", padx=18, pady=10)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_division.grid(row=1, column=4)
button_multiplication.grid(row=2, column=4)
button_substraction.grid(row=3, column=4)
button_add.grid(row=4, column=4)

window.mainloop() 

