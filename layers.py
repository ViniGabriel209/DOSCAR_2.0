import numpy as np
import matplotlib.pyplot as plt
from plotDOS import energiesAR, dos

plt.figure()             

# plt.plot(energiesAR[0], dos[0], label = 'Layer 1')      # LAYER 1
# plt.plot(energiesAR[0], dos[1], label = 'Layer 2')      # LAYER 2       
# plt.plot(energiesAR[0], dos[2], label = 'Layer 3')      # LAYER 3       
# plt.plot(energiesAR[0], dos[3], label = 'Layer 4')      # LAYER 4       
# plt.plot(energiesAR[0], dos[4], label = 'Layer 5')      # LAYER 5       
# plt.plot(energiesAR[0], dos[5], label = 'Layer 6')      # LAYER 6       
# plt.plot(energiesAR[0], dos[6], label = 'Layer 7')      # LAYER 7       
# plt.plot(energiesAR[0], dos[7], label = 'Layer 8')      # LAYER 8       
# plt.plot(energiesAR[0], dos[8], label = 'Layer 9')      # LAYER 9       
# plt.plot(energiesAR[0], dos[9], 'y', label = 'TiO2')      # LAYER 10      # INNER LAYER
# plt.plot(energiesAR[0], dos[10], label = 'Layer 11')     # LAYER 11        
# plt.plot(energiesAR[0], dos[11], label = 'Layer 12')     # LAYER 12        
# plt.plot(energiesAR[0], dos[12], label = 'Layer 13')     # LAYER 13        
# plt.plot(energiesAR[0], dos[13], label = 'Layer 14')     # LAYER 14        
# plt.plot(energiesAR[0], dos[14], label = 'Layer 15')     # LAYER 15        
# plt.plot(energiesAR[0], dos[15], label = 'Layer 16')     # LAYER 16        
# plt.plot(energiesAR[0], dos[16], label = 'Layer 17')     # LAYER 17        
# plt.plot(energiesAR[0], dos[17], label = 'Layer 18')     # LAYER 18       
# Perovskite ↓ 
# plt.plot(energiesAR[0], dos[18], label = 'Layer 19')     # LAYER 19        
# plt.plot(energiesAR[0], dos[19], label = 'Layer 20')     # LAYER 20        
# plt.plot(energiesAR[0], dos[20], label = 'Layer 21')     # LAYER 21        
# plt.plot(energiesAR[0], dos[21], label = 'Layer 22')     # LAYER 22        
# plt.plot(energiesAR[0], dos[22], label = 'Layer 23')     # LAYER 23        
# plt.plot(energiesAR[0], dos[23], label = 'Layer 24')     # LAYER 24        
# plt.plot(energiesAR[0], dos[24], label = 'Layer 25')     # LAYER 25        
# plt.plot(energiesAR[0], dos[25], label = 'Layer 26')     # LAYER 26        
# plt.plot(energiesAR[0], dos[26], label = 'Layer 27')     # LAYER 27        
# plt.plot(energiesAR[0], dos[27], 'g', label = 'Perovskite')     # LAYER 28      # INNER LAYER
# plt.plot(energiesAR[0], dos[28], label = 'Layer 29')     # LAYER 29        
# plt.plot(energiesAR[0], dos[29], label = 'Layer 30')     # LAYER 30        
# plt.plot(energiesAR[0], dos[30], label = 'Layer 31')     # LAYER 31        
# plt.plot(energiesAR[0], dos[31], label = 'Layer 32')     # LAYER 32        
# plt.plot(energiesAR[0], dos[32], label = 'Layer 33')     # LAYER 33        
# plt.plot(energiesAR[0], dos[33], label = 'Layer 34')     # LAYER 34        
# plt.plot(energiesAR[0], dos[34], label = 'Layer 35')     # LAYER 35        
# plt.plot(energiesAR[0], dos[35], label = 'Layer 36')     # LAYER 36        
# plt.plot(energiesAR[0], dos[36], label = 'Layer 37')     # LAYER 37        

plt.axhline(y = 0.0025, color = 'r')             
plt.legend()
plt.xlabel('Energy (eV)')             
plt.ylabel('DOS (A.U.)')             
plt.show()
