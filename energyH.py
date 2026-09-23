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

htable = {
    "n": n,
    "Energy (cm-1)": wavenum,
    "Energy (J)": joule, 
    "Energy (Hartree)": hartree, 
    "Energy (eV)" : evolt
}

hdf = pd.DataFrame(htable)
print(hdf)