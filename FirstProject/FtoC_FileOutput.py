temperatures=[10,-20,-289,100]

from FahrenheitToCelsius import celsiusToFarenheit;

with open('C:/Users/austin.ness/PersonalProjects/Python-Mega-Course/FirstProject/FtoC_output.txt', 'a+') as file:
    for t in temperatures:
        #print(t)
        fahr=celsiusToFarenheit(t)
        #print(far)
        if(isinstance(fahr, float)):
            file.write(str(fahr)+"\n")
