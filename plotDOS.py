import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from atomlayers import layers

dos1 = pd.DataFrame()
dos2 = pd.DataFrame()
dos3 = pd.DataFrame()
dos4 = pd.DataFrame()
dos5 = pd.DataFrame()
dos6 = pd.DataFrame()
dos7 = pd.DataFrame()
dos8 = pd.DataFrame()
dos9 = pd.DataFrame()
dos10 = pd.DataFrame()
dos11 = pd.DataFrame()
dos12 = pd.DataFrame()
dos13 = pd.DataFrame()
dos14 = pd.DataFrame()
dos15 = pd.DataFrame()
dos16 = pd.DataFrame()
dos17 = pd.DataFrame()
dos18 = pd.DataFrame()
dos19 = pd.DataFrame()
dos20 = pd.DataFrame()
dos21 = pd.DataFrame()
dos22 = pd.DataFrame()
dos23 = pd.DataFrame()
dos24 = pd.DataFrame()
dos25 = pd.DataFrame()
dos26 = pd.DataFrame()
dos27 = pd.DataFrame()
dos28 = pd.DataFrame()
dos29 = pd.DataFrame()
dos30 = pd.DataFrame()
dos31 = pd.DataFrame()
dos32 = pd.DataFrame()
dos33 = pd.DataFrame()
dos34 = pd.DataFrame()
dos35 = pd.DataFrame()
dos36 = pd.DataFrame()
dos37 = pd.DataFrame()

file = open('DOSCAR')
linhas = file.read().split('\n')

doscar = linhas[3006:]

for linha in doscar:
    if len(linha.split()) == 5 or linha == '':
        doscar.remove(linha)

doscar = [item.split() for item in doscar]

doscar = pd.DataFrame(doscar, columns = ['energy', 's', 'p', 'd'])
doscar['energy'] = doscar['energy'].astype(float)
doscar['s'] = doscar['s'].astype(float)
doscar['p'] = doscar['p'].astype(float)
doscar['d'] = doscar['d'].astype(float)

doscar['totaldos'] = doscar['s'] + doscar['p'] + doscar['d']

doscar.drop(['s', 'p', 'd'], axis = 1, inplace = True)

atoms = []

for i in range(1, 311):
    for j in range(3000):
        atoms.append(i)

doscar['atoms'] = pd.Series(atoms)

doscar.set_index('atoms', inplace = True)

for layer, atoms in enumerate(layers):
    for atom in atoms:
        if layer == 1:
            dos1[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 2:
            dos2[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 3:
            dos3[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 4:
            dos4[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 5:
            dos5[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 6:
            dos6[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 7:
            dos7[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 8:
            dos8[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 9:
            dos9[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 10:
            dos10[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 11:
            dos11[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 12:
            dos12[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 13:
            dos13[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 14:
            dos14[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 15:
            dos15[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 16:
            dos16[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 17:
            dos17[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 18:
            dos18[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 19:
            dos19[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 20:
            dos20[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 21:
            dos21[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 22:
            dos22[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 23:
            dos23[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 24:
            dos24[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 25:
            dos25[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 26:
            dos26[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 27:
            dos27[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 28:
            dos28[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 29:
            dos29[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 30:
            dos30[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 31:
            dos31[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 32:
            dos32[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 33:
            dos33[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 34:
            dos34[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 35:
            dos35[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        elif layer == 36:
            dos36[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')
        # if layer == 37:
        else:    
            dos37[f'dos{atom}'] = doscar.loc[atom, 'totaldos'].reset_index().drop(columns = 'atoms')

dos1 = dos1.sum(axis = 1).to_numpy()
dos2 = dos2.sum(axis = 1).to_numpy()
dos3 = dos3.sum(axis = 1).to_numpy()
dos4 = dos4.sum(axis = 1).to_numpy()
dos5 = dos5.sum(axis = 1).to_numpy()
dos6 = dos6.sum(axis = 1).to_numpy()
dos7 = dos7.sum(axis = 1).to_numpy()
dos8 = dos8.sum(axis = 1).to_numpy()
dos9 = dos9.sum(axis = 1).to_numpy()
dos10 = dos10.sum(axis = 1).to_numpy()
dos11 = dos11.sum(axis = 1).to_numpy()
dos12 = dos12.sum(axis = 1).to_numpy()
dos13 = dos13.sum(axis = 1).to_numpy()
dos14 = dos14.sum(axis = 1).to_numpy()
dos15 = dos15.sum(axis = 1).to_numpy()
dos16 = dos16.sum(axis = 1).to_numpy()
dos17 = dos17.sum(axis = 1).to_numpy()
dos18 = dos18.sum(axis = 1).to_numpy()
dos19 = dos19.sum(axis = 1).to_numpy()
dos20 = dos20.sum(axis = 1).to_numpy()
dos21 = dos21.sum(axis = 1).to_numpy()
dos22 = dos22.sum(axis = 1).to_numpy()
dos23 = dos23.sum(axis = 1).to_numpy()
dos24 = dos24.sum(axis = 1).to_numpy()
dos25 = dos25.sum(axis = 1).to_numpy()
dos26 = dos26.sum(axis = 1).to_numpy()
dos27 = dos27.sum(axis = 1).to_numpy()
dos28 = dos28.sum(axis = 1).to_numpy()
dos29 = dos29.sum(axis = 1).to_numpy()
dos30 = dos30.sum(axis = 1).to_numpy()
dos31 = dos31.sum(axis = 1).to_numpy()
dos32 = dos32.sum(axis = 1).to_numpy()
dos33 = dos33.sum(axis = 1).to_numpy()
dos34 = dos34.sum(axis = 1).to_numpy()
dos35 = dos35.sum(axis = 1).to_numpy()
dos36 = dos36.sum(axis = 1).to_numpy()
dos37 = dos37.sum(axis = 1).to_numpy()

# TRUNCATION OF THE ENERGY AND DOS ARRAYS
n = 2137   # line index of the minimum desired energy value

deleted = np.zeros(n)
c = 0

for i in range(0, n):
    deleted[i] = c
    c = c + 1

deleted = deleted[:].astype(int)

dos1 = np.delete(dos1, deleted)
dos2 = np.delete(dos2, deleted)
dos3 = np.delete(dos3, deleted)
dos4 = np.delete(dos4, deleted)
dos5 = np.delete(dos5, deleted)
dos6 = np.delete(dos6, deleted)
dos7 = np.delete(dos7, deleted)
dos8 = np.delete(dos8, deleted)
dos9 = np.delete(dos9, deleted)
dos10 = np.delete(dos10, deleted)
dos11 = np.delete(dos11, deleted)
dos12 = np.delete(dos12, deleted)
dos13 = np.delete(dos13, deleted)
dos14 = np.delete(dos14, deleted)
dos15 = np.delete(dos15, deleted)
dos16 = np.delete(dos16, deleted)
dos17 = np.delete(dos17, deleted)
dos18 = np.delete(dos18, deleted)
dos19 = np.delete(dos19, deleted)
dos20 = np.delete(dos20, deleted)
dos21 = np.delete(dos21, deleted)
dos22 = np.delete(dos22, deleted)
dos23 = np.delete(dos23, deleted)
dos24 = np.delete(dos24, deleted)
dos25 = np.delete(dos25, deleted)
dos26 = np.delete(dos26, deleted)
dos27 = np.delete(dos27, deleted)
dos28 = np.delete(dos28, deleted)
dos29 = np.delete(dos29, deleted)
dos30 = np.delete(dos30, deleted)
dos31 = np.delete(dos31, deleted)
dos32 = np.delete(dos32, deleted)
dos33 = np.delete(dos33, deleted)
dos34 = np.delete(dos34, deleted)
dos35 = np.delete(dos35, deleted)
dos36 = np.delete(dos36, deleted)
dos37 = np.delete(dos37, deleted)

dos = np.array([
    dos1,
    dos2,
    dos3,
    dos4,
    dos5,
    dos6,
    dos7,
    dos8,
    dos9,
    dos10,
    dos11,
    dos12,
    dos13,
    dos14,
    dos15,
    dos16,
    dos17,
    dos18,
    dos19,
    dos20,
    dos21,
    dos22,
    dos23,
    dos24,
    dos25,
    dos26,
    dos27,
    dos28,
    dos29,
    dos30,
    dos31,
    dos32,
    dos33,
    dos34,
    dos35,
    dos36,
    dos37
])

dos[0:18] = dos[0:18] / 12
dos[18::2] = dos[18::2] / 4
dos[19::2] = dos[19::2] / 6

# =========================
# ENERGY ARRAY MANIPULATION
# ========================= 

energiesDF = doscar.loc[1, 'energy'][:3000].reset_index().drop(columns = 'atoms')
energiesDF = energiesDF.to_numpy()
energiesDF = [energy[0] for energy in energiesDF]

deleted = np.zeros(n)            
c = 0            
            
for i in range(0, n):            
    deleted[i] = c            
    c = c + 1            
            
deleted = deleted[:].astype(int)            
        
energiesDF = np.delete(energiesDF, deleted)

energiesAR = np.array([
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
    energiesDF,
])

s = (37, len(dos1)) # N° de camadas, quantidade de energias
c = np.zeros(s)

for a in range(len(dos1)):
    for i in range(0, 37):
        c[i][a] = i + 1

# print(energiesAR.shape)
# print(dos.shape)
# print(c.shape)

def tridimensionalplot():

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.set_xlabel('Energy (eV)')    
    ax.set_ylabel('Layer')
    ax.set_zlabel('Density of states (A.U.)')

    surf = ax.plot_surface(energiesAR, c, dos, cmap = 'viridis', linewidth = 0, antialiased = False)
    cbar = fig.colorbar(surf, shrink = 0.5, aspect = 5)

    plt.show()


def bidimensionalplot():
    
    ax = plt.subplot()
    # im = ax.pcolormesh(c, e1, dos, cmap = 'viridis')
    im = ax.pcolormesh(c, energiesAR, dos, cmap = 'turbo')
    cbar = plt.colorbar(im, ticks = [dos.min(), dos.max()])
    cbar.ax.set_yticklabels(['min', 'max'])
    cbar.set_label('Density of states (A.U.)')
    plt.xlabel('Energy (eV)')
    plt.ylabel('Layer')
    plt.show()


# tridimensionalplot()
# bidimensionalplot()
