import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            screen_var.set(str(eval(screen_var.get())))
        except Exception:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.title("Calculator")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill="both", ipadx=8, pady=10)

buttons = ['7', '8', '9', 'C', '4', '5', '6', '/', '1', '2', '3', '*', '0', '-', '=', '+']
button_frame = tk.Frame(root)
button_frame.pack()

for i, btn_text in enumerate(buttons):
    btn = tk.Button(button_frame, text=btn_text, font="lucida 15 bold", padx=10, pady=10)
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    btn.bind("<Button-1>", button_click)

root.mainloop()
