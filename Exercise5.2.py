import numpy as np 
import pandas as pd

def CreateVector():
    #Creates test vector
    tvector = np.zeros(10)
    for i in range(1, 11):
        tvector[i-1] = 1 + (i-1)*2
    return tvector

def WriteVector():
    #Writes test vector to a .txt file
    tvector = CreateVector()
    np.savetxt("tvector.txt", tvector, fmt="%d")

WriteVector()