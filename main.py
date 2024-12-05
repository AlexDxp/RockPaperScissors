from inspect import EndOfBlock

import pygame
import random
from pygame import MOUSEBUTTONDOWN
import time
WHITE = (255, 255, 255)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RockPaperScissors")
screen.fill(WHITE)
pygame.display.flip()
imp = pygame.image.load("RockPaperScissors Images/Rock.png")
screen.blit(imp, (0, 200))
imp = pygame.image.load("RockPaperScissors Images/Paper.png")
screen.blit(imp, (200, 200))
imp = pygame.image.load("RockPaperScissors Images/Scissors.png")
screen.blit(imp, (400, 200))
pygame.display.flip()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                is_click = False
                while True:
                    if 0 <= x <= 200 and 200 <= y <= 400:
                        player = "Rock"
                        is_click = True
                    elif 200 < x <= 400 and 200 <= y <= 400:
                        player = "Paper"
                        is_click = True
                    elif 400 < x <= 600 and 200 <= y <= 400:
                        player = "Scissors"
                        is_click = True
                    else:
                        is_click = False
                    break
                if is_click:

                    game = random.randint(0,2)

                    if game == 0:
                        game = "Rock"
                    elif game == 1:
                        game = "Paper"
                    elif game == 2:
                        game = "Scissors"
                    imp = pygame.image.load("ROCK! PAPER! SCISSORS! SHOOT!/ROCK!.png")
                    screen.blit(imp, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.6)
                    imp = pygame.image.load("ROCK! PAPER! SCISSORS! SHOOT!/ROCK! PAPER!.png")
                    screen.blit(imp, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.6)
                    imp = pygame.image.load("ROCK! PAPER! SCISSORS! SHOOT!/ROCK! PAPER! SCISSORS!.png")
                    screen.blit(imp, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.6)
                    imp = pygame.image.load("ROCK! PAPER! SCISSORS! SHOOT!/SHOOT!.png")
                    screen.blit(imp, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.6)
                    imp = pygame.image.load("Blank.png")
                    screen.blit(imp, (0, 0))
                    pygame.display.flip()

                    if game == "Rock":
                        imp = pygame.image.load("RockPaperScissors Images/Rock.png")
                        screen.blit(imp, (200, 0))
                        pygame.display.flip()
                    elif game == "Paper":
                        imp = pygame.image.load("RockPaperScissors Images/Paper.png")
                        screen.blit(imp, (200, 0))
                        pygame.display.flip()
                    elif game == "Scissors":
                        imp = pygame.image.load("RockPaperScissors Images/Scissors.png")
                        screen.blit(imp, (200, 0))
                        pygame.display.flip()
                    if player == "Rock":
                        imp = pygame.image.load("RockPaperScissors Images/Rock.png")
                        screen.blit(imp, (200, 200))
                        pygame.display.flip()
                    elif player == "Paper":
                        imp = pygame.image.load("RockPaperScissors Images/Paper.png")
                        screen.blit(imp, (200, 200))
                        pygame.display.flip()
                    elif player == "Scissors":
                        imp = pygame.image.load("RockPaperScissors Images/Scissors.png")
                        screen.blit(imp, (200, 200))
                        pygame.display.flip()
                    time.sleep(1)

                    if player == game:
                        imp = pygame.image.load("End Screens/It's a TIE.png")
                        screen.blit(imp, (0, 0))
                        pygame.display.flip()
                    elif player == "Rock" and game == "Scissors":
                        imp = pygame.image.load("End Screens/You Win.png")
                        screen.blit(imp, (0, 0))
                        pygame.display.flip()
                    elif player == "Rock" and game == "Paper":
                        imp = pygame.image.load("End Screens/You Lose.png")
                        screen.blit(imp, (0, 0))
                        pygame.display.flip()
                    elif player == "Paper" and game == "Scissors":
                        imp = pygame.image.load("End Screens/You Lose.png")
                        screen.blit(imp, (0, 0))
                        pygame.display.flip()
                    elif player == "Paper" and game == "Rock":
                        imp = pygame.image.load("End Screens/You Win.png")
                        screen.blit(imp, (0, 0))
                        pygame.display.flip()
                    elif player == "Scissors" and game == "Rock":
                        imp = pygame.image.load("End Screens/You Lose.png")
                        screen.blit(imp, (0, 0))
                        pygame.display.flip()
                    elif player == "Scissors" and game == "Paper":
                        imp = pygame.image.load("End Screens/You Win.png")
                        screen.blit(imp, (0, 0))
                        pygame.display.flip()
