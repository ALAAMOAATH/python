class car:
    def __init__(self,color,model,price):
        self.car_color=color
        self.car_model=model
        self.car_price=price
    def myCar(self):
        if self.car_model>=2018:
            self.car_price+=100
            print(self.car_price)
        else:
            self.car_price-=30
            print(self.car_price)



