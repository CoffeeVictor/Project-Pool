from random import random, uniform
from math import floor
from json import dumps


class Pool:
    def __init__(self):
        self.n_linhas = 10
        self.n_cols = 10
        self.tile_l = 100/self.n_cols
        self.tile_a = 100/self.n_linhas
        self.tiles = [[random() for _ in range(self.n_cols)] for a in range(self.n_linhas)]

class Robo:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.spd = 0.4
        self.tgX = 0
        self.tgY = 0

    def update(self):
        if self.x == self.tgX and self.y == self.tgY:
            self.tgX = uniform(0, 100)
            self.tgY = uniform(0, 100)

        if self.x < self.tgX:
            self.x += self.spd
        if self.x > self.tgX:
            self.x -= self.spd
        if self.y < self.tgY:
            self.y += self.spd
        if self.y > self.tgY:
            self.y -= self.spd

    def report(self, Pool):
        searchX = floor(self.x/Pool.tile_l)
        searchY = floor(self.y/Pool.tile_a)
        oxReport = Pool.tiles[searchX][searchY]
        retDict = {
            'robo.x':self.x,
            'robo.y':self.y,
            'tile.x':searchX,
            'tile.y':searchY,
            'oxLevel':oxReport,
        }
        return dumps(retDict, indent=4)