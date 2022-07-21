import requests

from Single_Parameter_Model import SingleParameterModel


class SingleParameter:

    def __init__(self, lat):
        self.URL = 'https://api.sunrise-sunset.org/json?' + lat
        self.request = requests.get(self.URL)
        self.resp_json = self.request.json()
        print(self.resp_json)

    def data_response(self):
        return SingleParameterModel(self.resp_json)


x = SingleParameter('lat=4.4')
print(x.data_response().sunrise)
