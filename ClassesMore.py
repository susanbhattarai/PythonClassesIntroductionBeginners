class Country(object):
    def __init__(self, name, capital_city, population):
        self.name = name
        self.capital_city = capital_city
        self.population = population

    def __str__(self):
        string = 'The capital city of ' + self.name + ' is ' + self.capital_city
        return string

    def bigger(self, other):
        if self.population > other.population:
            b = self.name + ' is bigger than ' + other.name
        else:
            b = other.name + ' is bigger than ' + self.name
        return b

   def __cmp__(self, other):
        return bigger(self, other)

A  = Country("Nepal", "Kathmandu", 2000)
B = Country("India", "Delhi", 100000)
print bigger(A, B) # A.bigger(B) # A > B  # A > B # 
    
