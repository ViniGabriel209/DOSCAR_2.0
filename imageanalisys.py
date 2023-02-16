'''
This code is an attempt to determine the band edges through the 2d image of the band alignment.
Unfortunately, the result was less precise than the traditional way.
More enhancement is welcome.
'''

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from plotDOS import energiesAR

img = cv.imread('dos2d.png')

pixels = []

altura, largura, canaisDeCor = img.shape

for y in range(altura):
    line = []
    for x in range(largura):

        line.append([y, x])

    pixels.append(line)

ymedio = altura // 2
xmedio = largura // 2

yedge = []
count = 0

for index, vetor in enumerate(pixels[:][ymedio]):

    if img.item(vetor[1], vetor[0], 0) == 0 and img.item(vetor[1], vetor[0], 1) == 0 and img.item(vetor[1], vetor[0], 2) == 0:
        yedge.append(index)
        count += 1

    if count == 2:
        break

xedge = []
count = 0

for index, vetor in enumerate(pixels[ymedio][::-1]):

    if img.item(vetor[0], vetor[1], 0) == 0 and img.item(vetor[0], vetor[1], 1) == 0 and img.item(vetor[0], vetor[1], 2) == 0:
        xedge.append(index)
        count += 1

xedge = xedge[2:]

xedge = [len(pixels[0]) - x for x in xedge]

img = img[yedge[0] + 1: yedge[1], xedge[1]: xedge[0] - 1]

cv.imwrite('onlydos.png', img)

# NEXT STEP OF THE CODE

newimg = cv.imread('onlydos.png')

pixels = []

altura, largura, canaisDeCor = newimg.shape

step = largura // 37

layers = [c for c in range(step // 2, largura, step)]

for y in range(altura):
    line = []
    for x in range(largura):

        line.append([y, x])

    pixels.append(line)

pixels = np.array(pixels)

positionsToParse = pixels[:, layers]

noDos = []

for number in range(37):    
    edgeline = []
    for index, vetor in enumerate(positionsToParse[:, number]):
        azul = newimg.item(vetor[0], vetor[1], 0)
        verde = newimg.item(vetor[0], vetor[1], 1)
        vermelho = newimg.item(vetor[0], vetor[1], 2)

        if azul == 59 and verde == 18 and vermelho == 48:
            edgeline.append(index)

    noDos.append(edgeline)

gaps = []

for lista in noDos:
    gap = []
    for index, position in enumerate(lista):

        if index == len(lista) - 1:
            if (position + 1 in lista or position - 1 in lista):
                gap.append(position)
            break
        if index == 0:
            continue
        if (lista[index + 1] - position != 1 or position - lista[index - 1] != 1) and (position + 1 in lista or position - 1 in lista):
            gap.append(position)

    del gap[0]
    gaps.append(gap)


X = energiesAR[0][0]
Y = energiesAR[0][-1]
x = 0
y = len(pixels) -1

count = 0
for i in gaps:
    if len(i) > count:
        count = len(i)

for i in gaps:
    for a in range(count - len(i)):
        i.append(np.nan)

gaps = np.array(gaps)
gaps = len(pixels) - gaps

bandedges = (X - Y) * (gaps - y) / (x - y) + Y