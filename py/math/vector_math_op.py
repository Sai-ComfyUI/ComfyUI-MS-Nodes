import os
import numpy as np

def evaluate(X_A, Y_A, Z_A, X_B, Y_B, Z_B,Operation)->list:
    
    A = np.array([X_A, Y_A, Z_A])
    B = np.array([X_B, Y_B, Z_B])
    
    if Operation == "Add":
        out = np.add(A, B)
    elif Operation == "Subtract":
        out = np.subtract(A, B)
    elif Operation == "Multiply":
        out = np.multiply(A, B)
    elif Operation == "Dvivie":
        out = np.divide(A, B)
        
    return out
