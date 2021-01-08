# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:05:18 2021

@author: Santiago D. Salas, PhD sdsalas@espol.edu.ec
"""

import numpy as np
import matplotlib.pyplot as plt
import control as co

## FOPDT gp

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

## gc PID
## Cohen - Coon for tuning
kc = 1#1/kp*taup/td_p*((3*td_p + 16*taup)/(12*taup))
tauI = 10 #td_p*(32 + 6*td_p/taup)/(13 + 8*td_p/taup)
tauD = 10 #4*td_p/(11 + 2*td_p/taup)

alpha = 0.1

nc = [kc*(alpha*tauI*tauD+tauI*tauD),kc*(tauI+alpha*tauD),kc]## sdsalas@espol.edu.ec
dc = [alpha*tauI*tauD,tauI,0]
gc = co.tf(nc,dc)

CL = (FOPDT*gc)/(1+FOPDT*gc)

print(CL)

t1,y1 = co.step_response(CL)
# t2,y2 = co.impulse_response(CL) ## sdsalas@espol.edu.ec

g_OL = FOPDT*gc

### Poles
poles = co.pole(CL)
print(poles)

### Bode
bode_diag = co.bode_plot(g_OL, dB = True)

### Root Locus
RL_diag = co.root_locus(g_OL)

## Plot Results
plt.figure()
plt.plot(t1,y1,label='y(t) set point')
plt.plot([t1[0],t1[-1]],[1,1],'--')
# plt.plot(t2,y2,label='y(t) disturbance')
# plt.plot([t2[0],t2[-1]],[0,0],'--')
plt.legend()
plt.xlabel('time domain')
plt.ylabel('output')
plt.show()


