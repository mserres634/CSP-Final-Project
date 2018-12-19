
from sense_hat import SenseHat
sense = SenseHat()
from time import sleep


red= (225, 0, 0)
orange= (225, 165, 0)
yellow= (225, 225, 0)
green= (0, 225, 0)
blue= (0, 0, 225)
purple= (128, 0, 128)
white= (225, 225, 225)
colors = [red, orange, yellow, green, blue, purple]


bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]





def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)


def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], white)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y +1):
        ball_velocity[0] = -ball_velocity[0]
    
    



def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1



def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y += 1


  
draw_bat()
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down



while True:
    for color in colors:

        draw_ball()
        if ball_position[0] == 0:
          sense.show_message("RUN.SAD")
          break;
        draw_bat()
        sleep(.25)
        sense.clear(color)

