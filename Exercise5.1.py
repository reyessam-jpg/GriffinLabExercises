import pandas as pd
import numpy as np
def HTable():
#Create Hydrogen E table dataframe
    n = ["1", "2", "3", "4", "5", "6"]
    wavenum1 = ["0.0000000000", "82259.158", "97492.304", "102823.904", "105291.657", "106632.1681"]
    wavenum = np.array([float(w) for w in wavenum1])
    j_conv= 6.626e-34 * 2.998e10
    joule = wavenum * j_conv
    h_conv = 4.55634e-6
    hartree = wavenum * h_conv
    e_conv = 8065.54
    evolt = wavenum / e_conv

    htable = {
        "n": n,
        "Energy (cm-1)": wavenum,
        "Energy (J)": joule, 
        "Energy (Hartree)": hartree, 
        "Energy (eV)" : evolt
    }
    hdf = pd.DataFrame(htable)
    return hdf

def HTableArray():
#Create HTable then shape array around elements. 
#Column headders pulled and stored in another array paired alongside the mdvar array

    hdftemplate = HTable()
    mdvar = np.empty(hdftemplate.shape)
    mdvarhead = np.array(hdftemplate.columns, dtype=str)

#Iterate through rows then each column of a row, pulls element then assigns to numpy matrix

    for row in range(len(hdftemplate)):
        for col in range(len(hdftemplate.columns)):
            mdvar[row, col] = hdftemplate.iloc[row, col]

    return mdvar, mdvarhead

def HTableWrite():
#Write to binary file, numpy function preserves dtype 

   mdvar, mdvarhead = HTableArray()
   np.savez("htable.npz", headers=mdvarhead, values=mdvar)

def HTableRead():
#Read binary file and convert back into array then dataframe

    readtable = np.load("htable.npz")
    headers = readtable['headers']
    values = readtable['values']
    hdfnew = pd.DataFrame(values, columns = headers)
    hdfnew['n'] = hdfnew['n'].astype(int).astype(str)
    return hdfnew

def HTableComp():
    hdf = HTable()
    hdfnew = HTableRead()
    hdfbool = np.empty(hdf.shape)
    for row in range(len(hdf)):
        for col in range(len(hdf.columns)):
            hdfbool[row,col] = hdf.iloc[row,col]==hdfnew.iloc[row,col]
    print(hdf, hdfnew, hdfbool, sep='n\n')

HTableWrite()
HTableRead()
HTableComp()