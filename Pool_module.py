from random import random, uniform, randint
from math import floor
from json import dumps


class Pool:
    def __init__(self, width, height):
        self.n_linhas = 10
        self.n_cols = 10
        self.width = width
        self.height = height
        self.tile_l = width/self.n_cols
        self.tile_a = height/self.n_linhas
        self.tiles = [[random() for _ in range(self.n_cols)] for a in range(self.n_linhas)]
    def refresh(self):
        self.tiles = [[random() for _ in range(self.n_cols)] for a in range(self.n_linhas)]

class Robo:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tx = 0
        self.ty = 0
        self.spd = 4
        self.tgX = 0
        self.tgY = 0

    def update(self, Pool):
        self.tx = floor(self.x/Pool.tile_l)
        self.ty = floor(self.y/Pool.tile_a)

        if self.tx == self.tgX and self.ty == self.tgY:
            self.tgX = randint(0, Pool.n_cols)
            self.tgY = randint(0, Pool.n_linhas)
            print('New targets: ', self.tgX, self.tgY)

        if self.tx < self.tgX:
            self.x += self.spd
        if self.tx > self.tgX:
            self.x -= self.spd
        if self.ty < self.tgY:
            self.y += self.spd
        if self.ty > self.tgY:
            self.y -= self.spd

    def report(self, Pool):
        searchX = floor(self.x/Pool.tile_l)
        searchY = floor(self.y/Pool.tile_a)
        oxReport = Pool.tiles[searchX][searchY]
        retDict = {
            'robo_x':self.x,
            'robo_y':self.y,
            'tile_x':searchX,
            'tile_y':searchY,
            'oxLevel':oxReport,
        }
        return dumps(retDict, indent=4)