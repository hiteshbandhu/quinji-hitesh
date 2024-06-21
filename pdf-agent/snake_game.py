import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.food = self.place_food()
        self.direction = "Down"
        self.score = 0
        self.game_over = False
        self.update_snake()
        self.update_food()
        self.master.bind("<KeyPress>", self.change_direction)
        self.run_game()

    def place_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return (x, y)

    def update_snake(self):
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 20, segment[1] + 20, fill="green")

    def update_food(self):
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 20, self.food[1] + 20, fill="red")

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym

    def run_game(self):
        if not self.game_over:
            self.move_snake()
            self.check_collisions()
            self.master.after(100, self.run_game)

    def move_snake(self):
        head_x, head_y = self.snake[-1]
        if self.direction == "Up":
            new_head = (head_x, head_y - 20)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 20)
        elif self.direction == "Left":
            new_head = (head_x - 20, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 20, head_y)
        self.snake.append(new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.place_food()
            self.update_food()
        else:
            del self.snake[0]
        self.canvas.delete(tk.ALL)
        self.update_snake()
        self.update_food()

    def check_collisions(self):
        head_x, head_y = self.snake[-1]
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400:
            self.game_over = True
        if len(self.snake) != len(set(self.snake)):
            self.game_over = True
        if self.game_over:
            self.canvas.create_text(200, 200, text="Game Over", fill="red", font=("Helvetica", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()