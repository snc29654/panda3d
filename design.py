"""01_03_showbase.py"""
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *


class App(ShowBase):
    # コンストラクタ
    def __init__(self):
        # ShowBaseを継承する
        ShowBase.__init__(self)

        self.x = 5
        self.y = 0
        self.z = 10
        # ウインドウの設定
        self.properties = WindowProperties()
        self.properties.setTitle('Showbase sample')
        self.properties.setSize(1200, 800)
        self.win.requestProperties(self.properties)
        self.setBackgroundColor(0, 0, 0)

        # マウス操作を禁止
        self.disableMouse()
        # カメラの設定
        self.camera.setPos(self.x, self.y, self.z)
        self.camera.lookAt(0, 10, 0)

        # ブロックを一つ置く
        self.cube = self.loader.loadModel('models/misc/rgbCube')
        self.cube.setPos(0, 10, 0)
        self.cube.reparentTo(self.render)
        self.accept( "a", self.a_key )    
        self.accept( "b", self.b_key )    
        self.accept( "c", self.c_key )    
        self.accept( "d", self.d_key )    
        self.accept( "e", self.e_key )    
        self.accept( "f", self.f_key )    
 
    def a_key(self): 
        self.x += 1
        self.camera.setPos(self.x, self.y, self.z)
    def b_key(self): 
        self.x -= 1
        self.camera.setPos(self.x, self.y, self.z)
    def c_key(self): 
        self.y += 1
        self.camera.setPos(self.x, self.y, self.z)
    def d_key(self): 
        self.y -= 1
        self.camera.setPos(self.x, self.y, self.z)
    def e_key(self): 
        self.z += 1
        self.camera.setPos(self.x, self.y, self.z)
    def f_key(self): 
        self.z -= 1
        self.camera.setPos(self.x, self.y, self.z)

app = App()
app.run()