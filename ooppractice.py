
class point:
    def __init__(self,newx=0,newy=0):
        self.x = newx
        self.y = newy
    def movepoint(self,newx,newy):
        self.x = newx
        self.y = newy
    def printpoint(self):
        print("x is ",self.x)
        print("y is ",self.y)
originmain = point()
origin = point(4,4)
mypoint = point(2,3)
mypoint.movepoint(5,5)
mypoint.printpoint()
origin.printpoint()
originmain.printpoint()
del originmain.x
origin.printpoint()