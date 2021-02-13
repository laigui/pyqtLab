# -*- coding: utf-8 -*-
"""
A brief description of the function.

Created on Tue Sep 22 19:49:09 2020

@author: mikeqin
"""

# ============================================================================
#% Imports
# ============================================================================
import numpy as np


# ============================================================================
#%% Functions
# ============================================================================
def get_08h2028_torque(spd):
    """
    Get max torque of 08h2028 per datasheet.

    Parameters
    ----------
    spd : float
        Motor speed in rpm.

    Returns
    -------
    torq: float
        Motor torque in N*m.

    """
    torq = -4e-15 * spd**4 + 6e-12*spd**3 + 3e-9*spd**2 - 1e-5*spd + 0.0157
    
    return torq

def get_motor_current(vph, ke, spd, rm, lm):
    """

    :param vph:
    :param ke:
    :param spd:
    :param rm:
    :param lm:
    :return:
    """
    iph = (vph - ke*spd/4) / np.sqrt(rm**2 + (2*np.pi*spd/4)**2 * lm**2)
    return iph

def get_motor_max_current(vbus, ke, spd, rm, lm):
    """

    :param vbus:
    :param ke:
    :param spd:
    :param rm:
    :param lm:
    :return:
    """
    iph_max = (vbus - ke*spd/4) / np.sqrt(rm**2 + (2*np.pi*spd/4)**2 * lm**2)
    return iph_max

def get_op_pulses(feed, pitch, theta):
    return feed/pitch*360/theta

def get_pos_period(feed, theta_m, X):
    s, p = X
    pulses = get_op_pulses(feed, p, theta_m)
    return pulses/(s*0.75)

def get_screw_inertia(rho, length, diameter):
    return np.pi/32*rho*length*0.001*(diameter*0.001)**4

def get_acc_torque(feed, rho, length, diameter, J0, theta_m, X):
    s, p = X
    JL = get_screw_inertia(rho, length, diameter)
    pulses = get_op_pulses(feed, p, theta_m)
    return (J0 + JL) * np.pi * theta_m/180 * (s/pulses)
    
def get_req_torque(feed, rho, length, J0, theta_m, mass, mu, diameter, eff, sf, X):
    s, p = X
    F = mass * 9.807 * (np.sin(90*np.pi/180) - mu*np.cos(90*np.pi/180))
    TL = F*diameter/2*(p+mu*np.pi*diameter)/(np.pi*diameter-mu*p)*0.001/eff
    Ta = get_acc_torque(feed, rho, length, diameter, J0, theta_m, X)
    return (TL+Ta)*sf

def get_max_current(X, Vbus, Ke, Rm, Lm):
    s, p = X
    return get_motor_max_current(Vbus, Ke, s, Rm, Lm)