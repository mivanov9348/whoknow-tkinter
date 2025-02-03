import json
import tkinter as tk
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра с въпроси")
        self.root.geometry("500x400")

        self.current_level = 0
        self.score = 0

        with open('questions.json', 'r', encoding='utf-8') as file:
            self.questions_by_level = json.load(file)

        self.start_screen()

    def start_screen(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Добре дошли в играта с въпроси!", font=("Arial", 16))
        label.pack(pady=20)

        start_button = tk.Button(self.root, text="Старт", command=self.load_question)
        start_button.pack(pady=10)

    def load_question(self):
        self.clear_screen()

        level_key = f"level_{self.current_level + 1}"
        if level_key not in self.questions_by_level:
            self.end_game()
            return

        level_questions = self.questions_by_level[level_key]
        if not level_questions:
            self.end_game()
            return

        question_data = random.choice(level_questions)
        question_label = tk.Label(self.root, text=question_data["question"], font=("Arial", 14), wraplength=400)
        question_label.pack(pady=20)

        for answer in question_data["answers"]:
            button = tk.Button(self.root, text=answer, width=20,
                               command=lambda a=answer: self.check_answer(a, level_key, question_data))
            button.pack(pady=5)

    def check_answer(self, selected_answer, level_key, question_data):
        level_questions = self.questions_by_level[level_key]

        if selected_answer == question_data["correct"]:
            self.score += 1
            level_questions.remove(question_data)
            if not level_questions:
                self.current_level += 1
            self.load_question()
        else:
            self.end_game()

    def end_game(self):
        self.clear_screen()
        result_text = f"Играта приключи! Твоят резултат е {self.score} от {self.get_total_questions()}."
        result_label = tk.Label(self.root, text=result_text, font=("Arial", 14))
        result_label.pack(pady=20)

        restart_button = tk.Button(self.root, text="Рестарт", command=self.restart_game)
        restart_button.pack(pady=10)

    def get_total_questions(self):
        total = 0
        for level in self.questions_by_level.values():
            total += len(level)
        return total

    def restart_game(self):
        self.current_level = 0
        self.score = 0
        with open('questions.json', 'r', encoding='utf-8') as file:
            self.questions_by_level = json.load(file)
        self.start_screen()

    def clear_screen(self):
        # Изчистване на екрана
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
