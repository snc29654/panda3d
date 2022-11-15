from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import Loader
from panda3d.core import Quat
from direct.task import Task
import random
 
class MoveCube(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)
        self.cubet=[0,1,2,3,4,5,6,7,8,9]

        for i in range(10):
            self.cubet[i] = self.loader.loadModel("models/misc/rgbCube")
            self.cubet[i].reparentTo(self.render)
            self.cubet[i].setScale(1, 1, 1)
            self.cubet[i].setPos(0, 20, 0)
            self.cubet[i].setQuat( Quat( 0, 1, 1, 1 ) )


        self.x=0
        self.y=20
        self.z=1
        self.state=0
        self.taskMgr.add(self.MoveTest1, "MoveTest")



    def MoveTest1(self, task):

        for i in range(10):
            self.cubet[i].setPos(self.x+random.uniform(-5,5), self.y+random.uniform(-5,5), self.z+random.uniform(-5,5))
        return Task.cont

app = MoveCube()
app.run()