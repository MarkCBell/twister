
''' This is a module for testing twister. It uses S_0_4.sur to
generate all hyperbolic 2-bridge knot complements with up to 9 crossings
and checks them with SnapPy's Manifold.is_isometric_to() command. '''

import os
import pytest
from twister import Surface
import snappy

base_surface = Surface('S_0_4')
knots = open(os.path.join(os.path.dirname(__file__), 'knots.txt'), 'r').readlines()
knots = [knot.strip() for knot in knots if knot.strip()]
knots = [knot.split(',') for knot in knots]

def assertManifoldsIsometric(manifold, target):
    for _ in range(100):
        try:
            if manifold.is_isometric_to(target):
                return
        except RuntimeError:
            pass  # SnapPy couldn't decide if these are isometric or not.
        manifold.randomize()

    assert False

@pytest.mark.parametrize('knot, word', knots)
def test_knot(knot, word):
    M = base_surface.splitting(gluing='*'.join(word), handles='a*B')
    N = snappy.Manifold(knot)

    assertManifoldsIsometric(M, N)
