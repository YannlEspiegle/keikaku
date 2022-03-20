import pygame
from constants import WINLONG, WINHAUT, WHITE
from grid import Grid

pygame.init()

screen = pygame.display.set_mode((WINLONG, WINHAUT))
pygame.display.set_caption("Jeu du Keikaku")

g = Grid()

def draw(scr):
    scr.fill(WHITE)
    g.draw(scr)
    pygame.display.update()

def main():
    while True:
        draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                g.click(x, y)

if __name__ == '__main__':
    main()
