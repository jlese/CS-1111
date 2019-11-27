# jwl4vg Jack Lesemann

import pygame
import gamebox
import random

# create gamebox and dinosaur
camera = gamebox.Camera(800, 600)
character = gamebox.from_image(400, 300, r"C:\Users\jackw\Downloads\download (2).png")

# create score, counter var, allow game loop to start
score = 0
counter = 0
game_on = True
walls = []

# draw ground
ground = gamebox.from_color(400, 465, "black", 99999999, 300)


def cactus_reset():
    '''
    resets cacti
    :return:
    '''
    global walls

    walls = []


def tick(keys):
    '''
    game code here
    :param keys:
    :return:
    '''
    global counter
    global score
    global game_on

    if game_on:
        # create score
        score_number = gamebox.from_text(camera.x + 3, 20, str(score // 5), 30, 'black')

        # keep scoreboard moving with camera
        score_number.x += 3

        # allow player to jump
        if character.y == 296.5:
            if pygame.K_UP in keys:
                character.y -= 100
        else:
            character.y += .5

        # set background, scroll camera, and draw character
        camera.clear("white")
        camera.draw(character)
        camera.x += 3

        # keep character centered and create sense of gravity
        character.x += 3
        character.y += 2
        character.move_to_stop_overlapping(ground)

        camera.draw(score_number)

        counter += 1
        score += 1

        # create new randomly spaced cacti
        if counter % 70 == 0:
            new_wall = gamebox.from_image(camera.x + 300 + random.randint(150, 250), 300,
                                          r"C:\Users\jackw\Downloads\cactus (1).jpg")
            walls.append(new_wall)

        for wall in walls:
            # stop game loop if character hits wall and move to outside if
            if character.touches(wall):
                game_on = False
            camera.draw(wall)

        camera.draw(ground)
        camera.display()
    else:
        camera.clear("black")

        # display text
        end_screen1 = gamebox.from_text(camera.x + 3, 250, "GAME OVER", 30, 'red')
        camera.draw(end_screen1)

        end_screen2 = gamebox.from_text(camera.x + 3, 300, "YOUR FINAL SCORE WAS " + str(score // 5), 30, 'red')
        camera.draw(end_screen2)

        end_screen3 = gamebox.from_text(camera.x + 3, 350, "PRESS SPACE TO RESTART OR X TO QUIT", 30, 'red')
        camera.draw(end_screen3)

        # restart or quit
        if pygame.K_SPACE in keys:
            cactus_reset()
            game_on = True
            score = 0
        elif pygame.K_x in keys:
            gamebox.stop_loop()

        camera.display()


ticks_per_second = 40
gamebox.timer_loop(ticks_per_second, tick)
