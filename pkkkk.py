
class vehicle:
    def __init__(self,name,ml,c):
        self.name=name
        self.mileage=ml
        self.capacity=c

    def fare(self):
        print(self.capacity*100)

