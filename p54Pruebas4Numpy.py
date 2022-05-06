#Edgar Moises Hernandez Gonzalez (Moyete)
#26/09/18-12/01/19
#Pruebas4 Matrices con Numpy

import numpy as np

A=np.zeros((5,2))
B=np.ones((3,3))
C=np.zeros_like(B)
D=np.ones_like(A)

E=np.array([1,2,3])

print("A =")
print(A)
print("B =")
print(B)
print("C =")
print(C)
print("D =")
print(D)
print("E =")
print(E)

X=np.matrix('1 2;4 5')
Y=np.matrix('3 1;-2 1')
print("Producto 1= ")
print(X * Y)

A = np.array([[1, 2],
              [4, 5]])
B = np.array([[3, 1],
              [-2, 1]])
print("Producto 2= ")
print(A @ B)
print("Producto 3= ")
print(A.dot(B))