# This file contains the atomic positions of CsSnI3tet-TiO2 heterostructure

poscar = open('POSCAR', 'r')
positions = poscar.read().split('\n')
positions = positions[9 : -1]

layers = []

z = [1.483500,
     2.967000,
     4.450500,
     5.934000,
     7.417500,
     8.901000,
    10.384500,
    11.868000,
    13.351501,
    14.835001,
    16.318501,
    17.802001,
    19.285501,
    20.769001,
    22.252501,
    23.736001,
    25.219501,
    26.703001,
    29.200001,
    32.292309,
    35.384616,
    38.476924,
    41.569232,
    44.661540,
    47.753848,
    50.846156,
    53.938463,
    57.030771,
    60.123079,
    63.215387,
    66.307695,
    69.400003,
    72.492310,
    75.584618,
    78.676926,
    81.769234,
    84.861542
     ]

coordinates = []

for i in range(len(positions)):
     coordinates.append(positions[i].split())


for i in range(len(z)):

     atoms = []

     for c in range(len(coordinates)):

          if float(coordinates[c][2]) == z[i]:
               atoms.append(c + 1)
             
     layers.append(atoms)
