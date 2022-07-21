import requests

zoo_animals = requests.get('https://zoo-animal-api.herokuapp.com/animals/rand')

print(zoo_animals.json())

