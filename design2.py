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
        self.state=0
        self.taskMgr.add(self.MoveTest1, "MoveTest")

        self.cube2 = self.loader.loadModel("models/misc/rgbCube")
        self.cube2.reparentTo(self.render)
        self.cube2.setScale(1, 1, 1)
        self.cube2.setPos(0, 20, 0)
        self.cube2.setQuat( Quat( 0, 1, 1, 1 ) )
        self.x1=0
        self.y1=20
        self.z1=1
        self.state1=0
        self.taskMgr.add(self.MoveTest2, "MoveTest2")


    def MoveTest1(self, task):
        
        if(self.state==0):
            self.x+=0.2
            self.y+=1
            self.z+=0.2
            if(self.x>10):
                self.state=1
        if(self.state==1):
            self.x-=0.2
            self.y-=1
            self.z-=0.2
            if(self.x<0.1):
                self.state=0



        self.cube.setPos(self.x, self.y, self.z)
        return Task.cont
    def MoveTest2(self, task):
        
        if(self.state1==0):
            self.x1+=0.1
            self.y1+=1
            self.z1+=0.1
            if(self.x1>10):
                self.state1=1
        if(self.state1==1):
            self.x1-=0.1
            self.y1-=1
            self.z1-=0.1
            if(self.x1<0.1):
                self.state1=0



        self.cube2.setPos(self.x1, self.y1, self.z1)
        return Task.cont
  
app = MoveCube()
app.run()