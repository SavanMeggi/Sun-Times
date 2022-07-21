from single_parameter import SingleParameter

user_latitude = input('Input a float value of a latitude of your choice on earth here ...\n')
user_longitude = input('Input a float value of a longitude of your choice on earth here ...\n')
Latitude = SingleParameter('lan' + user_latitude, '&lng=' + user_longitude)




print(Latitude)
print('Sunrise is at:')
print(Latitude.data_response().sunrise)
print('Sunset is at:')
print(Latitude.data_response().sunset)
print('The length of the day in hh/mm/ss is:')
print(Latitude.data_response().day_length)