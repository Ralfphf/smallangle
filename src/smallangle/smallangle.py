import click
import numpy as np
from numpy import pi
import pandas as pd

#Creates a click group for the main commando
@click.group()
def calculation_group():
    pass

#Sub-commando for the function sin with NUMBER as options
@calculation_group.command()
@click.option("-n", "--number", default = 10) 

#calculates the sin(x) with x between 0 and 2pi in steps given by the option NUMBER
def sin(number):
    """calculate sin(x) for 0 < x < 2pi in NUMBER steps

    NUMBER is the amount of even steps taken between 0 and 2pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


#Sub-commando for the function tan with NUMBER as options
@calculation_group.command()
@click.option("-n", "--number", default = 10)

#calculates the sin(x) with x between 0 and 2pi in steps given by the option NUMBER
def tan(number):
    """calculate tan(x) for 0 < x < 2pi in NUMBER steps

    NUMBER is the amount of even steps taken between 0 and 2pi
    """ 
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

#If the function 'calculation_group' gets used in another file, this script will not be run
if __name__ == "__main__":
    calculation_group()