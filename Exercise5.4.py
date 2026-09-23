import numpy as np
import pandas as pd
import random
from sympy import randprime

def Sample3D():
    sample = np.zeros((3,3,3))
    for layer in range(sample.shape[0]):
        for row in range(sample.shape[1]):
            for col in range(sample.shape[2]):
                sample[layer, row, col] = randprime(1,40)
    return sample

def Write3D():
    sample = Sample3D()
    np.save("sample3D.npy", sample)

def Read3D():
    sampleread = np.load("sample3D.npy")
    print(sampleread)

Write3D()
Read3D()