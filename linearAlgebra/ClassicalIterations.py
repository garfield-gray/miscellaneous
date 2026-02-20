"""
Jan 20 2026 
this code is meant to calculate the Jacobi & Gauss-Seidel iterations
"""
import numpy as np
A = np.array([[9,-2,1],
              [-1,5,-1],
              [1,-2,9]])
"""A = np.array([[2,-1],[-1,2]])"""
'''
A = np.array([[29,2,1],[2,6,1],[1,1,1/5]])
'''
D_A = np.diag(np.diag(A))
L_A = np.tril(A) - D_A
U_A = np.triu(A) - D_A

b = np.array([[13],
              [9],
              [-11]])

'''b = np.array([[10],[4]])'''

'''b = np.array([[10],[4],[100]])'''
M_J = D_A
N_J = -(L_A+U_A)

M_GS = L_A+D_A
N_GS = -U_A

Xinit = np.array([[0],[0],[0]])
def ClassicalIterations(M,N,b,X0 = Xinit,it = 6):
    X = X0
    for i in range(it):
        print(X)
        rhs = N@X+b
        X = np.linalg.solve(M,rhs)
        print(i)



ClassicalIterations(M_GS,N_GS,b)

"""
print(D_A)
print("*******************************")
print(L_A)
print("*******************************")
print(U_A)

"""
