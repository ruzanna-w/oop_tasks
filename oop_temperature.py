class Temperature:
    def __init__(self, celsius):
        if celsius < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, temperature):
        if temperature < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        else:
            self._celsius = temperature
    
    @property 
    def fahrenheit(self):
        F = (self._celsius * 9 / 5) + 32
        return F

temp = Temperature(300)

print(temp.celsius)
print(temp.fahrenheit)