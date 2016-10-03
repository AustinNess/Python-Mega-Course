def farenheitToCelsius(farenheitDegrees):
    return (farenheitDegrees-32)*(5/9)

def celsiusToFarenheit(celsiusDegrees):
    fDegrees = (celsiusDegrees)*(9/5) + 32
    return fDegrees if fDegrees > -273.15 else "temp is not possible, too low"


temp1 = 70
temp2 = -500
print("{0} degrees F = {1} degrees C".format(temp1,farenheitToCelsius(temp1)))
print("{0} degrees F = {1} degrees C".format(temp2,celsiusToFarenheit(temp2)))
