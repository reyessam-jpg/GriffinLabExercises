import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt

def InitialParam(step):
    #Define initial cartesians
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    z = random.randint(0, 10)
    #Define initial velocity, mass
    vx = random.randint(0, 10)
    vy = random.randint(0, 10)
    vz = random.randint(0, 10)
    m = random.randint(1, 10)
    #Define position and velocity vectors
    xpos = np.zeros(step+1)
    xpos[0] = x
    ypos = np.zeros(step+1)
    ypos[0] = y
    zpos = np.zeros(step+1)
    zpos[0] = z
    xvelo = np.zeros(step+1)
    xvelo[0] = vx
    yvelo = np.zeros(step+1)
    yvelo[0] = vy
    zvelo = np.zeros(step+1)
    zvelo[0] = vz
    #Define acceleration vectors (z vec = gravity)
    xa = random.randint(0, 10)
    ya = random.randint(0, 10)
    za = -9.8

    return xpos, ypos, zpos, xvelo, yvelo, zvelo, xa, ya, za, m

def ParticleMove():
    #Define time step size and steps, import params
    dt = 0.001
    steps = 5000
    xpos, ypos, zpos, xvelo, yvelo, zvelo, xa, ya, za, m = InitialParam(5000)

    #Iterate through steps using Newtonian equations of motion
    for step in range(steps): 
        xpos[step+1] = xpos[step] + xvelo[step]*dt + 0.5*xa*dt**2
        ypos[step+1] = ypos[step] + yvelo[step]*dt + 0.5*ya*dt**2
        zpos[step+1] = zpos[step] + zvelo[step]*dt + 0.5*za*dt**2
        if zpos[step+1] <= 0:
            zpos[step +1] = 0
        xvelo[step+1] = xvelo[step] + xa*dt
        yvelo[step+1] = yvelo[step] + ya*dt
        zvelo[step+1] = zvelo[step] + za*dt
    return xpos, ypos, zpos

def VisualizeGrav():
    xpos, ypos, zpos = ParticleMove()
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    ax.scatter(xpos, ypos, zpos)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Gravity Sim")
    plt.savefig("/Users/sreyes/Desktop/GG QD/drag_testGrav.png")

def Drag(shape, grav):
    #shape 0=sphere, 1=cube, grav 0 = y, 1 = n
    #quad drag, rho in kg/m^3, drag coeff for sphere or cube, import start params and steps initialization
    rho = 1.225
    sphere = 0.47
    cube = 1.05
    #cross-sec area in m^2
    area = random.randint(1,10)
    xpos, ypos, zpos, xvelo, yvelo, zvelo, xa, ya, za, m = InitialParam(5000)
    if grav == 0: 
        za = -9.8
    if grav ==1:
        za = random.randint(0, 10)
    dt = 0.001
    steps = 5000
    if shape == 0:
        for step in range(steps): 
            #Get speed vector of all three coordinates
            speed = np.sqrt(xvelo[step]**2 + yvelo[step]**2 + zvelo[step]**2)
            #calculate drag
            drag = -(rho*sphere*area) / (2*m) * speed

            #Update acceleration with drag factor

            xacc = xa + drag*xvelo[step]
            yacc = ya + drag*yvelo[step]
            zacc = za + drag*zvelo[step]

            xpos[step+1] = xpos[step] + xvelo[step]*dt + 0.5*xacc*dt**2
            ypos[step+1] = ypos[step] + yvelo[step]*dt + 0.5*yacc*dt**2
            zpos[step+1] = zpos[step] + zvelo[step]*dt + 0.5*zacc*dt**2
            if zpos[step+1] <= 0:
                zpos[step +1] = 0
            xvelo[step+1] = xvelo[step] + xacc*dt
            yvelo[step+1] = yvelo[step] + yacc*dt
            zvelo[step+1] = zvelo[step] + zacc*dt

    if shape == 1: 
        for step in range(steps): 
            #Get speed vector of all three coordinates
            speed = np.sqrt(xvelo[step]**2 + yvelo[step]**2 + zvelo[step]**2)
            #calculate drag
            drag = -(rho*cube*area) / (2*m) * speed

            #Update acceleration with drag factor

            xacc = xa + drag*xvelo[step]
            yacc = ya + drag*yvelo[step]
            zacc = za + drag*zvelo[step]

            xpos[step+1] = xpos[step] + xvelo[step]*dt + 0.5*xacc*dt**2
            ypos[step+1] = ypos[step] + yvelo[step]*dt + 0.5*yacc*dt**2
            zpos[step+1] = zpos[step] + zvelo[step]*dt + 0.5*zacc*dt**2
            if zpos[step+1] <= 0:
                zpos[step +1] = 0
            xvelo[step+1] = xvelo[step] + xacc*dt
            yvelo[step+1] = yvelo[step] + yacc*dt
            zvelo[step+1] = zvelo[step] + zacc*dt
    return xpos, ypos, zpos, grav

def VisualizeDrag(shape, grav): 
    xpos, ypos, zpos, grav= Drag(shape, grav)
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    ax.scatter(xpos, ypos, zpos)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    if shape == 0: 
        if grav ==0:
            ax.set_title("Sphere Drag Sim with Gravity")
            plt.savefig("/Users/sreyes/Desktop/GG QD/drag_testSphereWithGravity.png")
        if grav ==1:
            ax.set_title("Sphere Drag Sim without Gravity")
            plt.savefig("/Users/sreyes/Desktop/GG QD/drag_testSphereNoGravity.png")
    if shape ==1: 
        if grav ==0:
            ax.set_title("Cube Drag Sim with Gravity")
            plt.savefig("/Users/sreyes/Desktop/GG QD/drag_testCubeWithGravity.png")
        if grav ==1:
            ax.set_title("Cube Drag Sim without Gravity")
            plt.savefig("/Users/sreyes/Desktop/GG QD/drag_testCubeNoGravity.png")

VisualizeGrav()
VisualizeDrag(0, 0)
VisualizeDrag(1, 0)
VisualizeDrag(0, 1)
VisualizeDrag(1, 1)
plt.show()