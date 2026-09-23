import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

def RandSpherical():
    r = random.randint(0, 100)
    theta = round(random.uniform(0, math.pi), 4)
    phi = round(random.uniform(0, 2*math.pi), 4)
    return r, theta, phi

def ConvertSpherical(): 
    r, theta, phi = RandSpherical()
    x = round(r*math.sin(theta)*math.cos(phi), 5)
    y = round(r*math.sin(theta)*math.sin(phi), 5)
    z = round(r*math.cos(theta), 5)
    return x, y, z

def Plot():
    x, y, z = ConvertSpherical()
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    ax.scatter(x, y, z)
    plt.show()

Plot()t