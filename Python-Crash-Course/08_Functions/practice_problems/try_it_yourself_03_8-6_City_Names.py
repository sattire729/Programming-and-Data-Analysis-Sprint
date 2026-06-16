# 8-6 City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    string = f"{city}, {country}"
    return string.title()

c_c = city_country('santiago', 'Chile')
print(c_c)
c_c = city_country('Paris', 'france')
print(c_c)
c_c = city_country('beijing', 'china')
print(c_c)