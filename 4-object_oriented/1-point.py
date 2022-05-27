class Point:
    def draw(self):
        self.x=10
        print("Draw")


# ------------------------------------

p=Point()
p.draw()
print(p.x)

print(type(p))

i=10

print(isinstance(i,int))
print(isinstance(i,Point))
print(isinstance(p,Point))