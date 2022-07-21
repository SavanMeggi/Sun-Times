class SingleParameterModel:

    def __init__(self, single):
        self.result = single['result']
        self.sunrise = self.result['sunrise']
        self.sunset = self.result['sunset']
        self.day_length = self.result['day_length']



