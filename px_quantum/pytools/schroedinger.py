import numpy as np
from scipy.linalg import eigh_tridiagonal


class Schroedinger:
    """
    Class for solving the Schroedinger equation numerically.

    Methods
        get_ml2v(): Calculate the potential energy.
        get_w_v(): Calculate the eigenvalues and eigenvectors of the Hamiltonian.

    """

    def __init__(self):
        self.N = 1000
        self.x, self.dx = np.linspace(0, 1, self.N, retstep=True)

    def get_ml2v(self) -> np.ndarray:
        """
        Calculate the potential energy.

        Returns
            numpy.ndarray: An array of zeros.

        """
        return np.zeros(len(self.x))

    def get_w_v(self) -> tuple:
        """
        Calculate the eigenvalues and eigenvectors of the Hamiltonian.

        Returns
            Tuple[numpy.ndarray, numpy.ndarray]: The first 10 eigenvalues and eigenvectors.

        """
        main_diag = 1 / self.dx**2 + self.get_ml2v()[1:-1]
        off_diag = -1 / (2 * self.dx**2) * np.ones(len(main_diag) - 1)

        w, v = eigh_tridiagonal(main_diag, off_diag)

        return w[:10], v.T[:10]
