import numpy as np



"""
        cost1 cost2  
friend1
friend2
"""
coefs = np.array([[0,1,1],
                  [1,2,0],
                  [1,2,0],
                  [0,1,0]])


costs = np.array([[2000],[7000],[2000]])

"""already paied"""
payments = np.array([[2000],
                     [0],
                     [2000],
                     [7000]])
normalCoefs = coefs@np.linalg.inv(np.diag(coefs.sum(0)))
print(payments-normalCoefs@costs)
