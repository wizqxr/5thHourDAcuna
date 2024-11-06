import os
import random
import time

# Game settings
width = 20
height = 10
snake = [(width // 2, height // 2)]
direction = (0, 1)  # Start moving right
food = (random.randint(0, width - 1), random.randint(0, height - 1))

def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(height):
        for x in range(width):
            if (x, y) == snake[0]:
                print('O', end='')  # Snake head
            elif (x, y) in snake[1:]:
                print('o', end='')  # Snake body
            elif (x, y) == food:
                print('*', end='')  # Food
            else:
                print(' ', end='')
        print()

def move_snake():
    global food
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Check for collisions
    if (new_head in snake) or (new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height):
        return False  # Game over

    # Update snake
    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randint(0, width - 1), random.randint(0, height - 1))
    else:
        snake.pop()  # Remove the tail

    return True

# Game loop
while True:
    draw()

    # Input direction
    direction_input = input("Enter direction (w/a/s/d): ").strip().lower()
    if direction_input == 'w':
        direction = (0, -1)  # Up
    elif direction_input == 's':
        direction = (0, 1)   # Down
    elif direction_input == 'a':
        direction = (-1, 0)  # Left
    elif direction_input == 'd':
        direction = (1, 0)   # Right

    if not move_snake():
        print("Game Over!")
        break

    time.sleep(0.2)
