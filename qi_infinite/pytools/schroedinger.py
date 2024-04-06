import numpy as np
from scipy.linalg import eigh_tridiagonal


class Schroedinger:
    def __init__(self):
        self.N = 100
        self.x, self.dx = np.linspace(0, 1, self.N, retstep=True)

    def get_mL2V(self):
        return np.zeros(len(self.x))

    def get_w_v(self):
        main_diag = 1 / self.dx**2 + self.get_mL2V()[1:-1]
        off_diag = -1/(2*self.dx**2) * np.ones(len(main_diag)-1)

        w, v = eigh_tridiagonal(main_diag, off_diag)

        return w[:10], v.T[:10]
