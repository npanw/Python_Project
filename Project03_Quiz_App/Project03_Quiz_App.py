import tkinter as tk
from tkinter import messagebox

questions = ["What is the capital of France?", "Which language is used for web development?", "What is 2 + 2?", "What is the color of the sky?"]
options = [["London", "Paris", "Berlin", "Madrid"], ["Python", "JavaScript", "C++", "Java"], ["3", "2", "4", "5"], ["Green", "Red", "Blue", "Yellow"]]
answers = ["Paris", "JavaScript", "4", "Blue"]

current_question = 0
score = 0

def next_question():
    global current_question, score
    if var.get() == answers[current_question]:
        score += 1
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", "Incorrect!")
    current_question += 1
    if current_question < len(questions):
        update_question()
    else:
        messagebox.showinfo("Quiz Completed", f"Your score is: {score}")
        root.quit()

def update_question():
    question_label.config(text=questions[current_question])
    for i, option in enumerate(options[current_question]):
        radio_buttons[i].config(text=option, value=option)
    var.set(None)

root = tk.Tk()
root.title("Quiz Application")

var = tk.StringVar()
question_label = tk.Label(root, text=questions[current_question], font=('Arial', 16))
question_label.pack(pady=20)

radio_buttons = [tk.Radiobutton(root, variable=var, font=('Arial', 14)) for _ in range(4)]
for rb in radio_buttons:
    rb.pack(anchor='w')

update_question()
tk.Button(root, text="Submit", command=next_question, font=('Arial', 14)).pack(pady=20)
root.mainloop()