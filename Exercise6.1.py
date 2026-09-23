import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def TriangleGraph():
    xcoord = [-50, 0, 50]
    ycoord = [0, 50, 0]
    plt.plot(xcoord, ycoord)
    plt.xlabel('X Axis Quantity (unitless)')
    plt.ylabel('Y Axis Quantity (unitless)')
    plt.title('Exercise 6.1')
    plt.show()

TriangleGraph()