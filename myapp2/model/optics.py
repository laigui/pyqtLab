# -*- coding: utf-8 -*-
"""
Optics model functions.

Created on Sat Nov 14 20:13:28 2020

@author: mikeqin

References:
    [1] V. Lakshminarayanan, H. Ghalila, A. Ammar, and L. S. Varadharajan, Understanding optics with Python. CRC Press, 2017.
    [2] K. D. Moeller, Optics, 2nd ed. Springer, 2007.
"""

# ============================================================================
#%% Imports
# ============================================================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize


# ============================================================================
#%% Constants
# ============================================================================
# Conversion factors from non-SI to SI
_wl_units = {'angstrom': 1e-10, 'nm': 1e-9, 'um': 1e-6, 'm': 1.0}
_wn_units = {'nm': 1e9, 'um': 1e6, 'cm': 1e3, 'm': 1.0, 'angm': 1./(2.*np.pi)}
_f_units = {'Hz': 1.0, 'kHz': 1e3, 'MHz': 1e6, 'GHz': 1e9, 'THz': 1e12}


# ============================================================================
#%% Functions
# ============================================================================
def _units_err_msg(measure):
    """
    Return a string with an error message appropriate to whichever
    units were incorrect.
    
    """
    if measure == 'wl':
        units = _wl_units
        name = "Wavelength"
    elif measure == 'f':
        units = _f_units
        name = "Frequency"
    elif measure == 'wn':
        units = _wn_units
        name = "Wavenumber"
    return name + "must be one of: " + str(units.keys())


def wavelength_to_wavenum(wl, wl_units="nm", wn_units="nm"):
    """
    Convert a wavelength to wavenumber.

    Parameters
    ----------
    wl : float
        Wavelength.
    wl_units : str, optional
        Units the wavelength is given in. The default is "nm".
    wn_units : str, optional
        Units for the returned wavenumber value. The default is "cm".

    Returns
    -------
    wn : float
        The wavenumber corresponding to the given wavelength.

    """
    try:
        wl_SI = wl * _wl_units[wl_units]
    except KeyError:
        raise ValueError(_units_err_msg('wl'))
    wn_SI = 1 / wl_SI
    try:
        wn = wn_SI / _wn_units[wn_units]
    except KeyError:
        raise ValueError(_units_err_msg('wl'))        
    return wn


def calc_amplitude_grating_intensities(lamda, a, b, f_2, N, x):
    """
    Calculate the intensities of an amplitude grating composed of a large 
    number of slits (N slits per mm) each with a width b and separated from 
    its neighbouring slit by a distance a from center-to-center.

    Parameters
    ----------
    lamda : float
        Wavelength (m).
    a : float
        Distance between the centers of the slits (m).
    b : float
        Dimensions of diffracting slit (m).
    f_2 : float
        Focal length of the lens L2 (m).
    N : integer
        Number of slits per mm.
    x : float
        X coordinates of screen.

    Returns
    -------
    I : float
        Intensity of the grating.
        
    References
    ----------
    [1] V. Lakshminarayanan, H. Ghalila, A. Ammar, and L. S. Varadharajan, Understanding optics with Python. CRC Press, 2017.

    """
    k = wavelength_to_wavenum(lamda, 'm', 'angm')  
    A = (k * a) / (2. * f_2)  
    B = (k * b) / (2. * f_2)
    
    # 1D representation
    I = (1 / N**2) * ((np.sin(B*x) / (B*x) )**2) * (np.sin(N*A*x) / np.sin(A*x))**2
    return I
