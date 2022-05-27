from turtle import pen


class Product:
    def __init__(self,name,price):
        self.name=name
        self.set_price(price)

    def set_price(self,value):
        print("Set Price Invoked")
        if(value<=0):
            raise Exception("Price cannot be 0 or less")
        else:
            self.__price=value
    
    def get_price(self):
        print("Get Price Invoked")
        return self.__price
    
    def __str__(self):
        return f"Product Name:{self.name} | Price: {self.__price}"

    price=property(get_price,set_price)
# -----------------------------------------------------

try:
    p1=Product("Earphones",500)
    print(p1)

    p2=Product("Keyboard",-800)
    print(p2)
    p2.price=-980
    print(p2.price)
except Exception as ex:
    print(ex)