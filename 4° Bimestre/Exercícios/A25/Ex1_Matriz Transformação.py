# Importação dos módulos
import numpy as np

# Programa principal
dx = float(input("Digite o valor de dx: "))
dy = float(input("Digite o valor de dy: "))
teta = float(input("Digite o valor de teta: "))
teta = np.radians(teta)

T = np.array([[1, 0, -dx], [0, 1, -dy], [0, 0, 1]])
print("T =\n", T)

R = np.array([[np.cos(teta), -np.sin(teta), 0], [np.sin(teta), np.cos(teta), 0], [0, 0, 1]])
print("\nR =\n", R)

M = np.linalg.inv(T)@R@T
print("\nM =\n", M)