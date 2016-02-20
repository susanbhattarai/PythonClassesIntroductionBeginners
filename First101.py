class Country(object):
	def __init__(self, name, capital):
		self.name = name
		self.capital = capital

	def __str__(self):
		sentence = 'The capital of ' + self.name + ' is ' + self.capital
		return sentence


my_country = Country('Nepal', 'Kathmandu')
print my_country
