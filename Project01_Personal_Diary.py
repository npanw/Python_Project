import tkinter as tk
from tkinter import filedialog, messagebox

def save_entry():
    with open(filedialog.asksaveasfilename(defaultextension=".txt"), "w") as file:
        file.write(text_area.get("1.0", tk.END))
    messagebox.showinfo("Success", "Entry saved")

def load_entry():
    with open(filedialog.askopenfilename(defaultextension=".txt"), "r") as file:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, file.read())
    messagebox.showinfo("Success", "Entry loaded")

root = tk.Tk()
root.title("Personal Diary")

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_entry)
file_menu.add_command(label="Load", command=load_entry)

root.mainloop()
