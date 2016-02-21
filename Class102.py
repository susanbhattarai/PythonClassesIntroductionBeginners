class Car(object):
    def __init__(self, model, mileage, man_date, cost):
        self.__model = model
        self.mileage = mileage
        self.man_date = man_date
        self.cost = cost


    def is_older(self):
        if self.man_date  < 1990:
            return "The car is old"
        else:
            return "Car is great"
    def is_expensive(self):
        if self.cost > 25000:
            return "Too expensive"
        else:
            return "Car is cheap" 

    def is_mileage(self):
        if self.mileage > 25:
            return "Great"
        else:
            return "Bad"


// Inheritance Concepts
class BugatiCar(Car):
    def __init__(self, model, mileage, man_date, cost, rating):
        Car.__init__(self, model, mileage, man_date, cost)
        self.rating = rating
    def is_expensive(self):
        if self.cost >  75000:
            return "Expensive bugati car"
        else:
            return "Cheap Bugati Car"





        
