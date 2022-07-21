from single_animal_model import SingleModel
import requests

class SingleAnimal():

    def __init__(self, SingleAnimal):
        self.URL = "https://zoo-animal-api.herokuapp.com/animals/" + SingleAnimal
        #self.request = requests.get(self.URL)
        #self.resp_json = self.request.json()

    def respond_data(self):
        return SingleModel(self.URL)

