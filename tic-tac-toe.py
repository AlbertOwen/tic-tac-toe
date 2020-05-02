# tic-tac-toe game
import turtle
from random import random
from random import seed


ttt_board = [['none', 'none', 'none'], ['none', 'none', 'none'],
             ['none', 'none', 'none']]  # a 3 x 3 list for stone type
ttt_weight = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # a 3 x 3 list for CPU to judge which move to take
t = turtle.Turtle()
wn = turtle.Screen()
wn.title("Tic-Tac-Toe Game")
wn.setup(300, 400)
wn.bgcolor('black')
t.hideturtle()
t.pensize(5)
t.speed(10)
seed(1)
processing = False


# draw the board
def draw_the_board():
    t.pencolor('white')
    t.setheading(0)
    for y in range(4):
        t.penup()
        t.goto(-150, y * 100 - 150)
        t.pendown()
        t.forward(300)
    t.setheading(270)
    for x in range(3):
        t.penup()
        t.goto(x * 100 - 50, 150)
        t.pendown()
        t.forward(300)
    # write a text
    t.penup()
    t.color('deep pink')
    t.goto(-100, 160)
    t.write("Click here to clear", font=("Arial", 16, "normal"))


# draw a circle, the (x, y) is the stone coordinate (0-2, 0-2)
def draw_circle(x, y):
    t.pencolor('green')
    t.penup()
    t.goto(x * 100 - 130, y * 100 - 100)
    t.pendown()
    t.setheading(270)
    t.circle(30)


# draw a cross, the (x, y) is the stone coordinate (0-2, 0-2)
def draw_cross(x, y):
    t.pencolor('blue')
    t.penup()
    t.goto(x * 100 - 130, y * 100 - 70)
    t.pendown()
    t.setheading(-45)
    t.forward(86)
    t.penup()
    t.goto(x * 100 - 130, y * 100 - 130)
    t.pendown()
    t.setheading(45)
    t.forward(86)


# write text
def write_text(text):
    t.penup()
    t.color('deep pink')
    t.goto(-100, -180)
    t.write(text, font=("Arial", 16, "normal"))


# check if there is a win
def game_over():
    # check horizontal lines
    for x in range(3):
        if ttt_board[x][0] == ttt_board[x][1] and ttt_board[x][1] == ttt_board[x][2]:
            if ttt_board[x][0] != 'none':
                return ttt_board[x][0]

    # check vertical lines
    for y in range(3):
        if ttt_board[0][y] == ttt_board[1][y] and ttt_board[1][y] == ttt_board[2][y]:
            if ttt_board[0][y] != 'none':
                return ttt_board[0][y]

    # check diagonal lines
    if ttt_board[0][0] == ttt_board[1][1] and ttt_board[1][1] == ttt_board[2][2]:
        if ttt_board[0][0] != 'none':
            return ttt_board[0][0]
    if ttt_board[0][2] == ttt_board[1][1] and ttt_board[1][1] == ttt_board[2][0]:
        if ttt_board[1][1] != 'none':
            return ttt_board[1][1]

    # check if the board is full
    for x in range(3):
        for y in range(3):
            if ttt_board[x][y] == 'none':
                return 'none'
    # board is full It is a tie
    return 'tie'


# CPU to calculate and move randomly
def cpu_places_a_stone_random():
    while True:
        pos_x = int(random() * 3)
        pos_y = int(random() * 3)
        if ttt_board[pos_x][pos_y] == 'none':
            ttt_board[pos_x][pos_y] = 'cross'
            draw_cross(pos_x, pos_y)
            return


# CPU to block 2 stones
def cpu_places_a_stone_block():
    # check horizontal lines
    for x in range(3):
        if ttt_board[x][0] == ttt_board[x][1] == "circle" and ttt_board[x][2] == 'none':
            ttt_board[x][2] = 'cross'
            draw_cross(x, 2)
            return
        if ttt_board[x][1] == ttt_board[x][2] == "circle" and ttt_board[x][0] == 'none':
            ttt_board[x][0] = 'cross'
            draw_cross(x, 0)
            return
        if ttt_board[x][0] == ttt_board[x][2] == "circle" and ttt_board[x][1] == 'none':
            ttt_board[x][1] = 'cross'
            draw_cross(x, 1)
            return

    # check vertical lines
    for y in range(3):
        if ttt_board[0][y] == ttt_board[1][y] == "circle" and ttt_board[2][y] == 'none':
            ttt_board[2][y] = 'cross'
            draw_cross(2, y)
            return
        if ttt_board[1][y] == ttt_board[2][y] == "circle" and ttt_board[0][y] == 'none':
            ttt_board[0][y] = 'cross'
            draw_cross(0, y)
            return
        if ttt_board[0][y] == ttt_board[2][y] == "circle" and ttt_board[1][y] == 'none':
            ttt_board[1][y] = 'cross'
            draw_cross(1, y)
            return

    # check diagonal lines
    if ttt_board[0][0] == ttt_board[1][1] == "circle" and ttt_board[2][2] == 'none':
        ttt_board[2][2] = 'cross'
        draw_cross(2, 2)
        return
    if ttt_board[1][1] == ttt_board[2][2] == "circle" and ttt_board[0][0] == 'none':
        ttt_board[0][0] = 'cross'
        draw_cross(0, 0)
        return
    if ttt_board[0][0] == ttt_board[2][2] == "circle" and ttt_board[1][1] == 'none':
        ttt_board[1][1] = 'cross'
        draw_cross(1, 1)
        return

    if ttt_board[0][2] == ttt_board[1][1] == "circle" and ttt_board[2][0] == 'none':
        ttt_board[2][0] = 'cross'
        draw_cross(2, 0)
        return
    if ttt_board[2][0] == ttt_board[1][1] == "circle" and ttt_board[0][2] == 'none':
        ttt_board[0][2] = 'cross'
        draw_cross(0, 2)
        return
    if ttt_board[2][0] == ttt_board[0][2] == "circle" and ttt_board[1][1] == 'none':
        ttt_board[1][1] = 'cross'
        draw_cross(1, 1)
        return

    cpu_places_a_stone_random()


# play the game
def play(pos_x, pos_y):
    if pos_x != 99 and pos_y != 99:
        if ttt_board[pos_x][pos_y] == 'none':
            ttt_board[pos_x][pos_y] = 'circle'
            draw_circle(pos_x, pos_y)

            ret = game_over()
            if ret == 'circle':
                write_text("You Won!")
            elif ret == 'cross':
                write_text("Computer Won!")
            elif ret == 'tie':
                write_text("It is a Tie!")
            else:
                cpu_places_a_stone_block()

            ret = game_over()
            if ret == 'circle':
                write_text("You Won!")
            elif ret == 'cross':
                write_text("Computer Won!")
            elif ret == 'tie':
                write_text("It is a Tie!")

    print(ttt_board)


# mouse click call back function
def clicked(mouse_x, mouse_y):
    global processing

    if processing:
        return
    processing = True

    print("you clicked: ", mouse_x, ', ', mouse_y)

    if -100 < mouse_x < 100 and 160 < mouse_y < 180:
        print("Clear the board")
        t.clear()
        draw_the_board()
        # clear ttt_board
        for x in range(3):
            for y in range(3):
                ttt_board[x][y] = 'none'
                ttt_weight[x][y] = 0

    if -40 < mouse_x < 40:
        pos_x = 1
    elif 60 < mouse_x < 130:
        pos_x = 2
    elif -130 < mouse_x < -60:
        pos_x = 0
    else:
        pos_x = 99  # set to an invalid number

    if -40 < mouse_y < 40:
        pos_y = 1
    elif 60 < mouse_y < 130:
        pos_y = 2
    elif -130 < mouse_y < -60:
        pos_y = 0
    else:
        pos_y = 99  # set to an invalid number

    print("pos: ", pos_x, ', ', pos_y)
    play(pos_x, pos_y)
    processing = False


draw_the_board()

wn.onscreenclick(clicked)
wn.mainloop()
