import pygame
import gamebox

camera = gamebox.Camera(800, 600)

# create counter and game level vars and facing boolean
counter = 0
game_level = 1
facing = True

character = gamebox.from_image(350, 460, r"C:\Users\jackw\Desktop\CS GAME PROJECT ASSETS\cat_idle.png")

# level 1
background_1 = gamebox.from_image(1000, 300, r"C:\Users\jackw\Desktop\CS GAME PROJECT ASSETS\GAME BACKGROUND.png")
ground_1 = gamebox.from_color(0, 785, 'black', 9000, 600)

# level 2
background_2 = gamebox.from_image(1000, 300, r"C:\Users\jackw\Desktop\CS GAME PROJECT ASSETS\GAME BACKGROUND 2.png")
ground_1 = gamebox.from_color(0, 785, 'black', 9000, 600)

# level 3
background_3 = gamebox.from_image(1000, 300, r"C:\Users\jackw\Desktop\CS GAME PROJECT ASSETS\GAME BACKGROUND 3.png")
ground_1 = gamebox.from_color(0, 785, 'black', 9000, 600)

# finish
finish_text = gamebox.from_image(3510, 400, r"C:\Users\jackw\Desktop\CS GAME PROJECT ASSETS\finish.png")
finish_line = gamebox.from_color(3510, 460, 'white', 20, 50)

# list of projectiles created when facing to the right
projectiles_right = [
]

# list of projectiles created when facing to the left
projectiles_left = [
]

# list of enemies
enemies_right = [
]

enemies_left = [
]


def reset():
    global enemies_left
    global enemies_right
    global projectiles_right
    global projectiles_left

    enemies_left = []
    enemies_right = []
    projectiles_right = []
    projectiles_left = []


def tick(keys):
    global character
    global counter
    global facing
    global game_level
    counter += 1

    game_level = 1

    # sets background and difficulty to level 1
    if game_level == 1:
        camera.draw(background_1)

        start_screen = gamebox.from_image(400, 300, r"C:\Users\jackw\Desktop\CS GAME PROJECT ASSETS\start.png")
        camera.draw(start_screen)

        # if player is facing the the right, camera and character move positively, sprite changes to rightwards facing
        if pygame.K_RIGHT in keys:
            character.x += 5
            camera.x += 5
            facing = True
            character = gamebox.from_image(character.x, character.y,
                                           r"C:\Users\jackw\Desktop\CS GAME PROJECT ASSETS\cat_idle_right.png")

        # if player is facing the the left, camera and character move negatively, sprite changes to leftwards facing
        if pygame.K_LEFT in keys:
            character.x -= 5
            camera.x -= 5
            facing = False
            character = gamebox.from_image(character.x, character.y,
                                           r"C:\Users\jackw\Desktop\CS GAME PROJECT ASSETS\cat_idle_left.png")

        # if space is clicked, projectiles are created in direction according to facing
        if pygame.K_SPACE in keys:
            new_proj = gamebox.from_circle(character.x, character.y, 'white', 3)
            if counter % 10 == 0:
                if facing:
                    projectiles_right.append(new_proj)
                if not facing:
                    projectiles_left.append(new_proj)

        # deletes rightwards projectiles and enemies if they touch
        for projectile in projectiles_right:
            if projectile.x > (camera.x + 500) or projectile.x < (camera.x - 500):
                projectiles_right.remove(projectile)
            projectile.x += 10
            camera.draw(projectile)
            for enemy in enemies_right:
                if projectile.touches(enemy):
                    projectiles_right.remove(projectile)
                    enemies_right.remove(enemy)

        # deletes leftwards projectiles and enemies if they touch
        for projectile in projectiles_left:
            if projectile.x > (camera.x + 500) or projectile.x < (camera.x - 500):
                projectiles_left.remove(projectile)
            projectile.x -= 10
            camera.draw(projectile)
            for enemy in enemies_left:
                if projectile.touches(enemy):
                    projectiles_left.remove(projectile)
                    enemies_left.remove(enemy)

        # creates new enemy every 40 ticks
        if counter % 50 == 0:
            new_enemy = gamebox.from_image(camera.x + 600, 464, r"C:\Users\jackw\Desktop\CS GAME PROJECT ASSETS\zombie_facing_left.png")
            enemies_right.append(new_enemy)
        if counter % 55 == 0:
            new_enemy = gamebox.from_image(camera.x - 600, 464, r"C:\Users\jackw\Desktop\CS GAME PROJECT ASSETS\zombie_facing_right.png")
            enemies_left.append(new_enemy)

        # if character touches enemy, game ends
        for enemy in enemies_right:
            enemy.x -= 4
            if character.touches(enemy):
                gamebox.stop_loop()
            camera.draw(enemy)
        for enemy in enemies_left:
            enemy.x += 5
            if character.touches(enemy):
                gamebox.stop_loop()
            camera.draw(enemy)

        # moves to next level when character touches finish
        if character.touches(finish_line):
            game_level = 2
            character.x = 350
            camera.x = 350
            reset()

    if game_level == 2:
        camera.draw(background_2)

    if game_level == 3:
        camera.draw(background_3)

    camera.draw(character)
    camera.draw(finish_text)

    camera.display()


ticks_per_second = 40
gamebox.timer_loop(ticks_per_second, tick)