import pygame
from math import floor, ceil
import Pool_module as PM
from opensimplex import OpenSimplex

def mappit(X, A, B, C, D):
    return floor((X-A)/(B-A) * (D-C) + C)

pygame.init()

noise = OpenSimplex()

n_linhas = 10
n_cols = 10

screen_size = (width, height) = 360, 640
FPS = 60
run = True

matrix = [[0 for x in range(n_cols)] for y in range(n_linhas)]
zoff = 0
loff = 0

for linha in range(n_linhas):
	coff = 0
	for coluna in range(n_cols):
		matrix[linha][coluna] = noise.noise3d(x = coff, y = loff, z = zoff)
		coff += 0.2
	loff += 0.2

r_width = ceil(width/n_cols)
r_height = ceil(height/n_linhas)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Yo")

while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    screen.fill((0, 0, 0))
    zoff += 0.02
    loff = 0
    for linha in range(len(matrix)):
    	coff = 0
    	for coluna in range(len(matrix[linha])):
    		matrix[linha][coluna] = noise.noise3d(x = coff, y = loff, z = zoff)
    		coff += 0.2
    	loff += 0.2

    for linha in range(len(matrix)):
    	for coluna in range(len(matrix[linha])):
    		b = mappit(matrix[linha][coluna], -1, 1, 0, 255)
    		r = 255 - b
    		pygame.draw.rect(screen, (r, 0, b), (coluna*r_width, linha*r_height, r_width, r_height))

    #pygame.draw.rect(screen, (255, 255, 255), (myRobot.x-5, myRobot.y-5, 10, 10))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()