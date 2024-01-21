class Cerchio:
    def __init__(self,raggio):
        self.raggio=raggio
    def area(self):
        area=(self.raggio**2)*3.14
        print(area)
    def circonferenza(self):
        circonferenza=2*self.raggio*3.14
        print(circonferenza)
raggio1=Cerchio(5)
raggio1.area()
raggio1.circonferenza()