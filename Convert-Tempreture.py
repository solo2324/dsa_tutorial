class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:

        Kelvin=celsius + 273.15
        fahrenheit= celsius * 1.80 + 32.00
        a = [Kelvin,fahrenheit]
        return a
