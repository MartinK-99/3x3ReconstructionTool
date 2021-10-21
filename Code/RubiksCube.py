import numpy as np

"""
Copyright MartinK-99 2021
"""

class Cube:
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

        self.u = np.array([["w","w","w"],["w","w","w"],["w","w","w"]])
        self.d = np.array([["y","y","y"],["y","y","y"],["y","y","y"]])
        self.r = np.array([["r","r","r"],["r","r","r"],["r","r","r"]])
        self.l = np.array([["o","o","o"],["o","o","o"],["o","o","o"]])
        self.f = np.array([["g","g","g"],["g","g","g"],["g","g","g"]])
        self.b = np.array([["b","b","b"],["b","b","b"],["b","b","b"]])

    # Matrix Rotation
    def rotateMatrix(self,A,r):
        # Clockwise Drehung der Matrix
        if r == "cw":
            A[0,0],A[0,1],A[0,2],A[1,2],A[2,2],A[2,1],A[2,0],A[1,0]= \
            A[2,0],A[1,0],A[0,0],A[0,1],A[0,2],A[1,2],A[2,2],A[2,1]
        # Counter-Clockwise Drehung der Matrix
        elif r == "ccw":
            A[2,0],A[1,0],A[0,0],A[0,1],A[0,2],A[1,2],A[2,2],A[2,1]= \
            A[0,0],A[0,1],A[0,2],A[1,2],A[2,2],A[2,1],A[2,0],A[1,0]
        # 180° Drehung der Matrix
        elif r == "2":
            A[0,0],A[0,1],A[0,2],A[1,2],A[2,2],A[2,1],A[2,0],A[1,0]= \
            A[2,2],A[2,1],A[2,0],A[1,0],A[0,0],A[0,1],A[0,2],A[1,2]
        else:
            print("dafuq you want from me")

        return A

    # Cube Rotation
    def rotation(self, r):
        if r == "x":
            self.b, self.d, self.f, self.u = self.u, self.b, self.d, self.f

            self.l = self.rotateMatrix(self.l, "ccw")
            self.r = self.rotateMatrix(self.r, "cw")
            self.b = self.rotateMatrix(self.b, "2")
            self.d = self.rotateMatrix(self.d, "2")
        elif r == "x'":
            self.u, self.b, self.d, self.f = self.b, self.d, self.f, self.u

            self.l = self.rotateMatrix(self.l, "cw")
            self.r = self.rotateMatrix(self.r, "ccw")
            self.b = self.rotateMatrix(self.b, "2")
            self.u = self.rotateMatrix(self.u, "2")

        elif r == "x2" or r == "x2'":
            self.u, self.b, self.d, self.f = self.d, self.f, self.u, self.b

            self.l = self.rotateMatrix(self.l, "2")
            self.r = self.rotateMatrix(self.r, "2")
            self.f = self.rotateMatrix(self.f, "2")
            self.b = self.rotateMatrix(self.b, "2")

        elif r == "y":
            self.f, self.r, self.b, self.l = self.r, self.b, self.l, self.f

            self.u = self.rotateMatrix(self.u, "cw")
            self.d = self.rotateMatrix(self.d, "ccw")
        elif r == "y'":
            self.r, self.b, self.l, self.f = self.f, self.r, self.b, self.l

            self.u = self.rotateMatrix(self.u, "ccw")
            self.d = self.rotateMatrix(self.d, "cw")
        elif r == "y2" or r == "y2'":
            self.r, self.b, self.l, self.f = self.l, self.f, self.r, self.b

            self.u = self.rotateMatrix(self.u, "2")
            self.d = self.rotateMatrix(self.d, "2")

        elif r == "z":
            self.u, self.l, self.d, self.r = self.l, self.d, self.r, self.u

            self.f = self.rotateMatrix(self.f, "cw")
            self.b = self.rotateMatrix(self.b, "ccw")
            self.u = self.rotateMatrix(self.u, "cw")
            self.d = self.rotateMatrix(self.d, "cw")
            self.r = self.rotateMatrix(self.r, "cw")
            self.l = self.rotateMatrix(self.l, "cw")
        elif r == "z'":
            self.l, self.d, self.r, self.u = self.u, self.l, self.d, self.r

            self.f = self.rotateMatrix(self.f, "ccw")
            self.b = self.rotateMatrix(self.b, "cw")
            self.u = self.rotateMatrix(self.u, "ccw")
            self.d = self.rotateMatrix(self.d, "ccw")
            self.r = self.rotateMatrix(self.r, "ccw")
            self.l = self.rotateMatrix(self.l, "ccw")
        elif r == "z2" or r == "z2'":
            self.l, self.d, self.r, self.u = self.r, self.u, self.l, self.d

            self.f = self.rotateMatrix(self.f, "2")
            self.b = self.rotateMatrix(self.b, "2")
            self.l = self.rotateMatrix(self.l, "2")
            self.r = self.rotateMatrix(self.r, "2")
            self.u = self.rotateMatrix(self.u, "2")
            self.d = self.rotateMatrix(self.d, "2")
        else:
            print("dafuq you want from me")

    # Moves ausschließlich mit Rotationen und R Moves definiert
    def move(self,mv):
        # Hardcoded R Rotationen
        if mv == "R":
            self.r = self.rotateMatrix(self.r, "cw")
            self.u[0, 2], self.u[1, 2], self.u[2, 2], self.b[0, 0], self.b[1, 0], self.b[2, 0], self.d[0, 2], self.d[
                1, 2], self.d[2, 2], self.f[0, 2], self.f[1, 2], self.f[2, 2] = \
                self.f[0, 2], self.f[1, 2], self.f[2, 2], self.u[2, 2], self.u[1, 2], self.u[0, 2], self.b[2, 0], \
                self.b[1, 0], self.b[0, 0], self.d[0, 2], self.d[1, 2], self.d[2, 2]
        elif mv == "R'":
            self.f[0, 2], self.f[1, 2], self.f[2, 2], self.u[2, 2], self.u[1, 2], self.u[0, 2], self.b[2, 0], self.b[
                1, 0], self.b[0, 0], self.d[0, 2], self.d[1, 2], self.d[2, 2] = \
                self.u[0, 2], self.u[1, 2], self.u[2, 2], self.b[0, 0], self.b[1, 0], self.b[2, 0], self.d[0, 2], \
                self.d[1, 2], self.d[2, 2], self.f[0, 2], self.f[1, 2], self.f[2, 2]
            self.r = self.rotateMatrix(self.r, "ccw")
        elif mv == "R2" or mv == "R2'":
            self.f[0, 2], self.f[1, 2], self.f[2, 2], self.u[2, 2], self.u[1, 2], self.u[0, 2], self.b[2, 0], self.b[
                1, 0], self.b[0, 0], self.d[0, 2], self.d[1, 2], self.d[2, 2] = \
                self.b[2, 0], self.b[1, 0], self.b[0, 0], self.d[2, 2], self.d[1, 2], self.d[0, 2], self.f[0, 2], \
                self.f[1, 2], self.f[2, 2], self.u[0, 2], self.u[1, 2], self.u[2, 2]
            self.r = self.rotateMatrix(self.r, "2")

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
    def algorithm(self,alg):
        algList = alg.split()
        for i in algList:
            if i in ["x","x'","x2","y","y'","y2","z","z'","z2"]:
                self.rotation(i)
            else:
                self.move(i)

    # Gibt aus ob Cube gelöst ist oder nicht
    def isSolved(self):
        return\
            np.all(self.u == self.u[0,0]) and \
            np.all(self.d == self.d[0,0]) and \
            np.all(self.f == self.f[0,0]) and \
            np.all(self.b == self.b[0,0]) and \
            np.all(self.l == self.l[0,0]) and \
            np.all(self.r == self.r[0,0])

    def __str__(self):
        string = str(self.u)+ "\n"
        string += str(np.concatenate((self.f,self.r,self.b,self.l),axis=1))
        string += "\n" + str(self.d)
        return string