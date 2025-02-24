import numpy as np
import pandas as pd
from matplotlib.pyplot import plot, show, title
import seaborn as sns

'''
print("All libraries imported successfully!")

# Simple plot
data = [1, 2, 3, 4, 5]
plot(data)
title("Test Plot")
show()
'''

'kelvin'
'''
def guess_the_number() -> None:
    secret_number = 7  # The number to guess
    guess = int(input("Guess a number between 1 and 10: "))  # Get user input

    if guess == secret_number:
        print("Woohoo! You guessed it right! The number was", secret_number)
    else:
        print("Sorry, wrong guess. The secret number was", secret_number)


guess_the_number()
'''

def frobenius_inner_product(A, B):
    """Computes the Frobenius inner product of two matrices A and B."""
    return np.trace(B.T @ A)  # Equivalent to sum of elementwise products


def gram_schmidt_frobenius(matrices):
    """Applies the Gram-Schmidt process using the Frobenius inner product."""
    orthogonal_basis = []

    for A in matrices:
        U = np.copy(A)  # Copy the matrix to modify it

        for prev_U in orthogonal_basis:
            # Compute projection coefficient
            proj_coeff = frobenius_inner_product(A, prev_U) / frobenius_inner_product(prev_U, prev_U)
            # Subtract projection
            U -= proj_coeff * prev_U

        orthogonal_basis.append(U)

    return np.array(orthogonal_basis)


# Given basis matrices
v1 = np.array([[1, 1], [1, -2]])
v2 = np.array([[-2, -1], [0, 2]])
v3 = np.array([[-6, -2], [-2, 9]])

basis_matrices = [v1, v2, v3]

# Compute the orthogonal basis
orthogonal_basis = gram_schmidt_frobenius(basis_matrices)

# Print the orthogonal basis
print("Orthogonal Basis Matrices:")
for i, mat in enumerate(orthogonal_basis, 1):
    print(f"U_{i}:\n", mat, "\n")