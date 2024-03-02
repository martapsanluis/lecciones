# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:10:07 2024

@author: Marta
"""
######Clases particulares de Lola#####
###########################
###########################
###Paquetes
import numpy as np
import sympy as sp
from sympy.solvers import solve

##########################3
#####TEMA 2########

# Como multiplicar un numero por un vector
A = sp.Matrix([[0, 2],[1, 2]])
a = sp.Matrix([-1, 2])
sola = A*a
print("Solucion de A por a", sola)

B = sp.Matrix([[0, -3, 0], [0, -1, 3], [0, -0, 2]]);
b = sp.Matrix([0, -1, 2])
solb = B*b
print("Solucion de B por b", solb, "\n \n")

# Ahora practica tu
c = sp.Matrix([3, 0])
solc = A*c
print("Solucion de A por c", solc)

E = sp.Matrix([[0, -3, 0], [0, -1, 3]]);
e = sp.Matrix([1, 2, 3])  
sole = E*e
print("Solucion de E por e", sole, "\n \n")             

# Diagonalizacion
M = sp.Matrix([[1, -3, 3], [3, -5, 3], [6, -6, 4]]);
P, D = M.diagonalize()

# Valores y vectores propios
landa = [D[0,0], D[1,1], D[2,2]]
v0 = P[:,0]
v1 = P[:,1]
v2 = P[:,2]

print("El vector", v0, "tiene autovalor", landa[0], 
      "y efectivamente multiplicar M por v0 da", M*v0)
 
# Esto no ocurre siempre!
w = sp.Matrix([0, 1, 2])
print("En cambio, M por (0, 1, 2) da", M*w, "que no es multiplo de w")