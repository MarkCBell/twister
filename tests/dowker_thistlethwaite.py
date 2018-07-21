
import pytest
import os
from twister import DT_drilling_surface, DT_handles_surface
import snappy

codes = open(os.path.join(os.path.dirname(__file__), 'DT.txt'), 'r').readlines()

def assertManifoldsIsometric(manifold, target):
    for _ in range(100):
        try:
            if manifold.is_isometric_to(target):
                return
        except RuntimeError:
            pass  # SnapPy couldn't decide if these are isometric or not.
        manifold.randomize()

    assert False

@pytest.mark.parametrize('code', codes)
def test_drilling(code):
    code = code.strip()
    encode = list(map(int, code.split(',')))
    M = DT_drilling_surface(encode).splitting(gluing="s", handles="h")
    N = snappy.Manifold('DT[%s]' % str(code))

    assertManifoldsIsometric(M, N)

@pytest.mark.parametrize('code', codes)
def test_handles(code):
    code = code.strip()
    encode = list(map(int, code.split(',')))
    M = DT_handles_surface(encode).splitting(gluing="", handles="h")
    N = snappy.Manifold('DT[%s]' % str(code))

    assertManifoldsIsometric(M, N)

