import pygame
from constants import TAILLE_CASE, BLACK, CROIX, ROND, WINHAUT, WINLONG
from assets import IMAGE_CROIX, IMAGE_ROND

TAILLE_MORP = 3 * TAILLE_CASE

class Morpion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fini = False
        self.winner = 0
        self.grille = [[0] * 3 for _ in range(3)]

    # TODO faire une belle fonction
    def check_end(self):
        for i in range(3):
            if self.grille[0][i] == self.grille[1][i] == self.grille[2][i] != 0:
                return True
            if self.grille[i][0] == self.grille[i][1] == self.grille[i][2] != 0:
                return True
        if self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != 0:
            return True
        if self.grille[0][2] == self.grille[1][1] == self.grille[2][0] != 0:
            return True
        return False

    def click(self, x, y, symbole):
        x_pos, y_pos = (x - self.x) // TAILLE_CASE, (y - self.y) // TAILLE_CASE
        if self.grille[y_pos][x_pos] == 0:
            self.grille[y_pos][x_pos] = symbole
            if self.check_end():
                self.fini = True
                self.winner = symbole
            return (x_pos, y_pos)
        return (-1, -1)

    # TODO quand le morpion est gagné, ne montrer que le symbole gagnant
    def draw(self, scr):
        # lignes verticales
        pygame.draw.line(scr, BLACK, (self.x + TAILLE_CASE, self.y), (self.x + TAILLE_CASE, self.y + TAILLE_MORP))
        pygame.draw.line(scr, BLACK, (self.x + 2*TAILLE_CASE, self.y), (self.x + 2*TAILLE_CASE, self.y + TAILLE_MORP))

        # lignes horizontales
        pygame.draw.line(scr, BLACK, (self.x, self.y + TAILLE_CASE), (self.x + TAILLE_MORP, self.y + TAILLE_CASE))
        pygame.draw.line(scr, BLACK, (self.x, self.y + 2*TAILLE_CASE), (self.x + TAILLE_MORP, self.y + 2*TAILLE_CASE))

        image_croix = pygame.transform.scale(IMAGE_CROIX, (TAILLE_CASE,)*2)
        image_rond = pygame.transform.scale(IMAGE_ROND, (TAILLE_CASE,)*2)

        for y in range(3):
            for x in range(3):
                coords = (self.x + x * TAILLE_CASE, self.y + y * TAILLE_CASE)
                if self.grille[y][x] == CROIX:
                    scr.blit(image_croix, coords)
                elif self.grille[y][x] == ROND:
                    scr.blit(image_rond, coords)


class Grid:
    def __init__(self):
        self.morpions = [[Morpion(x*TAILLE_MORP, y*TAILLE_MORP) for x in range(3)] for y in range(3)]
        self.oblige = None
        self.trait = CROIX

    def draw(self, scr):
        pygame.draw.line(scr, BLACK, (0, TAILLE_MORP), (WINHAUT, TAILLE_MORP), 3)
        pygame.draw.line(scr, BLACK, (0, 6*TAILLE_CASE), (WINHAUT, 6*TAILLE_CASE), 3)

        pygame.draw.line(scr, BLACK, (TAILLE_MORP, 0), (TAILLE_MORP, WINLONG), 3)
        pygame.draw.line(scr, BLACK, (2*TAILLE_MORP, 0), (2*TAILLE_MORP, WINLONG), 3)

        for ligne in self.morpions:
            for morpion in ligne:
                morpion.draw(scr)

    def click(self, x, y):
        x_pos, y_pos = x // TAILLE_MORP, y // TAILLE_MORP
        if self.morpions[y_pos][x_pos].fini:
            return

        if self.oblige is None or self.morpions[y_pos][x_pos] == self.oblige:
            x_click, y_click = self.morpions[y_pos][x_pos].click(x, y, self.trait)
            if x_click < 0:
                return

            if not self.morpions[y_click][x_click].fini:
                self.oblige = self.morpions[y_click][x_click]
            else:
                self.oblige = None
            self.trait = CROIX if self.trait == ROND else ROND
