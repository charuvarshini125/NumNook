import tkinter as tk

# ---------------- Window ----------------
root = tk.Tk()
root.title("NumNook")
root.geometry("420x520")   # wider window to fit grid cleanly
root.configure(bg="#EAF3FF")
root.resizable(False, False)

expression = ""

# ---------------- Functions ----------------
def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Try again")
        expression = ""

# ---------------- Display ----------------
equation = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 22),
    bg="#FFFFFF",
    fg="#2C4A7A",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=25, pady=(25, 15), ipady=18)

# ---------------- Button Frame ----------------
button_frame = tk.Frame(root, bg="#EAF3FF")
button_frame.pack()

# Force equal column width (THIS IS KEY)
for i in range(4):
    button_frame.columnconfigure(i, weight=1, minsize=85)

# ---------------- Buttons ----------------
buttons = [
    ('7',0,0), ('8',0,1), ('9',0,2), ('+',0,3),
    ('4',1,0), ('5',1,1), ('6',1,2), ('-',1,3),
    ('1',2,0), ('2',2,1), ('3',2,2), ('×',2,3),
    ('C',3,0), ('0',3,1), ('=',3,2), ('÷',3,3)
]

def get_command(symbol):
    if symbol == '=':
        return calculate
    elif symbol == 'C':
        return clear
    elif symbol == '×':
        return lambda: press('*')
    elif symbol == '÷':
        return lambda: press('/')
    else:
        return lambda: press(symbol)

for (text, row, col) in buttons:
    btn = tk.Button(
        button_frame,
        text=text,
        command=get_command(text),
        font=("Arial", 14, "bold"),
        bg="#C6DEFF" if text == "=" else "#E4F0FF" if text == "C" else "#D6E8FF",
        fg="#2C4A7A",
        activebackground="#AFCBFF",
        activeforeground="#2C4A7A",
        width=6,        # REDUCED width
        height=2,
        bd=0,
        relief="flat",
        cursor="hand2"
    )
    btn.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

# ---------------- Footer ----------------
footer = tk.Label(
    root,
    text="NumNook — cozy math corner",
    bg="#EAF3FF",
    fg="#6A8CCF",
    font=("Arial", 10)
)
footer.pack(pady=15)

root.mainloop()
