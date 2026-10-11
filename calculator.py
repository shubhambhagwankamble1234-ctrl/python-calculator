import tkinter as tk

#Existing calculator logic
def calculate(a,operator,b) :
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        if b==0 :
            return "Error : Cannot divide by zero"
        return a/b
    else:
        return "Invalid Error."

#Create the main Window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("340x470")
root.resizable(False,False)
root.configure(bg="Dark grey")

#Calculator state
display = tk.StringVar(value="0")
first_number = None
current_operator = None
new_input = True

def press_number(number):
    global new_input

    current = display.get()

    if new_input:
        display.set("." if number == "." else number)
        new_input = False
    elif number == "." and "." in current:
        return
    elif current == "0" and number != ".":
        display.set(number)
    else:
        display.set(current + number)


def press_operator(operator):
    global first_number, current_operator, new_input

    try:
        first_number = float(display.get())
        current_operator = operator
        new_input = True
    except ValueError:
        display.set("Error")


def press_equal():
    global first_number, current_operator, new_input

    if first_number is None or current_operator is None:
        return

    try:
        second_number = float(display.get())

        result = calculate(
            first_number,
            current_operator,
            second_number
        )

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display.set(str(result))

        first_number = None
        current_operator = None
        new_input = True

    except (ValueError, ZeroDivisionError, OverflowError) as error:
        display.set("Error")
        first_number = None
        current_operator = None
        new_input = True


def clear_display():
    global first_number, current_operator, new_input

    display.set("0")
    first_number = None
    current_operator = None
    new_input = True


def backspace():
    global new_input

    if new_input:
        return

    current = display.get()

    if len(current) <= 1 or (
        len(current) == 2 and current.startswith("-")
    ):
        display.set("0")
    else:
        display.set(current[:-1])


# Display screen
screen = tk.Entry(
    root,
    textvariable=display,
    font=("Arial", 26),
    justify="right",
    state="readonly",
    readonlybackground="#303134",
    fg="white",
    bd=0
)
screen.pack(fill="x", padx=12, pady=18, ipady=15)

# Button layout
buttons = [
    [("C", "clear"), ("⌫", "back"), ("/", "/"), ("*", "*")],
    [("7", "7"), ("8", "8"), ("9", "9"), ("-", "-")],
    [("4", "4"), ("5", "5"), ("6", "6"), ("+", "+")],
    [("1", "1"), ("2", "2"), ("3", "3"), ("=", "=")],
    [("0", "0"), (".", ".")]
]

for row_index, row in enumerate(buttons):
    frame = tk.Frame(root, bg="#202124")
    frame.pack(fill="both", expand=True, padx=8)

    for label, value in row:
        if value == "clear":
            command = clear_display
        elif value == "back":
            command = backspace
        elif value in ("+", "-", "*", "/"):
            command = lambda op=value: press_operator(op)
        elif value == "=":
            command = press_equal
        else:
            command = lambda n=value: press_number(n)

        button = tk.Button(
            frame,
            text=label,
            command=command,
            font=("Arial", 16, "bold"),
            bg="#3c4043" if value not in ("=", "+", "-", "*", "/")
            else "#4285f4",
            fg="white",
            activebackground="#5f6368",
            activeforeground="white",
            bd=0
        )

        button.pack(
            side="left",
            fill="both",
            expand=True,
            padx=3,
            pady=3
        )

root.mainloop()
