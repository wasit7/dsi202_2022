class Rectangle(object):
    def __init__(self, w=0,h=0):
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
    def __repr__(self):
        return "w:%s, h:%s, area:%s"%(self.w,self.h,self.area())
class Square(Rectangle):
    def __init__(self,w=0,h=0):
        self.w=w
        self.h=w
def factory(kind="S",**kwargs):
    box={
        "S":Square,
        "R":Rectangle,
    }
    return box[kind](**kwargs)
print(Square(2))
print(Rectangle(3,5))
print(factory("R",w=5,h=7))
#spec=[{'kind':'R','w':1,'h':2},{'kind':'S','w':7,'h':0}]
#x = [m.factory(i['kind'],w=i['w'],h=i['h']) for i in spec]