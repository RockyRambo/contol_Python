# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:40:49 2021

@author: ssala
"""

import numpy as npy
import matplotlib.pyplot as plt
import control as co

## gp
kp = 3
taup = 2
np = [kp]
dp = [taup,1]
gp = co.tf(np,dp)

td_p = 1
np_exp = [-td_p/2,1]
dp_exp = [td_p/2,1]
gp_exp = co.tf(np_exp,dp_exp)

FOPDT = gp*gp_exp

print(FOPDT)

## gc only PID

## Cohen - Coon PID
kc = 1/kp*taup/td_p*((3*td_p + 16*taup)/(12*taup))
tauI = td_p*(32 + 6*td_p/taup)/(13 + 8*td_p/taup)
tauD = 4*td_p/(11 + 2*td_p/taup)

alpha = 0.1

nc = [kc*(alpha*tauI*tauD+tauI*tauD),kc*(tauI+alpha*tauD),kc]
dc = [alpha*tauI*tauD,tauI,0]
gc = co.tf(nc,dc)

print(gc)

CL = (FOPDT*gc)/(1+FOPDT*gc)

t1,y1 = co.step_response(CL)
t2,y2 = co.impulse_response(CL)

# plot results
plt.figure()
plt.plot(t1,y1,label='y(t) set-point')
plt.plot([t1[0],t1[-1]],[1,1],'--','k')
# plt.plot(t2,y2,label='y(t) disturbance')
# plt.plot([t2[0],t2[-1]],[0,0],'--','k')
plt.legend()
plt.xlabel('time domain')
plt.show()