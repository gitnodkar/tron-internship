from tkinter import *
import random

# Constants
GAME_WIDTH, GAME_HEIGHT = 15, 15
SNAKE_COLOR, FOOD_COLOR, BACKGROUND_COLOR = "#00FF00", "#FF0000", "#000000"
GRID_COLOR = "#333333"
SPACE_SIZE = 30
SPEED = 100

class Snake:
    def __init__(self):
        self.body = [(0, 0)]
        self.direction = (1, 0)  # Initial direction: right

class Food:
    def __init__(self):
        self.coordinates = (0, 0)

def create_food():
    x = random.randint(0, GAME_WIDTH - 1)
    y = random.randint(0, GAME_HEIGHT - 1)
    food.coordinates = (x, y)
    canvas.create_oval(x * SPACE_SIZE, y * SPACE_SIZE, (x + 1) * SPACE_SIZE, (y + 1) * SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn():
    x, y = snake.body[0]
    x = (x + snake.direction[0]) % GAME_WIDTH
    y = (y + snake.direction[1]) % GAME_HEIGHT

    if (x, y) in snake.body:
        snake_hit()
        return

    snake.body.insert(0, (x, y))
    canvas.create_rectangle(x * SPACE_SIZE, y * SPACE_SIZE, (x + 1) * SPACE_SIZE, (y + 1) * SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")

    if (x, y) == food.coordinates:
        global score
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        create_food()
    else:
        x, y = snake.body[-1]
        canvas.create_rectangle(x * SPACE_SIZE, y * SPACE_SIZE, (x + 1) * SPACE_SIZE, (y + 1) * SPACE_SIZE, fill=BACKGROUND_COLOR)

        snake.body.pop()

    window.after(SPEED, next_turn)

def snake_hit():
    global lives
    lives -= 1
    label.config(text=f"Score: {score} | Lives: {lives}")

    if lives == 0:
        game_over()
    else:
        # Reset snake position
        canvas.delete("snake")
        snake.body = [(0, 0)]
        snake.direction = (1, 0)
        create_food()
        next_turn()

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 50),
                       text="GAME OVER", fill="red", tag="gameover")

def change_direction(new_direction):
    snake.direction = new_direction

# Initialize the game
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
lives = 3
label = Label(window, text=f"Score: {score} | Lives: {lives}", font=('consolas', 20))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT * SPACE_SIZE, width=GAME_WIDTH * SPACE_SIZE)
canvas.pack()

for i in range(0, GAME_WIDTH * SPACE_SIZE, SPACE_SIZE):
    for j in range(0, GAME_HEIGHT * SPACE_SIZE, SPACE_SIZE):
        canvas.create_rectangle(i, j, i + SPACE_SIZE, j + SPACE_SIZE, outline=GRID_COLOR)

window.update()

window_width, window_height = window.winfo_width(), window.winfo_height()
screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
x, y = int((screen_width - window_width) / 2), int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction((-1, 0)))
window.bind('<Right>', lambda event: change_direction((1, 0)))
window.bind('<Up>', lambda event: change_direction((0, -1)))
window.bind('<Down>', lambda event: change_direction((0, 1)))

snake = Snake()
food = Food()
create_food()

next_turn()

window.mainloop()
