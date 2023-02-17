from matplotlib.lines import lineStyles
import numpy as np
import matplotlib.pyplot as plt

vbm, cbm = np.genfromtxt('bandedges.txt', unpack = True)

layer = [-18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def bandalignment():
    
    plt.figure()
    plt.axhline(vbm[9], color = 'green', linestyle = '--')
    plt.axhline(vbm[27], color = 'green', linestyle = '--')
    plt.axhline(cbm[9], color = 'blue', linestyle = '--')
    plt.axhline(cbm[27], color = 'blue', linestyle = '--')
    plt.plot(layer, cbm, '-k', label = 'CBM')
    plt.plot(layer, vbm, '-r', label = 'VBM')
    plt.xlabel('TiO2       ← atomic layer →   perovskite')
    plt.ylabel('Energy (eV)')
    plt.legend()
    plt.show()

def getgaps():

    gaps = cbm - vbm
    gapTi = gaps[9]
    gapPe = gaps[27]

    vbo = vbm[27] - vbm[9]
    cbo = cbm[27] - cbm[9]

    print('================================')
    print('TiO2 - CsPbI3 relaxed DFT-05')
    print('================================')
    print('bandedges:     TiO2 | Perovskita')
    print(f'VBM           {vbm[9]:.3f} | {vbm[27]:.3f} eV')
    print(f'CBM           {cbm[9]:.3f} | {cbm[27]:.3f} eV')
    print('================================')
    print(f'bandgap TiO2         = {gapTi:.3f} eV')
    print(f'bandgap Perovskite   = {gapPe:.3f} eV')
    print('================================')
    print(f'VBO = {vbo:.3f} eV')
    print(f'CBO = {cbo:.3f} eV')
    print('================================')


bandalignment()
getgaps()
