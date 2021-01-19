from numpy import pi, sin, cos, exp, sqrt, cross
from matplotlib import pyplot as plt

#Initialize variables with typical values for a baseball
g = 9.80
S0_over_m = 4.1e-4
omega = [0, 0, 2000 * 2 * pi / 60]
theta = 45 * pi/180
v0 = 110 * 0.44704 #mph to m/s
vx = v0*cos(theta)
vy = v0*sin(theta)
vz = 0
v = [v0*cos(theta), v0*sin(theta), 0]
ve = sqrt(v[0]**2 + v[1]**2)
dt = 0.01 

#This function returns the drag coefficient as a function of velocity
def B2(velocity):
    return (0.0039 + 0.0058/(1 + exp((velocity-35)/5)))

'''This function calculates the trajectory arrays necessary for plotting
    The parameter apply_magnus should be a value 0 or 1 to turn the Magnus on or off
    The function performs Euler's method with all the necessary acceleration terms 
'''
def getTrajectory(x, y, v, apply_magnus):
    while (y[-1] > 0):
        magnus_acceleration = S0_over_m * cross(omega, v)
        ve = sqrt(v[0]**2 + v[1]**2)
        x.append(x[-1] + v[0]*dt)
        y.append(y[-1] + v[1]*dt)
        v[0] += (-B2(ve) * ve * v[0] + magnus_acceleration[0] * apply_magnus) * dt
        v[1] += (-g + magnus_acceleration[1] * apply_magnus - B2(ve) * ve * v[1]) * dt
    return x, y
    
xs = [0]
ys = [1.016]

xs, ys = getTrajectory(xs,ys,v,1)
range_with_spin = xs[-1]    

v = [v0*cos(theta), v0*sin(theta), 0]

x = [0]
y = [1.016]

x,y = getTrajectory(x,y,v,0)
range_without_spin = x[-1]

plt.axes().set_facecolor('k')
plt.plot(xs, ys, label = "Range With Backspin", color = "springgreen")
plt.plot(x,y, label = "Range Without Spin", color = "fuchsia")
plt.legend()
plt.show()

print(range_with_spin, range_without_spin)

print("Backspin extends the range by ", (range_with_spin - range_without_spin), "m")
