import tkinter as tk
from tkinter import messagebox
import random

ROCK, PAPER, SCISSORS = 1, 2, 3
choices = {ROCK: "Rock ✊", PAPER: "Paper 🤚", SCISSORS: "Scissors ✌️"}

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.reset_game()

    def reset_game(self):
        
        self.clear_window()

        tk.Label(self.root, text="ROCK✊ PAPER🤚 SCISSORS✌️", font=("Comic Sans MS", 26, "bold")).pack(pady=10)

        tk.Button(self.root, text="Play Against CPU", command=lambda: self.setup_game("cpu"), width=20).pack(pady=5)
        print()
        tk.Button(self.root, text="Play Against a Friend", command=lambda: self.setup_game("friend"), width=20).pack(pady=5)

    def setup_game(self, opponent):
        self.opponent = opponent
        self.clear_window()

        tk.Label(self.root, text="Player 1 lets start with a name: ", font=("Comic Sans MS", 12)).pack(pady=5)
        self.player1_name_entry = tk.Entry(self.root)
        self.player1_name_entry.pack(pady=5)

        if opponent == "friend":
            tk.Label(self.root, text="Now you enter a name Player 2: ", font=("Comic Sans MS", 12)).pack(pady=5)
            self.player2_name_entry = tk.Entry(self.root)
            self.player2_name_entry.pack(pady=5)

        tk.Button(self.root, text="Start Game", command=self.start_game, width=20).pack(pady=10)

    def start_game(self):
        """Start the game after setting player names."""
        player1_name = self.player1_name_entry.get().strip()
        if not self.validate_name(player1_name, "Player 1"):
            return

        self.player1_name = player1_name

        if self.opponent == "friend":
            player2_name = self.player2_name_entry.get().strip()
            if not self.validate_name(player2_name, "Player 2"):
                return
            self.player2_name = player2_name
        else:
            self.player2_name = "CPU"

        self.play_round()

    def validate_name(self, name, player_label):
        
        if not name.isalpha():
            messagebox.showerror(
                "Error", 
                f"Uh-oh {player_label} lets try that name again!."
            )
            return False
        if len(name) < 2:
            messagebox.showerror(
                "Error",
                f"Oops {player_label} lets try that name again!"
            )
            return False
        return True

    def play_round(self):
        self.clear_window()

        tk.Label(self.root, text=f"{self.player1_name}, pick your choice:", font=("Comic Sans MS", 12)).pack(pady=5)
        tk.Button(self.root, text="Rock ✊", command=lambda: self.get_choice(self.player1_name, ROCK), width=15).pack(pady=5)
        tk.Button(self.root, text="Paper 🤚", command=lambda: self.get_choice(self.player1_name, PAPER), width=15).pack(pady=5)
        tk.Button(self.root, text="Scissors ✌️", command=lambda: self.get_choice(self.player1_name, SCISSORS), width=15).pack(pady=5)

    def get_choice(self, player_name, choice):
        if player_name == self.player1_name:
            self.player1_choice = choice

            if self.opponent == "friend":
                self.clear_window()
                tk.Label(self.root, text=f"{self.player2_name}, pick your choice:", font=("Comic Sans MS", 12)).pack(pady=5)
                tk.Button(self.root, text="Rock ✊", command=lambda: self.get_choice(self.player2_name, ROCK), width=15).pack(pady=5)
                tk.Button(self.root, text="Paper 🤚", command=lambda: self.get_choice(self.player2_name, PAPER), width=15).pack(pady=5)
                tk.Button(self.root, text="Scissors ✌️", command=lambda: self.get_choice(self.player2_name, SCISSORS), width=15).pack(pady=5)
            else:
                self.player2_choice = random.randint(1, 3)
                self.display_result()
        else:
            self.player2_choice = choice
            self.display_result()

    def display_result(self):
        self.clear_window()

        player1_choice_name = choices[self.player1_choice]
        player2_choice_name = choices[self.player2_choice]

        tk.Label(self.root, text=f"{self.player1_name} chose: {player1_choice_name}", font=("Comic Sans MS", 12)).pack(pady=5)
        print()
        tk.Label(self.root, text=f"{self.player2_name} chose: {player2_choice_name}", font=("Comic Sans MS", 12)).pack(pady=5)

        if self.player1_choice == self.player2_choice:
            result = "It's a tie! 🤝"
        elif (self.player1_choice == ROCK and self.player2_choice == SCISSORS) or \
             (self.player1_choice == PAPER and self.player2_choice == ROCK) or \
             (self.player1_choice == SCISSORS and self.player2_choice == PAPER):
            result = f"{self.player1_name} wins! 🎉 woo!"
        else:
            result = f"{self.player2_name} wins! 🎉 great job!"

        tk.Label(self.root, text=result, font=("Comic Sans MS", 14, "bold")).pack(pady=10)

        tk.Button(self.root, text="Play Again", command=self.play_round, width=15).pack(pady=5)
        tk.Button(self.root, text="Main Menu", command=self.reset_game, width=15).pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
