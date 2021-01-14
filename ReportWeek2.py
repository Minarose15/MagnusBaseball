# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 16:17:21 2021

@author: Sabrina
"""
from numpy import pi, sin, cos, exp, sqrt
from matplotlib import pyplot as plt
from numpy import linspace, cos, sin, cross

g = 9.80
S0_over_m = 4.1e-4
omega = [0, 0, 2000 * 2 * pi / 60]
theta = 45 * pi/180
v0 = 110 * 0.44704 #mph to m/s
vx = v0*cos(theta)
vy = v0*sin(theta)
vz = 0
v = [vx, vy, vz]
ve = sqrt(v[0]**2 + v[1]**2)
dt = 0.01 

def B2(velocity):
    return (0.0039 + 0.0058/(1 + exp((velocity-35)/5)))

xs = [0]
ys = [1.016]

print(S0_over_m * cross(omega, v))
while (ys[-1] > 0):
    magnus_acceleration = S0_over_m * cross(omega, v)
    ve = sqrt(v[0]**2 + v[1]**2)
    xs.append(xs[-1] + v[0]*dt)
    ys.append(ys[-1] + v[1]*dt)
    v[0] += -B2(ve) * ve * v[0] * dt + magnus_acceleration[0] * dt
    v[1] += -g*dt + magnus_acceleration[1] * dt - B2(ve) * ve * vy * dt
    
print(magnus_acceleration)
    
range_with_spin = xs[-1]    

v = 101 * 0.44704
vx = v*cos(theta)
vy = v*sin(theta)
v = [vx, vy, vz]
vz = 0
dt = 0.01
m = 0.149 

x = [0]
y = [1.016]

while (y[-1] > 0):
    ve = sqrt(v[0]**2 + v[1]**2)
    x.append(x[-1] + v[0]*dt)
    y.append(y[-1] + v[1]*dt)
    v[0] += -B2(ve) * ve * v[0] * dt
    v[1] += -g*dt - B2(ve) * ve * v[1] * dt

range_without_spin = x[-1]

plt.axes().set_facecolor('k')
plt.plot(xs,ys, label = "Range With Backspin", color = "springgreen")
plt.plot(x,y, label = "Range Without Spin", color = "fuchsia")
plt.legend()
plt.show()

print(range_with_spin, range_without_spin)

print("Backspin extends the range by ", (range_with_spin - range_without_spin), "m")