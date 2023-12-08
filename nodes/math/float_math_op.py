import os

def evaluate(A, B, Operation):
    if Operation == "Add":
        out = A + B
    elif Operation == "Subtract":
        out = A - B
    elif Operation == "Multiply":
        out = A * B
    elif Operation == "Dvivie":
        out = A / B

    return out
