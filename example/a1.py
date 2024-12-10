from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.cube = self.loader.loadModel('models/misc/rgbCube')

        self.cube.setScale(2, 2, 2)

        self.cube.setQuat(Quat(0, 1, 1, 1))

        self.cube.setPos(0, 20, 0)

        self.cube.reparentTo(self.render)

app = App()
app.run()