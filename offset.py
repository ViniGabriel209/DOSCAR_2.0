from matplotlib.lines import lineStyles
import numpy as np
import matplotlib.pyplot as plt

vbm, cbm = np.genfromtxt('bandedges.txt', unpack = True)

layer = [-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def bandalignment():
    
    plt.figure()
    plt.axhline(vbm[5], color = 'green', linestyle = '--')
    plt.axhline(vbm[16], color = 'green', linestyle = '--')
    plt.axhline(cbm[5], color = 'blue', linestyle = '--')
    plt.axhline(cbm[16], color = 'blue', linestyle = '--')
    plt.plot(layer, cbm, '-k', label = 'CBM')
    plt.plot(layer, vbm, '-r', label = 'VBM')
    plt.xlabel('TiO2       ← atomic layer →   perovskite')
    plt.ylabel('Energy (eV)')
    plt.legend()
    plt.show()

def getgaps():

    gaps = cbm - vbm
    gapTi = gaps[5]
    gapPe = gaps[16]

    vbo = vbm[16] - vbm[5]
    cbo = cbm[16] - cbm[5]

    print('================================')
    print('TiO2 - CsPbI3 relaxed DFT')
    print('================================')
    print('bandedges:     TiO2 | Perovskita')
    print(f'VBM           {vbm[5]:.3f} | {vbm[16]:.3f} eV')
    print(f'CBM           {cbm[5]:.3f} | {cbm[16]:.3f} eV')
    print('================================')
    print(f'bandgap TiO2         = {gapTi:.3f} eV')
    print(f'bandgap Perovskite   = {gapPe:.3f} eV')
    print('================================')
    print(f'VBO = {vbo:.3f} eV')
    print(f'CBO = {cbo:.3f} eV')
    print('================================')


bandalignment()
getgaps()