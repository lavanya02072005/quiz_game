import tkinter as tk
from tkinter import messagebox
import random

# ─── Questions ───────────────────────────────────────────────────────────────

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Chennai", "Kolkata"],
        "answer": "New Delhi"
    },
    {
        "question": "How many planets are in our Solar System?",
        "options": ["7", "8", "9", "10"],
        "answer": "8"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein"],
        "answer": "Alexander Graham Bell"
    },
    {
        "question": "What is the largest continent?",
        "options": ["Africa", "Europe", "Asia", "Australia"],
        "answer": "Asia"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Japan", "Korea", "Thailand"],
        "answer": "Japan"
    },
    {
        "question": "What is the fastest land animal?",
        "options": ["Lion", "Horse", "Cheetah", "Leopard"],
        "answer": "Cheetah"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Amazon", "Nile", "Ganges", "Yangtze"],
        "answer": "Nile"
    }
]

# ─── Colors ──────────────────────────────────────────────────────────────────

BG_COLOR      = "#1a1a2e"
CARD_COLOR    = "#16213e"
ACCENT        = "#e94560"
CORRECT_COLOR = "#4ecca3"
WRONG_COLOR   = "#e94560"
TEXT_COLOR    = "#eaeaea"
BTN_COLORS    = ["#0f3460", "#533483", "#05c46b", "#0fbcf9"]

# ─── App ─────────────────────────────────────────────────────────────────────

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 General Knowledge Quiz")
        self.root.geometry("700x550")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.questions = random.sample(questions, 10)
        self.current    = 0
        self.score      = 0
        self.answered   = False

        self.build_ui()
        self.load_question()

    def build_ui(self):
        # ── Header ──
        header = tk.Frame(self.root, bg=ACCENT, pady=10)
        header.pack(fill="x")

        tk.Label(header, text="🎮 General Knowledge Quiz",
                 font=("Arial", 20, "bold"),
                 bg=ACCENT, fg="white").pack()

        # ── Score & Progress ──
        info_frame = tk.Frame(self.root, bg=BG_COLOR, pady=8)
        info_frame.pack(fill="x", padx=20)

        self.progress_label = tk.Label(info_frame,
                                       text="Question 1 / 10",
                                       font=("Arial", 12),
                                       bg=BG_COLOR, fg="#aaaaaa")
        self.progress_label.pack(side="left")

        self.score_label = tk.Label(info_frame,
                                    text="Score: 0",
                                    font=("Arial", 12, "bold"),
                                    bg=BG_COLOR, fg=CORRECT_COLOR)
        self.score_label.pack(side="right")

        # ── Progress Bar ──
        self.bar_frame = tk.Frame(self.root, bg="#333", height=8)
        self.bar_frame.pack(fill="x", padx=20, pady=2)
        self.bar = tk.Frame(self.bar_frame, bg=ACCENT, height=8, width=0)
        self.bar.pack(side="left")

        # ── Question Card ──
        card = tk.Frame(self.root, bg=CARD_COLOR,
                        padx=20, pady=20,
                        relief="flat", bd=0)
        card.pack(fill="x", padx=20, pady=10)

        self.question_label = tk.Label(card,
                                       text="",
                                       font=("Arial", 15, "bold"),
                                       bg=CARD_COLOR, fg=TEXT_COLOR,
                                       wraplength=620,
                                       justify="center")
        self.question_label.pack()

        # ── Option Buttons ──
        self.btn_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.btn_frame.pack(pady=10)

        self.buttons = []
        for i in range(4):
            row = i // 2
            col = i % 2
            btn = tk.Button(self.btn_frame,
                            text="",
                            font=("Arial", 12, "bold"),
                            bg=BTN_COLORS[i],
                            fg="white",
                            width=28, height=2,
                            relief="flat",
                            cursor="hand2",
                            command=lambda i=i: self.check_answer(i))
            btn.grid(row=row, column=col, padx=8, pady=8)
            self.buttons.append(btn)

        # ── Result Label ──
        self.result_label = tk.Label(self.root,
                                     text="",
                                     font=("Arial", 13, "bold"),
                                     bg=BG_COLOR, fg=CORRECT_COLOR)
        self.result_label.pack(pady=4)

        # ── Next Button ──
        self.next_btn = tk.Button(self.root,
                                  text="Next ➡",
                                  font=("Arial", 12, "bold"),
                                  bg=ACCENT, fg="white",
                                  width=15, height=1,
                                  relief="flat",
                                  cursor="hand2",
                                  command=self.next_question,
                                  state="disabled")
        self.next_btn.pack(pady=6)

    def load_question(self):
        self.answered = False
        self.result_label.config(text="")
        self.next_btn.config(state="disabled")

        q = self.questions[self.current]
        self.question_label.config(text=f"Q{self.current + 1}. {q['question']}")
        self.progress_label.config(text=f"Question {self.current + 1} / 10")

        # Update progress bar
        width = int((self.current / 10) * 660)
        self.bar.config(width=width)

        opts = q["options"]
        for i, btn in enumerate(self.buttons):
            btn.config(text=opts[i],
                       bg=BTN_COLORS[i],
                       state="normal")

    def check_answer(self, idx):
        if self.answered:
            return
        self.answered = True

        q = self.questions[self.current]
        selected = self.buttons[idx].cget("text")

        for btn in self.buttons:
            btn.config(state="disabled")

        if selected == q["answer"]:
            self.score += 1
            self.buttons[idx].config(bg=CORRECT_COLOR)
            self.result_label.config(text="✅ Correct!", fg=CORRECT_COLOR)
        else:
            self.buttons[idx].config(bg=WRONG_COLOR)
            self.result_label.config(
                text=f"❌ Wrong! Answer: {q['answer']}", fg=WRONG_COLOR)
            # Highlight correct answer
            for btn in self.buttons:
                if btn.cget("text") == q["answer"]:
                    btn.config(bg=CORRECT_COLOR)

        self.score_label.config(text=f"Score: {self.score}")
        self.next_btn.config(state="normal")

    def next_question(self):
        self.current += 1
        if self.current < 10:
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Result Screen
        tk.Frame(self.root, bg=ACCENT, pady=10).pack(fill="x")

        tk.Label(self.root, text="🏆 Quiz Completed!",
                 font=("Arial", 22, "bold"),
                 bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=30)

        percentage = (self.score / 10) * 100

        if percentage == 100:
            emoji, msg = "🥇", "Perfect Score!"
        elif percentage >= 70:
            emoji, msg = "🥈", "Great Job!"
        elif percentage >= 40:
            emoji, msg = "🥉", "Good Effort!"
        else:
            emoji, msg = "📚", "Keep Practicing!"

        tk.Label(self.root, text=emoji,
                 font=("Arial", 50),
                 bg=BG_COLOR).pack()

        tk.Label(self.root,
                 text=f"{self.score} / 10",
                 font=("Arial", 40, "bold"),
                 bg=BG_COLOR, fg=CORRECT_COLOR).pack()

        tk.Label(self.root, text=msg,
                 font=("Arial", 16),
                 bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)

        tk.Label(self.root,
                 text=f"Percentage: {percentage:.0f}%",
                 font=("Arial", 13),
                 bg=BG_COLOR, fg="#aaaaaa").pack()

        # Play Again Button
        tk.Button(self.root,
                  text="🔄 Play Again",
                  font=("Arial", 13, "bold"),
                  bg=ACCENT, fg="white",
                  width=15, height=2,
                  relief="flat",
                  cursor="hand2",
                  command=self.restart).pack(pady=30)

    def restart(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.questions = random.sample(questions, 10)
        self.current   = 0
        self.score     = 0
        self.answered  = False
        self.build_ui()
        self.load_question()

# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()