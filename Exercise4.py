import pandas as pd
import numpy as np
n = ["1", "2", "3", "4", "5", "6"]
wavenum1 = ["0.0000000000", "82259.158", "97492.304", "102823.904", "105291.657", "106632.1681"]
wavenum = np.array([float(w) for w in wavenum1])

j_conv= 6.626e-34 * 2.998e10
joule = wavenum * j_conv
h_conv = 4.55634e-6
hartree = wavenum * h_conv
e_conv = 8065.54
evolt = wavenum / e_conv

units = ["J", "Hartree", "eV"]
convfactor = [j_conv, h_conv, e_conv]
e_array = []

for factor in convfactor: 
    val = wavenum * factor
    e_array.append(val)


htable = {
    "n": n,
    "Energy (cm-1)": wavenum,
}

hdf = pd.DataFrame(htable)

num = 0

for unit in units: 
    hdf[f"Energy ({unit})"] = e_array[num]
    num+=1

print(hdf)