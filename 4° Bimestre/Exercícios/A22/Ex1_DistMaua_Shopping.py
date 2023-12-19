# Importação dos módulos
import numpy as np

# Programa principal
x = np.array([0, -178, -802, -1024, -935, -712, -612, -612, -590, -590, -623,   
                                                        -724, -724, -690, -590])
y = np.array([0, 78, 668, 1358, 1514, 1681, 2082, 2160, 2171, 2193, 2238, 2338, 
                                                              2371, 2416, 2416])

Dx = np.diff(x)
Dy = np.diff(y)

dist_rua = np.sum(np.sqrt(Dx**2 + Dy**2))
print("A distância entre a Mauá e o shopping é: %.2f m." %dist_rua)

dist_drone = np.sqrt(x[-1]**2 + y[-1]**2)
print("A distância entre a Mauá e o shopping de drone é: %.2f m." %dist_drone)