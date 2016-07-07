#######################################################################
###     This script is used as my goto-file for dataanalysis        ###
###     during the pap2 at Uni Heidelberg. Mostly reused functions  ###
###     for preventing redundance.                                  ###
###                                                                 ###
###     By:     Patrick Nisble                                      ###
###     Ver:    5                                                   ###
###     PyVer:  2.3+ / 3.3+                                         ###
###     prereqs:numpy, matplotlib, uncertainties, scipy             ###
#######################################################################

# todos

# imports
import numpy as _np
import matplotlib.pyplot as _plt
import matplotlib.mlab as _mlab
import uncertainties as unc

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
    '''return mathjax-html for jupyter notebook of formatted value, error and unit'''
    
    # import necessary libs for mathjax-html output
    from IPython.display import display, Math, Latex

    # test for use of uncertainties lib
    if isinstance(value, unc.UFloat):
        error = value.s
        value = value.n

    # print \pm err or not
    if error != 0:
        out = "%s \pm %s"%(round(value,decimal),round(error,decimal))
        if unit:
            out = '(' + out + ')' + unit
    else:
        out = str(round(value,decimal))
        if unit:
            out = out + unit

    # display call to print in jupyter notebook
    display(Math(name + "=" + out))
