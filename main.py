import pygame
import random
from pygame import MOUSEBUTTONDOWN

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
                print(x)
                print(y)
                while True:
                    if 0 <= x <= 200 and 200 <= y <= 400:
                        player = "Rock"
                        break
                    elif 200 <= x <= 400 and 200 <= y <= 400:
                        player = "Paper"
                        break
                    elif 400 <= x <= 600 and 200 <= y <= 400:
                        player = "Scissors"
                        break
                    else:
                        continue
                game = random.randint(0,2)

                if game == 0:
                    game = "Rock"
                elif game == 1:
                    game = "Paper"
                elif game == 2:
                    game = "Scissors"
                if player == game:
                    print("TIE!")
                elif player == "Rock" and game == "Scissors":
                    print("You Win!")
                elif player == "Rock" and game == "Paper":
                    print("You Lose!")
                elif player == "Paper" and game == "Scissors":
                    print("You Lose!")
                elif player == "Paper" and game == "Rock":
                    print("You Win!")
                elif player == "Scissors" and game == "Rock":
                    print("You Lose!")
                elif player == "Scissors" and game == "Paper":
                    print("You Win!")
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