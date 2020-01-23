from AtmosphericModel import AtmosphericModel as am

am.help()

#A class where the input is an altitude
atmosHeight = am.atmosphere(5000,0)

print("atmospheric model outputs for altitude=5000m input\n--------------------")
print("This is the pressure in kPa:")
print(atmosHeight.P)

print("This is the temperature in C:")
print(atmosHeight.T)

#A class where the input is a pressure
atmosPress = am.atmosphere(45,1)

print("\natmospheric model outputs for pressure=45kPa input\n--------------------")
print("This is the height in meters:")
print(atmosPress.h)

print("This is the temerature in C:")
print(atmosPress.T)
