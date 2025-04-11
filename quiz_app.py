import tkinter as tk
from tkinter import messagebox

# Quiz data
quiz = {
    "What is the capital of France?": (["London", "Paris", "Berlin", "Rome"], 1),
    "Which language is this app written in?": (["Python", "Java", "C++", "Ruby"], 0),
    "2 + 2 equals?": (["3", "4", "5", "6"], 1),
    "What color is the sky?": (["Green", "Blue", "Red", "Yellow"], 1),
    "Which animal barks?": (["Cat", "Bird", "Dog", "Fish"], 2)
}

questions = list(quiz.keys())

class QuizApp:
    def __init__(self, master):
        self.master = master
        master.title("Quiz App")
        master.geometry("400x350")
        self.score = 0
        self.current_q = 0

        self.question_label = tk.Label(master, text="", font=("Arial", 14), wraplength=380)
        self.question_label.pack(pady=20)

        self.answer = tk.IntVar()
        self.buttons = []
        for i in range(4):
            b = tk.Radiobutton(master, text="", variable=self.answer, value=i, font=("Arial", 12))
            b.pack(anchor='w', padx=20)
            self.buttons.append(b)

        self.submit_btn = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_btn.pack(pady=20)

        self.restart_btn = tk.Button(master, text="Restart", command=self.restart_quiz)
        self.restart_btn.pack(pady=10)
        self.restart_btn.pack_forget()  # Hide restart button initially

        self.load_question()

    def load_question(self):
        question = questions[self.current_q]
        self.question_label.config(text=question)
        options = quiz[question][0]
        for i in range(4):
            self.buttons[i].config(text=options[i])
        self.answer.set(-1)

    def check_answer(self):
        selected = self.answer.get()
        if selected == -1:
            messagebox.showwarning("No Selection", "Please choose an answer.")
            return
        correct = quiz[questions[self.current_q]][1]
        if selected == correct:
            self.score += 1
        self.current_q += 1
        if self.current_q < len(questions):
            self.load_question()
        else:
            self.show_results()

    def show_results(self):
        for btn in self.buttons:
            btn.pack_forget()
        self.submit_btn.pack_forget()
        self.question_label.config(text=f"Quiz Finished!\nYour Score: {self.score}/{len(questions)}")
        self.restart_btn.pack()

    def restart_quiz(self):
        self.score = 0
        self.current_q = 0
        for btn in self.buttons:
            btn.pack(anchor='w', padx=20)
        self.submit_btn.pack(pady=20)
        self.restart_btn.pack_forget()
        self.load_question()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
