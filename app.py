import web
import Pool_module as PM
from json import loads
import threading

def simul():
    import pygame
    from math import floor, ceil
    import Pool_module as PM

    def mappit(X, A, B, C, D):
        return floor((X-A)/(B-A) * (D-C) + C)

    pygame.init()

    n_linhas = 10
    n_cols = 10

    screen_size = (width, height) = 360, 640
    FPS = 60
    run = True

    myPool = PM.Pool(width = width, height = height)
    myRobot = PM.Robo()

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

        for l in range(len(myPool.tiles)):
            for c in range(len(myPool.tiles[l])):
                b = mappit(myPool.tiles[l][c], 0, 1, 0, 255)
                r = 255 - b
                pygame.draw.rect(screen, (r, 0, b), (c*r_width, l*r_height, r_width, r_height))
        pygame.draw.rect(screen, (255, 255, 255), (myRobot.x-5, myRobot.y-5, 10, 10))
        myRobot.update(myPool)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

urls = (
    '/robot', 'Robot',
    '/receber', 'Receive'
)

simul_thread = threading.Thread(target = simul)

myPool = PM.Pool(width = 360, height = 640)
myRobot = PM.Robo()

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


class Robot:
    def GET(self):
        global myRobot
        myRobot.update(myPool)
        web.header('Content-Type', 'application/json')
        return myRobot.report(myPool)

class Receive:
    def POST(self):
        response_json = web.data()
        print(response_json)
        print(str(response_json))
        text = response_json.decode("utf-8")
        print(text)
        print(type(text))
        '''data = loads(text)
        value = data["name"]
        return 'Hello ' + value'''

if __name__ == '__main__':
    app = MyApplication(urls, globals())
    simul_thread.start()
    app.run(8060)
