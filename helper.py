#######################################################################
###     This script is used as my goto-file for dataanalysis        ###
###     during the pap2 at Uni Heidelberg. Mostly reused functions  ###
###     for preventing redundance.                                  ###
###                                                                 ###
###     By:     Patrick Nisble                                      ###
###     Ver:    1                                                   ###
###     PyVer:  2.3+ / 3.3+                                         ###
#######################################################################

# todos

# imports
import numpy as _np
import matplotlib.pyplot as _plt
import matplotlib.mlab as _mlab
%matplotlib inline

# definitions

# load complete data from file, skip defines the number of skipped rows
def load_data(filename,skip=0):

    # import pylab inside the function so that it doesn't appear as a function for the module
    import pylab as py

    filename = str(filename)
    # returns every items in the data array as a list of items
    return [i for i in py.loadtxt(filename, unpack=True, skiprows=skip)]


# fitting curves to a linear function
def fit_lin():
     from scipy.optimize import curve_fit
     x = np.array(x)
     y = np.array(y)

     lin_func = lambda x,k,d: k * x + d
     popt, pcov = curve_fit(lin_func, x, y, sigma=sigma)
     fitted_y = popt[0]*x + popt[1]

     return fitted_y, popt, pcov

# fitting curves to polynomial functions
def fit_poly(x, y, deg=1, extrapolate=[]):

    # import numpy inside the function so it doesn't appear as a function for the module
    import numpy as np

    x = np.array(x)
    y = np.array(y)

    # p is an array of the polynomial coefficients
    p = np.polyfit(x, y, deg = deg)

    # get the desired function
    fitted_curve = np.poly1d(p)

    # use extrapolate values if given
    if(len(extrapolate)): x = np.array(extrapolate)

    return fitted_curve(x), p


# return formatted string for presenting results
def printResult(name,value,error):
    print("{0}: {1} +/- {2}".format(name,value,error))
