# -*- coding: utf-8 -*-
"""
L6470 motor control functions based on the simplified stepper model.

Created on Mon Sep  7 13:01:26 2020

@author: mike.qin

References:
    [1] E. Poli, “Voltage mode control operation and parameter optimization,” AN4144, 2017.
"""

# ============================================================================
#%% Imports
# ============================================================================
import numpy as np



# ============================================================================
#%% Functions
# ============================================================================
def get_l6470_kval(Rm, Iph, vbus):
    """
    Calculate Kval, which is normalized voltage applied to the phase at
    zero speed in order to obtain the target current value.

    Parameters
    ----------
    Rm : float
        Motor resistance per phase (Ohm).
    Iph : float
        Target peak phase current (A).
    vbus : float
        Bus voltage (V).

    Returns
    -------
    list
        kval: Normalized to the supply voltage (%).
        kval_reg: KVAL register value.

    """
    kval = Rm*Iph/vbus
    kval_reg = kval*256

    return [kval, kval_reg]


def get_l6470_bemf_intersect_spd(Rm, Lm):
    """
    Calculate intersect speed, which is the motor speed discriminating the
    compensation slope that should be used.
    :param Rm: Motor resistance per phase (Ohm)
    :param Lm:
    :return int_spd: step/s
    :return int_spd_reg: step/tick
    """
    int_spd = 4*Rm/(2*np.pi*Lm)
    int_spd_reg = int_spd * 2**26 * 250 * 1e-9

    return [int_spd, int_spd_reg]


def get_l6470_bemf_start_slope(Ke, vbus):
    """
    Calculate start slope.
    :param Ke:
    :param vbus: Bus voltage (V)
    :return st_slope: BEMF compensation start slope normalized to Vbus (%*s/step)
    :return st_slope_reg: BEMF compensation start slope normalized to Vbus, the
    register value 8bit with range 0.4
    """
    st_slope = Ke/4/vbus*100
    st_slope_reg = st_slope/100 * 2**16

    return [st_slope, st_slope_reg]


def get_l6470_bemf_final_slope(Lm, Iph, Ke, vbus):
    """
    Calculate final slope.
    :param Lm:
    :param Iph:
    :param Ke:
    :param vbus: Bus voltage (V)
    :return fn_slope: BEMF compensation final slope normalized to Vbus (%*s/step)
    :return fn_slope_reg: BEMF compensation final slope normalized to Vbus, the
    register value 8bit with range 0.4
    """
    fn_slope = (2*np.pi*Lm*Iph+Ke)/4/vbus*100
    fn_slope_reg = fn_slope/100 * 2**8 / 0.004

    return [fn_slope, fn_slope_reg]


def get_l6470_bemf_vph(rm, ke, iph, lm, spd, int_spd):
    """
    Calculate compensation voltage based on intersec speed
    :param rm: Motor resistance per phase (Ohm)
    :param ke:
    :param iph:
    :param lm:
    :param spd:
    :param int_spd:
    :return:
    """
    if spd < int_spd:
        return rm * iph + ke * spd/4
    else:
        return 2*np.pi*spd/4*lm*iph + ke*spd/4

