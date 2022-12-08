import dataclasses as d
import typing as t
from collections import deque

import numpy as np

"""
Copyright MartinK-99 2021
"""

Color: t.TypeAlias = str
Face: t.TypeAlias = t.Sequence[t.Sequence[Color]]

OUTER_COORDS = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (2, 1),
    (2, 0),
    (1, 0),
]
OUTER_COORDS_INV = {coord: i for i, coord in enumerate(OUTER_COORDS)}


@d.dataclass
class Face:
    """3x3 face, implemented with an efficient rotation method"""

    mid: Color
    outer: deque

    @classmethod
    def same_color(cls, c: Color):
        return cls(mid=c, outer=deque((c, c, c, c, c, c, c, c)))

    def __getitem__(self, item: t.Tuple[int, int]) -> Color:
        if item == (1, 1):
            return self.mid
        return self.outer[OUTER_COORDS_INV[item]]

    def __setitem__(self, key: t.Tuple[int, int], value: Color) -> None:
        if key == (1, 1):
            self.mid = value
        else:
            self.outer[OUTER_COORDS_INV[key]] = value

    @property
    def is_same_color(self) -> bool:
        return {self.mid} == set(self.outer)

    def rotate(self, how: str = "cw") -> None:
        if how == "cw":
            self.outer.rotate(-2)
            return
        if how == "2":
            self.outer.rotate(4)
        if how == "ccw":
            self.outer.rotate(2)

    @property
    def as_list(self) -> t.List[t.List[Color]]:
        return [[self[row, col] for row in range(3)] for col in range(3)]

    @property
    def as_ndarray(self) -> np.ndarray:
        return np.array(self.as_list)


class Cube:
    r: Face
    u: Face
    f: Face
    l: Face
    d: Face
    b: Face
    # no measurable benefit
    # __slots__ = ("r", "u", "f", "l", "d", "b")


    def __init__(self):
        # 0 Weiß
        # 1 Gelb
        # 2 Rot
        # 3 Orange
        # 4 Grün
        # 5 Blau
        # self.u = np.zeros((3,3))
        # self.d = 1*np.ones((3,3))
        # self.r = 2*np.ones((3,3))
        # self.l = 3*np.ones((3,3))
        # self.f = 4*np.ones((3,3))
        # self.b = 5*np.ones((3,3))

        self.u = Face.same_color("w")
        self.d = Face.same_color("y")
        self.r = Face.same_color("r")
        self.l = Face.same_color("o")
        self.f = Face.same_color("g")
        self.b = Face.same_color("b")

    # Matrix Rotation
    def rotateMatrix(self, A: Face, r: str):
        A.rotate(r)
        return A

    # Cube Rotation
    def rotation(self, r: str) -> None:
        if r == "x":
            self.b, self.d, self.f, self.u = self.u, self.b, self.d, self.f

            self.l.rotate("ccw")
            self.r.rotate("cw")
            self.b.rotate("2")
            self.d.rotate("2")
        elif r == "x'":
            self.u, self.b, self.d, self.f = self.b, self.d, self.f, self.u

            self.l.rotate("cw")
            self.r.rotate("ccw")
            self.b.rotate("2")
            self.u.rotate("2")

        elif r == "x2" or r == "x2'":
            self.u, self.b, self.d, self.f = self.d, self.f, self.u, self.b

            self.l.rotate("2")
            self.r.rotate("2")
            self.f.rotate("2")
            self.b.rotate("2")

        elif r == "y":
            self.f, self.r, self.b, self.l = self.r, self.b, self.l, self.f

            self.u.rotate("cw")
            self.d.rotate("ccw")
        elif r == "y'":
            self.r, self.b, self.l, self.f = self.f, self.r, self.b, self.l

            self.u.rotate("ccw")
            self.d.rotate("cw")
        elif r == "y2" or r == "y2'":
            self.r, self.b, self.l, self.f = self.l, self.f, self.r, self.b

            self.u.rotate("2")
            self.d.rotate("2")

        elif r == "z":
            self.u, self.l, self.d, self.r = self.l, self.d, self.r, self.u

            self.f.rotate("cw")
            self.b.rotate("ccw")
            self.u.rotate("cw")
            self.d.rotate("cw")
            self.r.rotate("cw")
            self.l.rotate("cw")
        elif r == "z'":
            self.l, self.d, self.r, self.u = self.u, self.l, self.d, self.r

            self.f.rotate("ccw")
            self.b.rotate("cw")
            self.u.rotate("ccw")
            self.d.rotate("ccw")
            self.r.rotate("ccw")
            self.l.rotate("ccw")
        elif r == "z2" or r == "z2'":
            self.l, self.d, self.r, self.u = self.r, self.u, self.l, self.d

            self.f.rotate("2")
            self.b.rotate("2")
            self.l.rotate("2")
            self.r.rotate("2")
            self.u.rotate("2")
            self.d.rotate("2")
        else:
            print("dafuq you want from me")

    # Moves ausschließlich mit Rotationen und R Moves definiert
    def move(self, mv: str) -> None:
        # Hardcoded R Rotationen
        if mv == "R":
            self.r.rotate("cw")
            self.u[0, 2], self.u[1, 2], self.u[2, 2], self.b[0, 0], self.b[1, 0], self.b[2, 0], self.d[0, 2], self.d[
                1, 2], self.d[2, 2], self.f[0, 2], self.f[1, 2], self.f[2, 2] = \
                self.f[0, 2], self.f[1, 2], self.f[2, 2], self.u[2, 2], self.u[1, 2], self.u[0, 2], self.b[2, 0], \
                self.b[1, 0], self.b[0, 0], self.d[0, 2], self.d[1, 2], self.d[2, 2]
        elif mv == "R'":
            self.f[0, 2], self.f[1, 2], self.f[2, 2], self.u[2, 2], self.u[1, 2], self.u[0, 2], self.b[2, 0], self.b[
                1, 0], self.b[0, 0], self.d[0, 2], self.d[1, 2], self.d[2, 2] = \
                self.u[0, 2], self.u[1, 2], self.u[2, 2], self.b[0, 0], self.b[1, 0], self.b[2, 0], self.d[0, 2], \
                self.d[1, 2], self.d[2, 2], self.f[0, 2], self.f[1, 2], self.f[2, 2]
            self.r.rotate("ccw")
        elif mv == "R2" or mv == "R2'":
            self.f[0, 2], self.f[1, 2], self.f[2, 2], self.u[2, 2], self.u[1, 2], self.u[0, 2], self.b[2, 0], self.b[
                1, 0], self.b[0, 0], self.d[0, 2], self.d[1, 2], self.d[2, 2] = \
                self.b[2, 0], self.b[1, 0], self.b[0, 0], self.d[2, 2], self.d[1, 2], self.d[0, 2], self.f[0, 2], \
                self.f[1, 2], self.f[2, 2], self.u[0, 2], self.u[1, 2], self.u[2, 2]
            self.r.rotate("2")

        elif mv == "L":
            self.rotation("z2")
            self.move("R")
            self.rotation("z2")
        elif mv == "L'":
            self.rotation("z2")
            self.move("R'")
            self.rotation("z2")
        elif mv == "L2" or mv == "L2'":
            self.rotation("z2")
            self.move("R2")
            self.rotation("z2")

        elif mv == "U":
            self.rotation("z")
            self.move("R")
            self.rotation("z'")
        elif mv == "U'":
            self.rotation("z")
            self.move("R'")
            self.rotation("z'")
        elif mv == "U2" or mv == "U2'":
            self.rotation("z")
            self.move("R2")
            self.rotation("z'")

        elif mv == "D":
            self.rotation("z'")
            self.move("R")
            self.rotation("z")
        elif mv == "D'":
            self.rotation("z'")
            self.move("R'")
            self.rotation("z")
        elif mv == "D2" or mv == "D2'":
            self.rotation("z'")
            self.move("R2")
            self.rotation("z")

        elif mv == "F":
            self.rotation("y'")
            self.move("R")
            self.rotation("y")
        elif mv == "F'":
            self.rotation("y'")
            self.move("R'")
            self.rotation("y")
        elif mv == "F2" or mv == "F2'":
            self.rotation("y'")
            self.move("R2")
            self.rotation("y")

        elif mv == "B":
            self.rotation("y")
            self.move("R")
            self.rotation("y'")
        elif mv == "B'":
            self.rotation("y")
            self.move("R'")
            self.rotation("y'")
        elif mv == "B2" or mv == "B2'":
            self.rotation("y")
            self.move("R2")
            self.rotation("y'")

        elif mv == "M":
            self.move("R")
            self.rotation("z2")
            self.move("R'")
            self.rotation("z2")
            self.rotation("x'")
        elif mv == "M'":
            self.move("R'")
            self.rotation("z2")
            self.move("R")
            self.rotation("z2")
            self.rotation("x")
        elif mv == "M2" or mv == "M2'":
            self.move("R2")
            self.rotation("z2")
            self.move("R2")
            self.move("z2")

        elif mv == "E":
            self.rotation("z")
            self.move("R")
            self.rotation("z2")
            self.move("R'")
            self.rotation("z")
            self.rotation("y'")
        elif mv == "E'":
            self.rotation("z")
            self.move("R'")
            self.rotation("z2")
            self.move("R")
            self.rotation("z")
            self.rotation("y")
        elif mv == "E2" or mv == "E2'":
            self.rotation("z")
            self.move("R2")
            self.rotation("z2")
            self.move("R2")
            self.rotation("z")
            self.rotation("y2")

        elif mv == "S":
            self.rotation("y'")
            self.move("R'")
            self.rotation("y2")
            self.move("R")
            self.rotation("z")
            self.rotation("x'")
        elif mv == "S'":
            self.rotation("y'")
            self.move("R")
            self.rotation("y2")
            self.move("R'")
            self.rotation("z'")
            self.rotation("x")
        elif mv == "S2" or mv == "S2'":
            self.rotation("y'")
            self.move("R2")
            self.rotation("y2")
            self.move("R2")
            self.rotation("x2")
            self.rotation("y'")

        elif mv == "Rw" or mv == "r":
            self.rotation("z2")
            self.move("R")
            self.rotation("z2")
            self.rotation("x")
        elif mv == "Rw'" or mv == "r'":
            self.rotation("z2")
            self.move("R'")
            self.rotation("z2")
            self.rotation("x'")
        elif mv == "Rw2" or mv == "r2" or mv == "Rw2'" or mv == "r2'":
            self.rotation("z2")
            self.move("R2")
            self.rotation("z2") # the mistake :O
            self.rotation("x2")

        elif mv == "Lw" or mv == "l":
            self.move("R")
            self.rotation("x'")
        elif mv == "Lw'" or mv == "l'":
            self.move("R'")
            self.rotation("x")
        elif mv == "Lw2" or mv == "l2" or mv == "Lw2'" or mv == "l2'":
            self.move("R2")
            self.rotation("x2")

        elif mv == "Uw" or mv == "u":
            self.rotation("z'")
            self.move("R")
            self.rotation("x'")
            self.rotation("z")
        elif mv == "Uw'" or mv == "u'":
            self.rotation("z'")
            self.move("R'")
            self.rotation("x")
            self.rotation("z")
        elif mv == "Uw2" or mv == "u2" or mv == "Uw2'" or mv == "u2'":
            self.rotation("z'")
            self.move("R2")
            self.rotation("z")
            self.rotation("y2")

        elif mv == "Dw" or mv == "d":
            self.rotation("z")
            self.move("R")
            self.rotation("x'")
            self.rotation("z'")
        elif mv == "Dw'" or mv == "d'":
            self.rotation("z")
            self.move("R'")
            self.rotation("x")
            self.rotation("z'")
        elif mv == "Dw2" or mv == "d2" or mv == "Dw2'" or mv == "d2'":
            self.rotation("z")
            self.move("R2")
            self.rotation("x2")
            self.rotation("z'")

        elif mv == "Fw" or mv == "f":
            self.rotation("y")
            self.move("R")
            self.rotation("x'")
            self.rotation("y'")
        elif mv == "Fw'" or mv == "f'":
            self.rotation("y")
            self.move("R'")
            self.rotation("x")
            self.rotation("y'")
        elif mv == "Fw2" or mv == "f2" or mv == "Fw2'" or mv == "f2'":
            self.rotation("y")
            self.move("R2")
            self.rotation("x2")
            self.rotation("y'")

        elif mv == "Bw" or mv == "b":
            self.rotation("y'")
            self.move("R")
            self.rotation("x'")
            self.rotation("y")
        elif mv == "Bw'" or mv == "b'":
            self.rotation("y'")
            self.move("R'")
            self.rotation("x")
            self.rotation("y")
        elif mv == "Bw2" or mv == "b2" or mv == "Bw2'" or mv == "b2'":
            self.rotation("y'")
            self.move("R2")
            self.rotation("x2")
            self.rotation("y")
        else:
            print("dafuq you want from me")

    # Algorithmus als String
    def algorithm(self, alg: str) -> None:
        algList = alg.split()
        for i in algList:
            if i in ["x","x'","x2","y","y'","y2","z","z'","z2"]:
                self.rotation(i)
            else:
                self.move(i)

    # Gibt aus ob Cube gelöst ist oder nicht
    def isSolved(self) -> bool:
        return all(
            f.is_same_color for f in (self.u, self.d, self.f, self.b, self.l, self.r)
        )

    def __str__(self):
        string = f"{self.u.as_ndarray}\n"
        string += str(
            np.concatenate(
                (
                    self.f.as_ndarray,
                    self.r.as_ndarray,
                    self.b.as_ndarray,
                    self.l.as_ndarray,
                ),
                axis=1,
            )
        )
        string += f"\n{self.d.as_ndarray}"
        return string
