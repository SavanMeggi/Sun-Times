class SingleModel:

    def __init__(self, single_animal):
        self.name = single_animal['name']
        self.result = single_animal['result']
        self.animal_type = self.result['animal_type']
        self.lifespan = self.result['lifespan']
        self.habitat = self.result['habitat']
        self.diet = self.result['diet']
        self.image = self.result['image_link']

