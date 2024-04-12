import numpy as np

from ..pytools.schroedinger import Schroedinger


def test_mL2V():
    assert Schroedinger().get_mL2V().all() == np.zeros(100).all()


def test_eigenvalues():
    w, v = Schroedinger().get_w_v()

    assert len(w) == 10
    assert len(v) == 10
