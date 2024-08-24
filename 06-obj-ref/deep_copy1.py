import copy

class HantedBus:
	def __init__(self, passengers=[]):
		self.passengers = passengers

	def pick(self, name):
		self.passengers.append(name)

	def drop(self, name):
		self.passengers.remove(name)


bus1 = HantedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)

bus2 = HantedBus()
bus2.pick('Carrie')
print(bus2.passengers)

bus3 = HantedBus()
print(bus3.passengers)
bus3.pick('Dave')
print(bus2.passengers)

print(bus2.passengers is bus3.passengers)
print(bus1.passengers)

print(dir(HantedBus.__init__))
print(HantedBus.__init__.__defaults__)
print(HantedBus.__init__.__defaults__[0] is bus2.passengers)
