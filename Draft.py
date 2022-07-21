import requests

zoo_animals = requests.get('https://zoo-animal-api.herokuapp.com/animals')

print(zoo_animals.json()) #

