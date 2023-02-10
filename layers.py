import numpy as np
import matplotlib.pyplot as plt
from plotDOS import energiesAR, dos

plt.figure()             

# plt.plot(energiesAR[0], dos[0])      # LAYER 1
# plt.plot(energiesAR[0], dos[1])      # LAYER 2       
# plt.plot(energiesAR[0], dos[2])      # LAYER 3       
# plt.plot(energiesAR[0], dos[3])      # LAYER 4       
# plt.plot(energiesAR[0], dos[4])      # LAYER 5       
# plt.plot(energiesAR[0], dos[5])      # LAYER 6       
# plt.plot(energiesAR[0], dos[6])      # LAYER 7       
# plt.plot(energiesAR[0], dos[7])      # LAYER 8       
# plt.plot(energiesAR[0], dos[8])      # LAYER 9       
# plt.plot(energiesAR[0], dos[9])      # LAYER 10       
# plt.plot(energiesAR[0], dos[10])     # LAYER 11        
# plt.plot(energiesAR[0], dos[11])     # LAYER 12        
# plt.plot(energiesAR[0], dos[12])     # LAYER 13        
# plt.plot(energiesAR[0], dos[13])     # LAYER 14        
# plt.plot(energiesAR[0], dos[14])     # LAYER 15        
# plt.plot(energiesAR[0], dos[15])     # LAYER 16        
# plt.plot(energiesAR[0], dos[16])     # LAYER 17        
# plt.plot(energiesAR[0], dos[17])     # LAYER 18        
# plt.plot(energiesAR[0], dos[18])     # LAYER 19        
# plt.plot(energiesAR[0], dos[19])     # LAYER 20        
# plt.plot(energiesAR[0], dos[20])     # LAYER 21        
# plt.plot(energiesAR[0], dos[21])     # LAYER 22        
# plt.plot(energiesAR[0], dos[22])     # LAYER 23        
# plt.plot(energiesAR[0], dos[23])     # LAYER 24        
# plt.plot(energiesAR[0], dos[24])     # LAYER 25        
# plt.plot(energiesAR[0], dos[25])     # LAYER 26        
# plt.plot(energiesAR[0], dos[26])     # LAYER 27        
# plt.plot(energiesAR[0], dos[27])     # LAYER 28        
# plt.plot(energiesAR[0], dos[28])     # LAYER 29        
# plt.plot(energiesAR[0], dos[29])     # LAYER 30        
# plt.plot(energiesAR[0], dos[30])     # LAYER 31        
# plt.plot(energiesAR[0], dos[31])     # LAYER 32        
# plt.plot(energiesAR[0], dos[32])     # LAYER 33        
# plt.plot(energiesAR[0], dos[33])     # LAYER 34        
# plt.plot(energiesAR[0], dos[34])     # LAYER 35        
# plt.plot(energiesAR[0], dos[35])     # LAYER 36        
# plt.plot(energiesAR[0], dos[36])     # LAYER 37        

plt.axhline(y = 0.0025, color = 'r')             
plt.xlabel('Energy (eV)')             
plt.ylabel('DOS (A.U.)')             
plt.show()