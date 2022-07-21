import requests

from Single_Parameter_Model import SingleParameterModel


class SingleParameter:

    def __init__(self, lat = 'lat=51.500153', lng = '&lng=-0.1262362'):     #Defualt London
        self.URL = 'https://api.sunrise-sunset.org/json?' + lat + lng
        self.request = requests.get(self.URL)
        self.resp_json = self.request.json()

    def data_response(self):
        return SingleParameterModel(self.resp_json)



