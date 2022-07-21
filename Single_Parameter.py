import requests
import json
class SingleParameter:

    def __init__(self):
        self.URL = 'https://api.sunrise-sunset.org/json?lan=-4.4203400'
        self.request = requests.get(self.URL)
        self.resp_json = self.request.json

    def data_response(self):
        return SingleParameterModel(self.resp_json)
