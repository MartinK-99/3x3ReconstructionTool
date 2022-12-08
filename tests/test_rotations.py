from textwrap import dedent

import pytest

from Code.RubiksCube import Cube, Face


@pytest.fixture
def cube() -> Cube:
    return Cube()


ORDER_4_ALGS = (
    "R U F D B L R' U' F' D' B' L' "
    "Rw Uw Fw Dw Bw Lw "
    "Rw' Uw' Fw' Dw' Bw' Lw' "
    "r u f d b l "
    "r' u' f' d' b' l' "
    "M E S M' E' S'"
).split()


@pytest.mark.parametrize(
    "algo, expected_order",
    [("", 0)] +
    [(a, 1) for a in "x y z x' y' z'".split()] +
    [(a, 4) for a in ORDER_4_ALGS],
)
def test_algo_order(cube: Cube, algo: str, expected_order: int):
    for i in range(expected_order):
        if i not in {0, expected_order}:
            assert not cube.isSolved()
        cube.algorithm(algo)
    assert cube.isSolved()


def test_string(cube: Cube):
    assert (
        str(cube)
        == dedent(
            """\
        [['w' 'w' 'w']
         ['w' 'w' 'w']
         ['w' 'w' 'w']]
        [['g' 'g' 'g' 'r' 'r' 'r' 'b' 'b' 'b' 'o' 'o' 'o']
         ['g' 'g' 'g' 'r' 'r' 'r' 'b' 'b' 'b' 'o' 'o' 'o']
         ['g' 'g' 'g' 'r' 'r' 'r' 'b' 'b' 'b' 'o' 'o' 'o']]
        [['y' 'y' 'y']
         ['y' 'y' 'y']
         ['y' 'y' 'y']]
    """
        ).strip()
    )


def test_ndarray_conversion():
    import numpy as np

    assert np.all(Face.same_color("w").as_ndarray == np.array([["w"] * 3] * 3))
