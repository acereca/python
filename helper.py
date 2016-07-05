#######################################################################
###     This script is used as my goto-file for dataanalysis        ###
###     during the pap2 at Uni Heidelberg. Mostly reused functions  ###
###     for preventing redundance.                                  ###
###                                                                 ###
###     By:     Patrick Nisble                                      ###
###     Ver:    5                                                   ###
###     PyVer:  2.3+ / 3.3+                                         ###
#######################################################################

# todos

# imports
import numpy as _np
import matplotlib.pyplot as _plt
import matplotlib.mlab as _mlab

# definitions


# fitting curves to a linear function
def fit_lin(x,y,sigma=None,zero=False):
     from scipy.optimize import curve_fit
     x = _np.array(x)
     y = _np.array(y)

     lin_func = lambda x,k,d: k * x + d

     if zero is True:
         lin_func = lambda x,k,d: k * x

     popt, pcov = curve_fit(lin_func, x, y, sigma=sigma)
     fitted_y = popt[0]*x + popt[1]

     return fitted_y, popt, pcov

# fitting curves to polynomial functions
def fit_poly(x, y, deg=1, extrapolate=[]):

    x = _np.array(x)
    y = _np.array(y)

    # p is an array of the polynomial coefficients
    p = _np.polyfit(x, y, deg = deg)

    # get the desired function
    fitted_curve = _np.poly1d(p)

    # use extrapolate values if given
    if(len(extrapolate)): x = _np.array(extrapolate)

    return fitted_curve(x), p

# return formatted string for presenting results
def printResult(name, value, error=0, unit=None, decimal = 5):
    from IPython.display import display, Math, Latex

    if error != 0:
        out = "%s \pm %s"%(round(value,decimal),round(error,decimal))
        if unit:
            out = '(' + out + ')' + unit
    else:
        out = str(round(value,decimal))
        if unit:
            out = out + unit

    display(Math(name + "=" + out))

def relErr(dlist,alist):
    return _np.sqrt(_np.sum((_np.array(dlist)/_np.array(alist))**2))
