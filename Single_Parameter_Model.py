class SingleParameterModel:

    def __init__(self, single_lan):
        self.result = single_lan['result']
        self.sunrise = self.result['sunrise']
        self.sunset = self.result['sunset']
        self.day_length = self.result['day_length']




