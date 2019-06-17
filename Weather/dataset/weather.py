from mrjob.job import MRJob

class MRWeather(MRJob):
    def MakeFahrenheit(self, tethsOfCelsius):
        celsius = float(tethsOfCelsius) / 10.0
        fahrenheit = celsius * 1.8 + 32.0
        return fahrenheit
    
    def mapper(self, _, line):
        (location, date, type, data, x, y, z, w) = line.split(',')
        if (type =='TMIN'):
            temperature = self.MakeFahrenheit(data)
            yield location, temperature


if __name__ == '__main__':
    MRWeather.run()