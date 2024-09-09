import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        current_text = entry_var.get()
        entry_var.set(current_text + text)

def start():
    start_button.grid_forget()
    clear_button.grid(row=1, column=0, columnspan=4)
    entry.grid(row=2, column=0, columnspan=4)
    for i, text in enumerate(button_text):
        button = tk.Button(root, text=text, font='Arial 18 bold', padx=20, pady=20, width=3)
        button.grid(row=(i//4)+3, column=i%4)
        button.bind("<Button-1>", click)

def exit_app(event):
    root.destroy()

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font='Arial 20 bold', bd=10, insertwidth=4, width=14, borderwidth=4, relief="ridge")

start_button = tk.Button(root, text="Start", font='Arial 18 bold', padx=20, pady=20)
start_button.grid(row=0, column=0, columnspan=4)
start_button.bind("<Button-1>", lambda e: start())

clear_button = tk.Button(root, text="Clear", font='Arial 18 bold', padx=20, pady=20)
clear_button.grid(row=1, column=0, columnspan=4)
clear_button.bind("<Button-1>", lambda e: entry_var.set(""))

exit_button = tk.Button(root, text="Exit", font='Arial 18 bold', padx=20, pady=20)
exit_button.grid(row=1, column=4, columnspan=4)
exit_button.bind("<Button-1>", exit_app)

button_text = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

root.mainloop()
