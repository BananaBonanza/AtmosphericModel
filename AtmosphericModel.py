# Atmospheric model created using the NASA equation found at:
# https://www.grc.nasa.gov/WWW/k-12/airplane/atmosmet.html
class atmosphere:
    def __init__(self, val, valGiven = 0,units = "SI"):
        #Convert from US to SI
        if units != "SI" and valGiven == 0:
            val = val / 3.281
        if units != "SI" and valGiven == 1:
            val = val * 0.04788
        #0 implies the given value is an altitude
        #1 implies the given value is a pressure
        if valGiven == 0:
            self.h = val
            self.hCalc()
        elif valGiven == 1:
            self.P = val
            self.PCalc()
        else:
            print("Not a valid 'valGiven' parameter.")
    def hCalc(self):
        if self.h < 11000:
            self.T = 15.04 - 0.00649*self.h
            self.P = 101.29 * ((self.T + 273.1)/288.08)**(5.256)
        elif self.h < 25000:
            self.T = -56.46
            self.P = 22.65 * np.exp(1.73 - 0.000157*self.h)
        elif self.h > 24999:
            self.T = -131.21 + 0.00299*self.h
            self.P = 2.488 * ((self.T + 273.1)/216.6)**(-11.388)
        self.rho = self.P / (0.2869 * (self.T + 273.1))
    def PCalc(self):
        if self.P > 22.632:
            self.T = (288.08*(self.P/101.29)**(1/5.256))-273.1
            self.h = (self.T - 15.04)/(-0.00649)
        elif self.P > 0.1113586:
            self.T = -56.46
            self.h = (1.73 - np.log((self.P/22.65)))/(0.000157)
        else:
            self.T = (216.6*(self.P/2.488)**(1/(-11.388)))-273.1
            self.h = (self.T + 131.21)/0.00299
        self.rho = self.P / (0.2869 * (self.T + 273.1))

def help():
    print("This model determines Pressure and Temperature from height or "+
          "\n Temperature and Height from Pressure. The input is as follows:")
    print("\natmos(value of variable, which variable is given)")
    print("\nFor an input of height, input '0' as the second term. For an"+
          "\n input of pressure, input '1' as the second term.")
    print("\nThe inputs and outputs are in SI units. So Pressure is in kPa,"+
          "\n the temperature is in K, and heights are in meters")
    print("\nBecause this is a class and not a function, you will need to"+
          "\n a variable as this term and the outputs are either '.P', '.T'"+
          "\n or '.h'. A full example can be found in the package file.")
    print("\n-----------------------------------\n")
