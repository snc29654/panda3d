from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import Loader
from panda3d.core import Quat
from direct.task import Task
 
class MoveCube(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)
        self.cube = self.loader.loadModel("models/misc/rgbCube")
        self.cube.reparentTo(self.render)
        self.cube.setScale(1, 1, 1)
        self.cube.setPos(0, 20, 0)
        self.cube.setQuat( Quat( 0, 1, 1, 1 ) )
        self.x=0
        self.y=20
        self.z=1
        self.taskMgr.add(self.MoveTest1, "MoveTest")

    def MoveTest1(self, task):
        self.x+=0.2
        self.y+=1
        self.z+=0.2
        self.cube.setPos(self.x, self.y, self.z)
        return Task.cont
  
app = MoveCube()
app.run()