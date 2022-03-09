# Snake Tutorial Python

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
'''============================================='''

# Classes


class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        


    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake(object):

    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)

        # for these two ones, up means 1, down means -1, stop 0, left, -1, right 1
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0

                    # to save the last position of the snake's head
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # Movement of the snake

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0, turn[1]])
                if i == len(self.body) - 1:
                    self.turns.pop()
        # If the snake reaches the edges of the screen
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])

                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])

                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)

                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[1], c.rows-1)

                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface) 


'''============================================='''

# Functions


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (225, 225, 225), (x, 0), (x, w))
        pygame.draw.line(surface, (225, 225, 225), (0, y), (w, y))


def redrawWindow(surface):
    global rows, width, s 
    s.draw(surface)
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows, s
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))

    s = snake((255, 0, 0), (10, 10))

    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)  # the lower this goes, the faster is gonna be

        clock.tick(10)  # the lower this goes, the slower is gonna be

        redrawWindow(win)

    pass


main()
