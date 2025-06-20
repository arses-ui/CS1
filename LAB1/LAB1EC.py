#Pong
#Author name: Arses Prasai
#Purpose- Lab 1
#Date: 3rd February


#attempts for extra credit
#1. score board
#2. different colored score side and a middle line
#3. change color to opposite side's color on crossing the middle line
#4. home page
#5. end the game when certain score and reset the count
#6. exit page
#7. glittery effect on the home screen

from cs1lib import *
from random import*

# booleans to change the position of the paddle
left_paddle_up = False
left_paddle_down= False
right_paddle_up = False
right_paddle_down = False

#booleans to change the screens
game_start= False
switch_to_game= False
change_screen= False
game_stop = False

#boolean to quit the program
quit_game= False

#constant variables
BOARD_WIDTH = 40
BOARD_HEIGHT = 160
SCREEN_SIZE = 800
LEFT_PADDLE_U = "a"
LEFT_PADDLE_D= "z"
RIGHT_PADDLE_U= "k"
RIGHT_PADDLE_D="m"
QUIT = "q"
START_GAME= " "


#coordinates for the left paddle
ax= 0
ay=0

#coordinates for right paddle
bx= SCREEN_SIZE - BOARD_WIDTH
by = SCREEN_SIZE- BOARD_HEIGHT

#parameters for the position of the ball
ball_radius= 20
x= 400
y= 400
x_speed = 15
y_speed = 15
speed_factor= 1.01

# other parameters/ variables
score_right_side = 0
score_left_side = 0
r= 0
g= 0
b= 0

# function to draw the ball and change its color based on its position
def pong_ball():
    global ball_radius, x, y, r, g, b
    set_fill_color(r,g,b)

    # ball changes colors as it crosses the halfway line
    draw_circle(x,y, ball_radius)
    if x<400:
        r = 0
        g= 0
        b= 0.5
    if x>400:
        r = 0.5
        g = 0
        b = 0
    if x == 400:
        r= 0
        g= 0
        b= 0

#function to change/ vary the position of the ball
def ball_position():
    global ball_radius, x, y, game_start, x_speed, y_speed, speed_factor

    #once the game starts, ball moves towards bottom right corner.
    if game_start:
        x += x_speed
        y += y_speed

# function for when ball hits the paddle
def collision_with_paddle():
    global  ball_radius, ay, by, ax, bx, x, y, x_speed, y_speed

    # when the ball touches the left paddle
    if  x - ball_radius <= BOARD_WIDTH and ay <= y <= ay + BOARD_HEIGHT:
        x+=10
        x_speed= - x_speed
        y_speed = y_speed * speed_factor
        x_speed = x_speed * speed_factor

    #when the ball touches  right paddle
    if x + ball_radius >= bx and by<= y <= by+ BOARD_HEIGHT:
        x_speed= - x_speed
        x-=10
        x_speed = x_speed*speed_factor
        y_speed = y_speed*speed_factor



#function to end the reposition when ball hits the vertical wall
def reset_game():
    global   x, y, game_start, score_left_side, score_right_side, x_speed, y_speed, by, ay, game_stop

    set_stroke_width(5)

    # when the ball ends up on the right side
    if x + ball_radius >= SCREEN_SIZE:
        #reposition the ball
        x = SCREEN_SIZE / 2
        y = SCREEN_SIZE / 2

        #reposition the paddle
        by = SCREEN_SIZE - BOARD_HEIGHT
        ay = 0

        # don't reset the speed
        x_speed= abs(x_speed)
        y_speed = abs(y_speed)

        game_start = False
        score_left_side += 1 #updates the score


    #when the ball ends up on the left side
    if x - ball_radius <= 0:

        #reposition ball
        x = SCREEN_SIZE/2
        y = SCREEN_SIZE/2

        # reposition paddle
        by = SCREEN_SIZE - BOARD_HEIGHT
        ay = 0

        #don't reset the speed
        x_speed = abs(x_speed)
        y_speed = abs(y_speed)

        game_start = False
        score_right_side += 1 #updates the score

    #condition to move to the exit page when one player reaches score of 10
    if score_left_side == 10 or score_right_side == 10:
            game_stop = True
            game_start = False


#function to restart the game and reset all the parameters
def restart_game():
    global score_right_side, score_left_side, game_start, x, y, x_speed, y_speed, ay, by
    x = SCREEN_SIZE / 2
    y = SCREEN_SIZE / 2
    score_right_side = 0
    score_left_side = 0
    x_speed = 15
    y_speed = 15
    by = SCREEN_SIZE - BOARD_HEIGHT
    ay = 0
    game_start= False


#function to end the game and text you to the exit page
def exit_page():
    global game_stop, score_right_side, score_left_side, game_start, x, y, x_speed, y_speed, ay, by

    # if  the counter reaches to 10, stop the game, move to a different page and reset the variables for the counter

    if game_stop:
        set_fill_color(0.5,0,0)
        draw_rectangle(0,0,400,800)
        set_fill_color(0,0,0.5)
        draw_rectangle(400,0,400,800)
        set_stroke_color(1,1,1)
        set_font_size(20)
        draw_text("GAME OVER", 230,200)
        set_font_size(10)
        draw_text("press r to restart",300,400)
        draw_text("press q to quit the game", 300, 450)
        restart_game()


#function to quit the game
def quit_pong():
    global quit_game
    if quit_game:
        cs1_quit()


#a function to draw the score board on the screen
def score_board():
    global score_left_side, score_right_side
    set_font_size(20)
    set_stroke_color(1,1,1)

    draw_text(str(score_left_side) ,250,50)
    draw_text(str(score_right_side),550, 50)
    set_stroke_color(0,0,0)

# function to change the ball's trajectory on touching the upper and lower walls
def check_horizontal_walls():
    global y, ball_radius, y_speed

    if y >= SCREEN_SIZE - ball_radius:
        y_speed = -y_speed

    if y <= ball_radius:
        y_speed= -y_speed


#define a function for recording keys pressed
def keyboard_press(value):

    global left_paddle_up, left_paddle_down, right_paddle_up, right_paddle_down, game_start, quit_game, change_screen, game_stop
    if value == LEFT_PADDLE_U:
        left_paddle_up= True
    if value == LEFT_PADDLE_D:
        left_paddle_down= True
    if value == RIGHT_PADDLE_U:
        right_paddle_up= True
    if value == RIGHT_PADDLE_D:
        right_paddle_down= True
    if value == "s":
        change_screen = True
    if value == QUIT:
        quit_game = True
    if value == START_GAME:
        game_start = True


#define a function for keys released
def keyboard_release(value):
    global left_paddle_up, left_paddle_down, right_paddle_up, right_paddle_down, game_start, quit_game, change_screen, game_stop
    if value == LEFT_PADDLE_U:
        left_paddle_up = False
    if value == LEFT_PADDLE_D:
        left_paddle_down = False
    if value == RIGHT_PADDLE_U:
        right_paddle_up = False
    if value == RIGHT_PADDLE_D:
        right_paddle_down = False
    if value == QUIT:
        quit_game= False
    if value == "r":
        game_stop = False
        restart_game()


def paddle_boards():
    global ax, ay, bx, by, right_paddle_up, right_paddle_down, left_paddle_down, left_paddle_up

    # draw the paddles
    set_fill_color(0.5,0.5,0.5)
    draw_rectangle(ax, ay, BOARD_WIDTH, BOARD_HEIGHT )
    draw_rectangle( bx, by, BOARD_WIDTH, BOARD_HEIGHT)

    #condition for the paddles to move
    if left_paddle_up and ay >0:
        ay -= 15

    if left_paddle_down and ay < SCREEN_SIZE - BOARD_HEIGHT:
        ay += 15

    if right_paddle_up and by >0:
        by-= 15

    if right_paddle_down and by < SCREEN_SIZE - BOARD_HEIGHT:
        by+= 15

#define a function to draw and move the paddle boards
def main_draw():
    global change_screen

    #welcome screen before starting the game
    if not change_screen:
        clear()
        set_stroke_color(uniform(0, 1.0), uniform(0, 1.0), uniform(0, 1.0))
        set_font_size(10)
        set_fill_color(0.5, 0,0)
        draw_rectangle(0, 0, 400, 800)
        set_fill_color(0,0,0.5)
        draw_rectangle(400,0,400,800)
        draw_text("WELCOME TO THE GAME", 220, 350)
        draw_text("PRESS s TO CONTINUE ", 230, 400)
        draw_text("PRESS q AT ANY MOMENT TO QUIT THE GAME", 120, 450)

    #once a key (s) is pressed, the homepage goes away and the game screen appears
    if change_screen:
        clear()
        set_fill_color(0.5, 0, 0)
        draw_rectangle(0, 0, 400, 800)
        set_fill_color(0,0,0.5)
        draw_rectangle(400,0,400,800)

        pong_ball()
        collision_with_paddle()
        ball_position()
        check_horizontal_walls()
        paddle_boards()
        reset_game()
        score_board()
        quit_pong()
        exit_page()

start_graphics(main_draw, width= SCREEN_SIZE, height=SCREEN_SIZE, key_release= keyboard_release, key_press=keyboard_press)







