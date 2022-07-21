import requests

Sun_times = requests.get('https://api.sunrise-sunset.org/json?lan=-4.4203400%27')

print(Sun_times.json())