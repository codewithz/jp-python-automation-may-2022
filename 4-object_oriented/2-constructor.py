class Point:
    def __init__(self,a,b):
        print("Point() invoked")
        self.x=a
        self.y=b
        self.z=self.x+self.y
    
    def draw(self):
        print(f"Point({self.x},{self.y})")
        self.x=40
        self.y=50
    
    def __str__(self):
        return f"Point({self.x},{self.y},{self.z})"


# ------------------------------------------------------

p=Point(23,25)
print(p)
p.draw()
print(p)