import pygame
import time
import random


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (180, 0, 0)
green = (0, 170, 0)
yellow = (200, 200, 0)
yellow_claro = (255, 255, 0)
green_claro = (0, 255, 0)
red_claro = (255, 0, 0)

pygame.display.set_caption('BangBang')

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()


turret_width = 5
roda_width = 5

tank_width = 40
tank_height = 20

ground_height = 35

font_small = pygame.font.SysFont("arial", 25)
font_med = pygame.font.SysFont("arial", 50)
font_large = pygame.font.SysFont("arial", 85)


def score(score):
    text = font_small.render("Score: " + str(score), True. black)
    screen.blit(text, [0,0])


def text_obj(text, color, size = "small"):

    if size == "small":
        text_surface = font_small.render(text, True, color)
    if size == "medium":
        text_surface = font_med.render(text, True, color)
    if size == "large":
        text_surface = font_large.render(text, True, color)

    return text_surface, text_surface.get_rect()


def text_to_button(msg, color, buttonx, buttony, bwidth, bheight, size="small"):
    text_surf, text_rect = text_obj(msg, color, size)
    text_rect.center = ((buttonx + (bwidth / 2)), buttony + (bheight / 2))
    screen.blit(text_surf, text_rect)


def message_to_screen(msg, color, y_deslocamento=0, size="small"):
    text_surf, text_rect = text_obj(msg, color, size)
    text_rect.center = (int(screen_width / 2)), int(screen_height / 2) + y_deslocamento
    screen.blit(text_surf, text_rect)


def tank(x, y, turposition):
    x = int(x)
    y = int(y)

    possibleturrets = [(x-27, y-2),
                       (x-26, y-5),
                       (x-25, y-8),
                       (x-23, y-12),
                       (x-20, y-14),
                       (x-18, y-15),
                       (x-15, y-17),
                       (x - 13, y - 19),
                       (x - 11, y - 21)
                       ]


    pygame.draw.circle(screen, black, (x,y), int(tank_height)/2)
    pygame.draw.rect(screen, black, (x-tank_height, y, tank_width, tank_height))

    pygame.draw.line(screen, black, (x,y), possibleturrets[turposition], turret_width)

    pygame.draw.circle(screen, black, (x-15, y+20), roda_width)
    pygame.draw.circle(screen, black, (x-10, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x-5, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x+5, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x+10, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x+15, y + 20), roda_width)

    return possibleturrets[turposition]

def enemy_tank(x, y, turposition):
    x = int(x)
    y = int(y)

    possibleturrets = [(x + 27, y - 2),
                       (x + 26, y - 5),
                       (x + 25, y - 8),
                       (x + 23, y - 12),
                       (x + 20, y - 14),
                       (x + 18, y - 15),
                       (x + 15, y - 17),
                       (x+13, y - 19),
                       (x + 11, y - 21)
                       ]

    pygame.draw.circle(screen, black, (x, y), int(tank_height) / 2)
    pygame.draw.rect(screen, black, (x - tank_height, y, tank_width, tank_height))

    pygame.draw.line(screen, black, (x, y), possibleturrets[turposition], turret_width)

    pygame.draw.circle(screen, black, (x - 15, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x - 10, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x - 5, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x + 5, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x + 10, y + 20), roda_width)
    pygame.draw.circle(screen, black, (x + 15, y + 20), roda_width)

    return possibleturrets[turposition]

    # x_init = 15
    # for x in range(8):
    #     pygame.draw.circle(screen, black, (x-x_init, y+20), roda_width)
    #     x_init -= 5


def controls():

    cont = True

    while cont:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        message_to_screen("Controls", green, -100, size="large")
        message_to_screen("Fire: Spacebar", black, -30)
        message_to_screen("Move Turret: Up and Down arrows ", black, 10)
        message_to_screen("Move Turret: Left and Right arrows ", black, 50)
        message_to_screen("Increase / decrease power: A and D keys", black, 90)
        message_to_screen("Pause: P", black, 130)

        button("Play", 150, 500, 100, 50, green, green_claro, action="play")
        # button("Main Menu", 350, 500, 100, 50, green, green_claro, action="MainMenu")
        button("Quit", 550, 500, 100, 50, red, red_claro, action="quit")

        pygame.display.update()

        clock.tick(15)


def button(text, x ,y, width, height, color, acolor, action=None):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > cursor[0] > x and y+height > cursor[1] > y:
        pygame.draw.rect(screen, acolor, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                controls()

            if action == "play":
                gameloop()

    else:
        pygame.draw.rect(screen, color,(x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def pause():
    paused = True
    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press C to continue playing or Q to quit", black, 25)
    pygame.display.update()
    while paused:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_c:
                    paused = False
                elif ev.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)


def barrier(xloc, randomheight, barrier_width):
    pygame.draw.rect(screen, black, [xloc, screen_height - randomheight, barrier_width, randomheight])


def explosion(x, y, size=50):
    explosion = True
    while explosion:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        startpoint = x, y
        colours = [red, red_claro, yellow, yellow_claro]

        magnitude = 1
        while magnitude < size:
            x_explosion = x + random.randrange(-1*magnitude, magnitude)
            y_explosion = y + random.randrange(-1 * magnitude, magnitude)

            pygame.draw.circle(screen, colours[random.randrange(0, 4)], (x_explosion, y_explosion), random.randrange(1, 5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explosion = False



def fire(x_y, tankx, tanky, turpos, gunpower, xloc, barrier_width, randomheight, tank2x, tank2y):
    fire = True
    damage = 0

    bullet = list(x_y)
    print("FIRE", x_y)

    while fire:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        # print(bullet[0], bullet[1])
        pygame.draw.circle(screen, red, (bullet[0], bullet[1]), 5)

        bullet[0] -= (12 - turpos) * 2
        bullet[1] += int((((bullet[0] - x_y[0])*0.015/(gunpower/50))**2) - (turpos + turpos/(12-turpos)))

        if bullet[1] > screen_height- ground_height:
            print("ultimo", bullet[0], bullet[1])
            hit_x = int((bullet[0] * screen_height - ground_height)/bullet[1])
            hit_y = int(screen_height - ground_height)
            print("impact", hit_x, hit_y)

            if tank2x + 10 > hit_x > tank2x - 10:
                print("Critical Hit")
                damage = 25
            elif tank2x + 15 > hit_x > tank2x - 15:
                print("Hard Hit")
                damage = 18
            elif tank2x + 25 > hit_x > tank2x - 25:
                print("Medium Hit")
                damage = 10
            elif tank2x + 35 > hit_x > tank2x - 35:
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        check_x1 = bullet[0] <= xloc + barrier_width
        check_x2 = bullet[0] >= xloc
        check_y1 = bullet[1] <= screen_height
        check_y2 = bullet[1] >= screen_height - randomheight

        if check_x1 and check_x2 and check_y1 and check_y2:
            print("ultimo", bullet[0], bullet[1])
            hit_x = int(bullet[0])
            hit_y = int(bullet[1])
            print("impact", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage


def enemy_fire(x_y, tankx, tanky, turpos, gunpower, xloc, barrier_width, randomheight, ptankx, ptanky):

    damage = 0
    power_atual = 1
    power_found = False

    while not power_found:
        power_atual +=1

        if power_atual > 100:
            power_found = True
        fire = True
        bullet = list(x_y)

        while fire:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # pygame.draw.circle(screen, red, (bullet[0], bullet[1]), 5)

            bullet[0] += (12 - turpos) * 2

            gunpower = random.randrange(int(power_atual*0.8), int(power_atual*1.25))
            bullet[1] += int((((bullet[0] - x_y[0]) * 0.015 / (gunpower / 50)) ** 2) - (turpos + turpos / (12 - turpos)))

            if bullet[1] > screen_height - ground_height:
                hit_x = int((bullet[0] * screen_height - ground_height) / bullet[1])
                hit_y = int(screen_height - ground_height)
                if ptankx+15 > hit_x > ptankx-15:
                    print("HELL YEAH!")
                    power_found = True
                fire = False

            check_x1 = bullet[0] <= xloc + barrier_width
            check_x2 = bullet[0] >= xloc
            check_y1 = bullet[1] <= screen_height
            check_y2 = bullet[1] >= screen_height - randomheight

            if check_x1 and check_x2 and check_y1 and check_y2:
                hit_x = int(bullet[0])
                hit_y = int(bullet[1])
                # explosion(hit_x, hit_y)
                fire = False


    fire = True
    bullet = list(x_y)
    print("FIRE", x_y)

    while fire:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(screen, red, (bullet[0], bullet[1]), 5)


        bullet[0] += (12 - turpos) * 2
        bullet[1] += int((((bullet[0] - x_y[0])*0.015/(power_atual/50))**2) - (turpos + turpos/(12-turpos)))

        if bullet[1] > screen_height- ground_height:
            print("ultimo", bullet[0], bullet[1])
            hit_x = int((bullet[0] * screen_height - ground_height)/bullet[1])
            hit_y = int(screen_height - ground_height)
            print("impact",hit_x, hit_y)
            if ptankx + 15 > hit_x > ptankx - 15:
                print("HIT!")
                damage = 25
            explosion(hit_x, hit_y)
            fire = False

        check_x1 = bullet[0] <= xloc + barrier_width
        check_x2 = bullet[0] >= xloc
        check_y1 = bullet[1] <= screen_height
        check_y2 = bullet[1] >= screen_height - randomheight

        if check_x1 and check_x2 and check_y1 and check_y2:
            print("ultimo", bullet[0], bullet[1])
            hit_x = int(bullet[0])
            hit_y = int(bullet[1])
            print("impact", hit_x, hit_y)

            if ptankx + 10 > hit_x > ptankx - 10:
                print("Critical Hit")
                damage = 25
            elif ptankx + 15 > hit_x > ptankx - 15:
                print("Hard Hit")
                damage = 18
            elif ptankx + 25 > hit_x > ptankx - 25:
                print("Medium Hit")
                damage = 10
            elif ptankx + 35 > hit_x > ptankx - 35:
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage


def power(nivel):
    text = font_small.render("Power: " + str(nivel) + "%", True, black)
    screen.blit(text, [screen_width/2, 0])


def game_intro():

    intro = True

    while intro:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_c:
                    intro = False
                elif ev.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.fill(white)
        message_to_screen("BangBang!", green, -100, size="large")
        message_to_screen("The objective is to destroy the other tank!", black, -30)
        # message_to_screen("Press C to Play, P to pause or Q to quit", black, 50)

        button("Play", 150, 500, 100, 50, green, green_claro, action="play")
        button("Controls", 350, 500, 100, 50, green, green_claro, action="controls")
        button("Quit", 550, 500, 100, 50, red, red_claro, action="quit")

        pygame.display.update()

        clock.tick(15)


def game_over():

    gameover = True

    while gameover:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        message_to_screen("Game Over", green, -100, size="large")
        message_to_screen("You lost", black, -30)

        button("Play Again", 150, 500, 150, 50, green, green_claro, action="play")
        button("Controls", 350, 500, 100, 50, green, green_claro, action="controls")
        button("Quit", 550, 500, 100, 50, red, red_claro, action="quit")

        pygame.display.update()

        clock.tick(15)


def win():

    win = True

    while win:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        message_to_screen("You Won", green, -100, size="large")
        message_to_screen("Congratulations!", black, -30)

        button("Play Again", 150, 500, 150, 50, green, green_claro, action="play")
        button("Controls", 350, 500, 100, 50, green, green_claro, action="controls")
        button("Quit", 550, 500, 100, 50, red, red_claro, action="quit")

        pygame.display.update()

        clock.tick(15)


def health_bars(player_health, enemy_health):
    if player_health > 75:
        player_health_colour = green
    elif player_health > 50:
        player_health_colour = yellow
    else:
        player_health_colour = red

    if enemy_health > 75:
        enemy_health_colour = green
    elif enemy_health > 50:
        enemy_health_colour = yellow
    else:
        enemy_health_colour = red

    pygame.draw.rect(screen, player_health_colour, (680, 25, player_health, 25))
    pygame.draw.rect(screen, enemy_health_colour, (20, 25, enemy_health, 25))


def gameloop():
    gameexit = False
    gameover = False
    FPS = 30

    player_health = 100
    enemy_health = 100

    tank1x = screen_width * 0.9
    tank1y = screen_height * 0.9
    tankmove = 0
    turposition_atual = 0
    changetur = 0

    tank2x = screen_width * 0.1
    tank2y = screen_height * 0.9

    firepower = 50
    powerchange = 0

    xloc = (screen_width/2) + random.randint(-0.1 * screen_width, 0.1 * screen_width)
    randomheight = random.randrange(screen_height * 0.1, screen_height * 0.5)
    barrier_width = 50


    while not gameexit:
        if gameover:
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gameover:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        gameexit = True
                        gameover = False
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_c:
                            gameloop()
                        elif ev.key == pygame.K_c:
                            gameexit = True
                            gameover = False

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                gameexit = True

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    tankmove = -5

                elif ev.key == pygame.K_RIGHT:
                    tankmove = 5

                elif ev.key == pygame.K_UP:
                    changetur = 1

                elif ev.key == pygame.K_DOWN:
                    changetur = -1

                elif ev.key == pygame.K_p:
                    pause()

                elif ev.key == pygame.K_SPACE:
                    damage = fire(gun, tank1x, tank1y, turposition_atual, firepower, xloc, barrier_width, randomheight, tank2x, tank2y)
                    enemy_health -= damage

                    possiblemovement = ["f", "r"]
                    moveindex = random.randrange(0, 2)

                    for x in range(random.randrange(0, 10)):
                        if screen_width * 0.3 > tank2x > screen_width * 0.03:
                            if possiblemovement[moveindex] == "f":
                                tank2x += 8
                            elif possiblemovement[moveindex] == "r":
                                tank2x -= 8

                            screen.fill(white)
                            health_bars(player_health, enemy_health)
                            gun = tank(tank1x, tank1y, turposition_atual)
                            enemy_gun = enemy_tank(tank2x, tank2y, 8)
                            firepower += powerchange

                            power(firepower)

                            barrier(xloc, randomheight, barrier_width)
                            screen.fill(green, rect=[0, screen_height - ground_height, screen_width, ground_height])

                            pygame.display.update()

                            clock.tick(FPS)


                    damage = enemy_fire(enemy_gun, tank2x, tank2y, 8, 50, xloc, barrier_width, randomheight, tank1x, tank1y)
                    player_health -= damage

                elif ev.key == pygame.K_a:
                    powerchange = -1

                elif ev.key == pygame.K_d:
                    powerchange = 1

            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_LEFT or ev.key == pygame.K_RIGHT:
                    tankmove = 0

                if ev.key == pygame.K_UP or ev.key == pygame.K_DOWN:
                    changetur = 0

                if ev.key == pygame.K_a or ev.key == pygame.K_d:
                    powerchange = 0

        tank1x += tankmove

        turposition_atual += changetur

        if turposition_atual > 8:
            turposition_atual = 8
        elif turposition_atual < 0:
            turposition_atual = 0

        if tank1x - (tank_width/2) < xloc + barrier_width:
            tank1x += 5

        screen.fill(white)
        health_bars(player_health, enemy_health)
        gun = tank(tank1x, tank1y, turposition_atual)
        enemy_gun = enemy_tank(tank2x, tank2y, 8)

        firepower += powerchange

        if firepower > 100:
            firepower = 100
        elif firepower < 1:
            firepower = 1

        power(firepower)

        barrier(xloc, randomheight, barrier_width)
        screen.fill(green, rect=[0, screen_height - ground_height, screen_width, ground_height])

        pygame.display.update()

        if player_health < 1:
            game_over()
        elif enemy_health < 1:
            win()

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameloop()







