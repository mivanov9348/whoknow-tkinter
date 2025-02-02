import tkinter as tk
from tkinter import messagebox

questions = [
    {"question": "What is the capital of Bulgaria?", "answers": ["Sofia", "Plovdiv", "Varna", "Burgas"], "correct": "Sofia", "level": 1},
    {"question": "Which is the highest peak in Bulgaria?", "answers": ["Vihren", "Musala", "Rila", "Pirin"], "correct": "Musala", "level": 2},
    {"question": "Who is the author of the poem 'Gramada'?", "answers": ["Hristo Botev", "Ivan Vazov", "Peyo Yavorov", "Pencho Slaveykov"], "correct": "Peyo Yavorov", "level": 3},
    {"question": "What is the chemical symbol for water?", "answers": ["H2O", "CO2", "O2", "NaCl"], "correct": "H2O", "level": 1},
    {"question": "Who wrote 'Romeo and Juliet'?", "answers": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"], "correct": "William Shakespeare", "level": 2},
    {"question": "What is the largest planet in the Solar System?", "answers": ["Earth", "Jupiter", "Saturn", "Mars"], "correct": "Jupiter", "level": 3},
    {"question": "What is the square root of 64?", "answers": ["4", "6", "8", "10"], "correct": "8", "level": 4},
    {"question": "Who painted the Mona Lisa?", "answers": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "correct": "Leonardo da Vinci", "level": 5},
    {"question": "What is the smallest prime number?", "answers": ["1", "2", "3", "5"], "correct": "2", "level": 6},
    {"question": "What is the capital of Japan?", "answers": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "correct": "Tokyo", "level": 7},
    {"question": "Who developed the theory of relativity?", "answers": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Niels Bohr"], "correct": "Albert Einstein", "level": 8},
    {"question": "What is the hardest natural material on Earth?", "answers": ["Gold", "Iron", "Diamond", "Quartz"], "correct": "Diamond", "level": 9},
    {"question": "What is the largest ocean on Earth?", "answers": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "correct": "Pacific Ocean", "level": 10},
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра с въпроси")
        self.root.geometry("500x400")

        self.current_level = 0
        self.score = 0

        self.start_screen()

    def start_screen(self):
        # Начален екран
        self.clear_screen()
        label = tk.Label(self.root, text="Добре дошли в играта с въпроси!", font=("Arial", 16))
        label.pack(pady=20)

        start_button = tk.Button(self.root, text="Старт", command=self.load_question)
        start_button.pack(pady=10)

    def load_question(self):
        # Зареждане на въпроса
        self.clear_screen()

        if self.current_level >= len(questions):
            self.end_game()
            return

        question_data = questions[self.current_level]
        question_label = tk.Label(self.root, text=question_data["question"], font=("Arial", 14), wraplength=400)
        question_label.pack(pady=20)

        for answer in question_data["answers"]:
            button = tk.Button(self.root, text=answer, width=20, command=lambda a=answer: self.check_answer(a))
            button.pack(pady=5)

    def check_answer(self, selected_answer):
        # Проверка на отговора
        question_data = questions[self.current_level]
        if selected_answer == question_data["correct"]:
            self.score += 1
            self.current_level += 1
            if self.current_level < len(questions):
                self.load_question()
            else:
                self.end_game()
        else:
            self.end_game()

    def end_game(self):
        # Край на играта
        self.clear_screen()
        result_text = f"Играта приключи! Твоят резултат е {self.score} от {len(questions)}."
        result_label = tk.Label(self.root, text=result_text, font=("Arial", 14))
        result_label.pack(pady=20)

        restart_button = tk.Button(self.root, text="Рестарт", command=self.restart_game)
        restart_button.pack(pady=10)

    def restart_game(self):
        # Рестартиране на играта
        self.current_level = 0
        self.score = 0
        self.start_screen()

    def clear_screen(self):
        # Изчистване на екрана
        for widget in self.root.winfo_children():
            widget.destroy()


# Стартиране на приложението
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
