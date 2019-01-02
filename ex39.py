# dictionary practice

# maps of states to abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# now a dictionary for cities within some states
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# now adding more to cities dict
cities['OR'] = 'Portland'
cities['NY'] = 'Albany'

# now we print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# now we print out some states
print('-' * 10)
print("Michigan abbreviation is: ", states['Michigan'])
print("Florida abbreviation is: ", states['Florida'])

# now we try embedding
print('-' * 10)
print("Michigan's city is: ", cities[states['Michigan']])
print("Florida's city is: ", cities[states['Florida']])

# now we loop through them all
print('-' * 10)
for state in states:
    print(f"{state}'s abbreviation is: {states[state]}")
    print(f"{state}'s city is: {cities[states[state]]}")

# and we try to see what happens if an entry isn't in the dictionary
print('-' * 10)
state = states.get('Texas') #what does get do? it's specific to dicts
if not state:
    print("Sorry, no Texas")

city = cities.get('TX', 'Does not exist')
print(f"the city for the state 'TX' is: {city}")
