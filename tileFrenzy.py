import pygame
import random
import time

def main():
    difficulty = input("Choose your difficulty (Easy, Medium, Hard, Expert): ")
    if difficulty == "Easy":
        tile_width = 200
        tile_height = 200
        tile_number = 3
    elif difficulty == "Medium":
        tile_width = 150
        tile_height = 150
        tile_number = 3
    elif difficulty == "Hard":
        tile_width = 100
        tile_height = 100
        tile_number = 3
    elif difficulty == "Expert":
        tile_width = 50
        tile_height = 50
        tile_number = 3
    else:
        print("Invalid input")
        return main()

    # initialize Pygame
    pygame.init()

    # set up the game window
    WIDTH = 1920
    HEIGHT = 1080
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tile Frenzy Aim Trainer")

    # define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # set up the clock
    clock = pygame.time.Clock()

    # set up the tiles
    tiles = []
    for i in range(tile_number):
        x = random.randint(tile_width, WIDTH - tile_width)
        y = random.randint(tile_height, HEIGHT - tile_height)
        tiles.append(pygame.Rect(x, y, tile_width, tile_height))

    # set up the score and statistics
    score = 0
    kills = 0
    start_time = time.time()

    # set up the font
    font = pygame.font.Font(None, 36)

    # main game loop
    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # check if a tile was clicked
                for tile in tiles:
                    if tile.collidepoint(pygame.mouse.get_pos()):
                        score += 1
                        tiles.remove(tile)
                        # add a new tile
                        x = random.randint(tile_width, WIDTH - tile_width)
                        y = random.randint(tile_height, HEIGHT - tile_height)
                        tiles.append(pygame.Rect(x, y, tile_width, tile_height))

                        # update the statistics
                        kills += 1
                        accuracy = round(score / kills * 100, 2)

        # fill the window with black
        window.fill(BLACK)

        # draw the tiles
        for tile in tiles:
            pygame.draw.rect(window, WHITE, tile)

        # draw the score and statistics
        score_text = font.render("Score: " + str(score), True, WHITE)
        kills_text = font.render("Kills per second: " + str(round(kills / (time.time() - start_time), 2)), True, WHITE)
        window.blit(score_text, (10, 10))
        window.blit(kills_text, (10, 50))

        # update the window
        pygame.display.update()

        # set the FPS
        clock.tick(60)

    # quit Pygame
    pygame.quit()

main()
