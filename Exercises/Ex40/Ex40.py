#Exercise 40: Dictionaries, Oh Lovely Dictionaries

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."

cities['_find'] = find_city

while True:
	print "State? (ENTER to quit",
	state = raw_input("> ")

	if not state: break

	city_found = cities['_find'](cities, state)
	print city_found
	
