import web
import Pool_module as PM

urls = (
    '/robot', 'Robot'
)

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


if __name__ == '__main__':
    app = MyApplication(urls, globals())
    app.run(8060)
