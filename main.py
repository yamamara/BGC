from tkinter import *

import matplotlib.pyplot as plot
import numpy as numpy
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Bound:
    XMIN = 0
    XMAX = 1
    YMIN = 2
    YMAX = 3


def add_term(string):
    terms.append(string)
    label.config(text="".join(terms))


def remove_term(event=None):
    if len(terms) > 0:
        terms.pop()

    label.config(text="".join(terms))


def on_key_press(event):
    if event.widget.winfo_class() != "Entry" and event.char.isnumeric() or event.char in operators + ("(", ")", "x"):
        add_term(event.char)


def get_bound(bound):
    value = 0

    if bound == Bound.XMIN:
        value = x_min.get()
    elif bound == Bound.XMAX:
        value = x_max.get()
    elif bound == Bound.YMIN:
        value = y_min.get()
    elif bound == Bound.YMAX:
        value = y_max.get()

    return int(value)


def is_number(n):
    if n.isdigit():
        return True
    else:
        return False


def convert_equation_to_numpy():
    equation = []
    open_parenthesis = 0
    closed_parenthesis = 0

    for i in range(len(terms)):
        if "(" in terms[i]:
            open_parenthesis += 1
        elif ")" in terms[i]:
            closed_parenthesis += 1

        if terms[i] == "^":
            equation.append("**")
        elif terms[i] == "π":
            equation.append("numpy.pi")
        elif terms[i] != "x" and terms[i][0].isalpha():
            equation.append("numpy." + terms[i])
        else:
            equation.append(terms[i])

        if i < len(terms) - 1 and not any(term in terms[i] for term in operators + ("(",)) and terms[i + 1] not in operators + (")",) and not terms[i + 1].isnumeric():
            equation.append("*")

    if open_parenthesis > closed_parenthesis:
        equation.append(")" * (open_parenthesis - closed_parenthesis))

    return "".join(equation)


def graph(event=None):
    figure, axis = plot.subplots()
    axis.axhline(y=0, lw=1, color='k')
    axis.axvline(x=0, lw=1, color='k')
    axis.set(xlim=(get_bound(Bound.XMIN), get_bound(Bound.XMAX)), xticks=numpy.arange(get_bound(Bound.XMIN), get_bound(Bound.XMAX)), ylim=(get_bound(Bound.YMIN), get_bound(Bound.YMAX)), yticks=numpy.arange(get_bound(Bound.YMIN), get_bound(Bound.YMAX)))
    plot.grid()

    if not terms:
        plot.plot(0)
    else:
        x = numpy.linspace(-100, 100, 1000)
        y = eval(convert_equation_to_numpy())

        if "x" in terms:
            plot.plot(x, y)
        else:
            plot.axhline(y=y)

    canvas = FigureCanvasTkAgg(figure, master=root)
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    toolbar.update()
    canvas.get_tk_widget().grid(row=0, sticky="NSEW")


terms = []
operators = ("+", "-", "*", "/", "^", ".")

root = Tk()
root.wm_title("BGC (Basic Graphing Calculator) - Made by Aryan Singh")
root.bind("<Button-1>", lambda event: event.widget.focus_set())
root.bind('<KeyPress>', on_key_press)
root.bind('<BackSpace>', remove_term)
root.bind('<Return>', graph)
root.geometry("600x600")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

label = Label(master=root, text="")
label.grid(row=1)
master_rows = Frame(master=root)
master_rows.grid(row=2, pady=(0, 10))
window_editor = Frame(master=root)
window_editor.grid(row=3)

button_rows = Frame(master=master_rows)
button_rows.grid(row=0, column=0, padx=(0, 10))
operator_rows = Frame(master=master_rows)
operator_rows.grid(row=0, column=1)
function_rows = Frame(master=master_rows)
function_rows.grid(row=0, column=2, padx=(10, 0))

button_row1 = Frame(master=button_rows)
button_row1.grid(row=0, column=0)
button_row2 = Frame(master=button_rows)
button_row2.grid(row=1, column=0)
button_row3 = Frame(master=button_rows)
button_row3.grid(row=2, column=0)
button_row4 = Frame(master=button_rows)
button_row4.grid(row=3, column=0)

operator_row1 = Frame(master=operator_rows)
operator_row1.grid(row=0, column=0)
operator_row2 = Frame(master=operator_rows)
operator_row2.grid(row=1, column=0)
operator_row3 = Frame(master=operator_rows)
operator_row3.grid(row=2, column=0)
operator_row4 = Frame(master=operator_rows)
operator_row4.grid(row=3, column=0)

function_row1 = Frame(master=function_rows)
function_row1.grid(row=0, column=0)
function_row2 = Frame(master=function_rows)
function_row2.grid(row=1, column=0)
function_row3 = Frame(master=function_rows)
function_row3.grid(row=2, column=0)
function_row4 = Frame(master=function_rows)
function_row4.grid(row=3, column=0)

Button(master=button_row1, text="1", width=5, command=lambda: add_term("1")).grid(row=0, column=0)
Button(master=button_row1, text="2", width=5, command=lambda: add_term("2")).grid(row=0, column=1)
Button(master=button_row1, text="3", width=5, command=lambda: add_term("3")).grid(row=0, column=2)
Button(master=button_row2, text="4", width=5, command=lambda: add_term("4")).grid(row=0, column=0)
Button(master=button_row2, text="5", width=5, command=lambda: add_term("5")).grid(row=0, column=1)
Button(master=button_row2, text="6", width=5, command=lambda: add_term("6")).grid(row=0, column=2)
Button(master=button_row3, text="7", width=5, command=lambda: add_term("7")).grid(row=0, column=0)
Button(master=button_row3, text="8", width=5, command=lambda: add_term("8")).grid(row=0, column=1)
Button(master=button_row3, text="9", width=5, command=lambda: add_term("9")).grid(row=0, column=2)
Button(master=button_row4, text="0", width=5, command=lambda: add_term("0")).grid(row=0, column=0)
Button(master=button_row4, text="⌫", width=5, command=lambda: remove_term).grid(row=0, column=1)
Button(master=button_row4, text="Graph", font="System 10 bold", width=5, command=graph).grid(row=0, column=2)

Button(master=operator_row1, text="+", width=5, command=lambda: add_term("+")).grid(row=0, column=0)
Button(master=operator_row1, text="-", width=5, command=lambda: add_term("-")).grid(row=0, column=1)
Button(master=operator_row2, text="*", width=5, command=lambda: add_term("*")).grid(row=0, column=0)
Button(master=operator_row2, text="/", width=5, command=lambda: add_term("/")).grid(row=0, column=1)
Button(master=operator_row3, text="^", width=5, command=lambda: add_term("^")).grid(row=0, column=0)
Button(master=operator_row3, text="(", width=5, command=lambda: add_term("(")).grid(row=0, column=1)
Button(master=operator_row4, text=")", width=5, command=lambda: add_term(")")).grid(row=0, column=0)
Button(master=operator_row4, text=".", width=5, command=lambda: add_term(".")).grid(row=0, column=1)

Button(master=function_row1, text="sin", width=5, command=lambda: add_term("sin(")).grid(row=0, column=0)
Button(master=function_row1, text="cos", width=5, command=lambda: add_term("cos(")).grid(row=0, column=1)
Button(master=function_row1, text="tan", width=5, command=lambda: add_term("tan(")).grid(row=0, column=2)
Button(master=function_row2, text="arcsin", width=5, command=lambda: add_term("arcsin(")).grid(row=0, column=0)
Button(master=function_row2, text="arccos", width=5, command=lambda: add_term("arccos(")).grid(row=0, column=1)
Button(master=function_row2, text="arctan", width=5, command=lambda: add_term("arctan(")).grid(row=0, column=2)
Button(master=function_row3, text="abs", width=5, command=lambda: add_term("abs(")).grid(row=0, column=0)
Button(master=function_row3, text="sqrt", width=5, command=lambda: add_term("sqrt(")).grid(row=0, column=1)
Button(master=function_row3, text="log", width=5, command=lambda: add_term("log(")).grid(row=0, column=2)
Button(master=function_row4, text="π", width=5, command=lambda: add_term("π")).grid(row=0, column=0)
Button(master=function_row4, text="e", width=5, command=lambda: add_term("e")).grid(row=0, column=1)
Button(master=function_row4, text="x", width=5, command=lambda: add_term("x")).grid(row=0, column=2)

vcmd = (root.register(is_number), "%n")
Label(master=window_editor, text="Xmin=").grid(row=0, column=0)
x_min_var = IntVar()
x_min_var.set(-10)
x_min = Entry(master=window_editor, textvariable=x_min_var, width=5, validate="key", vcmd=vcmd)
x_min.grid(row=0, column=1)
Label(master=window_editor, text="Xmax=").grid(row=0, column=2)
x_max_var = IntVar()
x_max_var.set(10)
x_max = Entry(master=window_editor, textvariable=x_max_var, width=5, validate="key", vcmd=vcmd)
x_max.grid(row=0, column=3)
Label(master=window_editor, text="Ymin=").grid(row=0, column=4)
y_min_var = IntVar()
y_min_var.set(-10)
y_min = Entry(master=window_editor, textvariable=y_min_var, width=5, validate="key", vcmd=vcmd)
y_min.grid(row=0, column=5)
Label(master=window_editor, text="Ymax=").grid(row=0, column=6)
y_max_var = IntVar()
y_max_var.set(10)
y_max = Entry(master=window_editor, textvariable=y_max_var, width=5, validate="key", vcmd=vcmd)
y_max.grid(row=0, column=7)
Button(master=window_editor, text="Update", width=5, command=graph).grid(row=0, column=8, padx=(10, 0))

graph()
root.mainloop()
