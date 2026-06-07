# 6-11 Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city's dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
cities = {
    'New York': {
        'country': 'United States',
        'population': 8336817,
        'fact': 'The city is known for its iconic skyline and the Statue of Liberty.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'The city is known for its bustling streets and traditional temples.'
    },
    'Paris': {
        'country': 'France',
        'population': 2148327,
        'fact': 'The city is known for its art, fashion, and the Eiffel Tower.'
    }
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']:,}")
    print(f"  Fact: {info['fact']}")