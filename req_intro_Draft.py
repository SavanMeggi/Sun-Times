import requests

Sun_times = requests.get('https://api.sunrise-sunset.org/json?lan=-4.4203400')

print(Sun_times.json())

data = Sun_times.json()['results']

print(data['sunrise'])
print(data['sunset'])
print(data['day_length'])