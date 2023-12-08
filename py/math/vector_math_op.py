import os
import numpy as np

def evaluate(X_A, Y_A, Z_A, X_B, Y_B, Z_B,Operation)->list:
    
    A = np.array([X_A, Y_A, Z_A])
    B = np.array([X_B, Y_B, Z_B])
    
    if Operation == "A+B":
        out = np.add(A, B)
    elif Operation == "A-B":
        out = np.subtract(A, B)
    elif Operation == "A*B":
        out = np.multiply(A, B)
    elif Operation == "A/B":
        out = np.divide(A, B)
        
    return out
