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

t1,y1 = co.step_response(FOPDT)
t2,y2 = co.impulse_response(FOPDT)

# plot results
plt.figure()
plt.plot(t1,y1,label='y(t) ultimate gain')
plt.plot([t1[0],t1[-1]],[np,np],'--','k')
plt.plot(t2,y2,label='y(t) disturbance')
plt.plot([t2[0],t2[-1]],[0,0],'--','k')
plt.legend()
plt.xlabel('time domain')
plt.show()