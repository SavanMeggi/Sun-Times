class SingleParameterModel:

    def __init__(self, single_lat):
        self.result = single_lat['results']
        self.sunrise = self.result['sunrise']
        self.sunset = self.result['sunset']
        self.day_length = self.result['day_length']


