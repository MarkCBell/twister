
import pytest
from twister import Surface
from itertools import chain, product

S_1_1 = Surface('S_1_1')
S_2_1 = Surface('S_2_1')

words = chain(
    ((S_1_1, ''.join(letters)) for letters in product('aAbB', repeat=4)),
    ((S_2_1, ''.join(letters)) for letters in product('aAbBcCdDeE', repeat=2))
    )

@pytest.mark.parametrize('surface, word', words)
def test_homology(surface, word):
    if any(x == y for x, y in zip(word.swapcase(), word[1:] + word[:1])): return
    M = surface.bundle(word)
    M_homology = str(M.homology())
    M.dehn_fill((0,1))
    M_filled_homology = str(M.homology())

    assert M_homology == M_filled_homology
