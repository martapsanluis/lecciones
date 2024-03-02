# -*- coding: utf-8 -*-
######Clases particulares de Lola#####
###########################
###########################
###Paquetes
import numpy as np
import sympy as sp
from sympy.solvers import solve

##########################3
#####TEMA 0########
print('------------------------------------------------')
print('------------------------------------------------')
print('Ejercicios del Tema 0')
print('------------------------------------------------')
print('------------------------------------------------ \n \n')
##### Ejercicio 1 #####
print('------------------------------------------------')
print('Ejercicio 0.1.')
print('------------------------------------------------')
A = [[6,3], [1,5]];
A = np.array(A); 
a = np.linalg.det(A);

B = [[-2, -3], [0,1]];
B = np.array(B);
b = np.linalg.det(B)

C = [[1.5, 4], [-1, 2]];
C = np.array(C);
c = np.linalg.det(C);
c = round(c);

D = [[1, 2, 3], [0, 1, 1], [2, 1, -1]];
D = np.array(D);
d = np.linalg.det(D);
d = round(d);

E = [[1, 0, 1], [-2, 1, -3], [2, 0, 3]];
E = np.array(E);
e = np.linalg.det(E);

F = [[6, 1/2, 3], [-1, 0, 1], [3, 2, -1]];
F = np.array(F);
f = np.linalg.det(F);

G = [[1, 1, 2], [0, 3, 0], [-2, -2, -4]];
G = np.array(G);
g = np.linalg.det(G);

print('\n a)', a, '\n b)', b, '\n c)', c,
      '\n d)', d, '\n e)', e, '\n f)', f, '\n g)', g, '\n \n')

###### Ejercicio 2 ########
print('------------------------------------------------')
print('Ejercicio 0.2')
print('------------------------------------------------')

A2 = [[2, 1, 3], [-4, -2, 0]];
A2 = np.array(A2)
ra = np.linalg.matrix_rank(A2);

B2 = [[6, -9], [-8, 12], [12, -18]];
B2 = np.array(B2);
rb = np.linalg.matrix_rank(B2);

C2 = [[3, 5, -2], [1, 4, 5], [8, 11, -11]];
C2 = np.array(C2);
rc = np.linalg.matrix_rank(C2);

D2 = [[1, -4, 0], [-2, 8, 3], [3, 1, -2]];
D2 = np.array(D2)
rd = np.linalg.matrix_rank(D2);

E2 = [[2, 6, 1, 3], [-2, 3, 0, 5], [2, 24, 3, 19]];
E2 = np.array(E2);
re = np.linalg.matrix_rank(E2);

F2 = [[-1, 2, 6, 3], [4, -8, -24, 1]];
F2 = np.array(F2);
rf = np.linalg.matrix_rank(F2);

G2 = [[-1, 2, 1, 3], [2, 1, 0, 1], [-1, 2, 1, -3]];
G2 = np.array(G2);
rg = np.linalg.matrix_rank(G2);

print('\n a)', ra, '\n b)', rb, '\n c)', rc,
      '\n d)', rd, '\n e)', re, '\n f)', rf, '\n g)', rg, '\n \n')

####### Ejercicio 3 ########
print('------------------------------------------------')
print('Ejercicio 0.3')
print('------------------------------------------------')

k = sp.Symbol('k');
M = sp.Matrix(( [k, k, 0], [2, k+1, k-1], [k-2, 0, 2*k+5] ));
detM = M.det();
sol = solve(detM, k);
print('El determinante de M vale', detM, '\n Se anula en...', sol)
####Caso k = 0 #####
M0 = M.subs(k, 0);
r0 = M0.rank();
####Caso k = 1 #####
M1 = M.subs(k, 1);
r1 = M1.rank();
####Caso k = -1 #####
M2 = M.subs(k, -1);
r2 = M2.rank();
#####Conclusion#####
print('Conclusion final:')
print('\n Si k no vale', sol, 'entonces el rango es 3.' 
      '\n Si k = 0, entonces el rango es', r0, 
      '\n Si k = 1, entonces el rango es', r1,
      '\n Si k = -1, entonces el rango es', r2,'. \n \n')

##### Ejercicio 4 ############
print('------------------------------------------------')
print('Ejercicio 0.4')
print('------------------------------------------------')
x = sp.Symbol('x');
d1 = sp.diff(x**2, x);
d2 = sp.diff(2*x, x);
print('\n 1)', d1,
      '\n 2)', d2, '\n \n')

###### Ejercicio extra 1 #######
print('------------------------------------------------')
print('Ejercicio extra 1')
print('------------------------------------------------')
### Multiplica Q1 por Q2 ####
Q1 = sp.Matrix(( [1, 0, 1], [0, 2, 3] ));
Q2 = sp.Matrix(( [1, 0, -1], [0, 0, 3] ));
Q2 = Q2.transpose()
### Solucion ####
Q3 = Q1*Q2
print('El producto de Q1 por Q2 da', Q3)

x = sp.Symbol('x');
### Multiplica P1 por P2 ####
P1 = sp.Matrix(( [x, 0, 1], [0, 2*x, x+1] ));
P2 = sp.Matrix(( [x, 0, -1], [0, 0, x-3] ));
P2 = P2.transpose()
### Solucion ####
P3 = P1*P2
print('El producto de P1 por P2 da', P3, '\n \n')

##### Ejercicio extra 2 #########
print('------------------------------------------------')
print('Ejercicio extra 2')
print('------------------------------------------------')
#### Estudiar el rango de N segun los valores de x ####
x = sp.Symbol('x');
N = sp.Matrix(( [x, 4], [1, x] ));
detN = N.det();
solN = solve(detN, x);
print('El determinante de N vale', detN, '\n Se anula en', solN, '\n')
#### Caso k = 2 #####
N0 = N.subs(x, 2);
n0 = N0.rank();
#### Caso k = -2 #####
N1 = N.subs(x, -2);
n1 = N1.rank();
##### Conclusion #####
print('Conclusion final:')
print(' Si k no vale', solN, 'entonces el rango es 2.' 
      '\n Si k = 2, entonces el rango es', n0, 
      '\n Si k = -2, entonces el rango es', n1,'. \n \n')
