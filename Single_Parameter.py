import requests

from Single_Parameter_Model import SingleParameterModel

class SingleParameter:

    def __init__(self, lan = '51.500153'):
        self.URL = 'https://api.sunrise-sunset.org/json?' + lan
        self.request = requests.get(self.URL)
        self.resp_json = self.request.json()

    def data_response(self):
        return SingleParameterModel(self.resp_json)

latitude = SingleParameter('lan=51.500153')

print(latitude.data_response())