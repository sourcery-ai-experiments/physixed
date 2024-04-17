import numpy as np

from ..pytools.schroedinger import Schroedinger


def test_ml2v():
    assert Schroedinger().get_ml2v().all() == np.zeros(100).all()


def test_eigenvalues():
    w, v = Schroedinger().get_w_v()

    assert len(w) == 10
    assert len(v) == 10
