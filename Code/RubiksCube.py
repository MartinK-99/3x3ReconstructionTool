"""
Copyright MartinK-99 2022
"""

class Cube:

    CUBE_ROTATIONS = ["x","x'","x2","y","y'","y2","z","z'","z2"]

    CUBE_MOVES = ["U","U'","U2","U2'","Uw","Uw'","u","u'","Uw2","Uw2'","u2","u2'",
                  "D","D'","D2","D2'","Dw","Dw'","d","d'","Dw2","Dw2'","d2","d2'",
                  "F","F'","F2","F2'","Fw","Fw'","f","f'","Fw2","Fw2'","f2","f2'",
                  "B","B'","B2","B2'","Bw","Bw'","b","b'","Bw2","Bw2'","b2","b2'",
                  "R","R'","R2","R2'","Rw","Rw'","r","r'","Rw2","Rw2'","r2","r2'",
                  "L","L'","L2","L2'","Lw","Lw'","l","l'","Lw2","Lw2'","l2","l2'",
                  "M","M'","M2","M2'",
                  "E","E'","E2","E2'"
                  "S","S'","S2","S2'"]


    def __init__(self):
        """
        Every face of the Rubik's Cube is a 3x3 array
        with string elements according to its color.
        """
        self.u = [["w" for i in range(3)] for i in range(3)]
        self.d = [["y" for i in range(3)] for i in range(3)]
        self.r = [["r" for i in range(3)] for i in range(3)]
        self.l = [["o" for i in range(3)] for i in range(3)]
        self.f = [["g" for i in range(3)] for i in range(3)]
        self.b = [["b" for i in range(3)] for i in range(3)]


    def rotateFace(self, face : list[list[str,3],3], rotation : str) -> list[list[str,3],3]:
        """
        The face of the Rubik's Cube saved as a 3x3 array
        is rotated by +-90° or 180° depending on the input.
        The rotated face will be returned.

        Yeah... Try figuring out how that works
        """
        # Clockwise rotation of matrix
        if rotation in ["cw", "1", 1]:
            return [list(a) for a in zip(*face[::-1])]
        # Counter-Clockwise rotation of matrix
        elif rotation in ["ccw", "-1", -1, "3", 3]:
            return [list(a) for a in zip(*face)][::-1]
        # 180° rotation of matrix
        elif rotation in ["2", 2]:
            return [a[::-1] for a in face][::-1]
        else:
            raise Exception(f"Either the matrix input or \"{rotation}\" is not correct!\nTry \"cw\" for clockwise, \"ccw\" for counterclockwise and \"2\" for 180 degree rotation.")

    
    def rotation(self, rot : str):
        """
        Here the cube is rotated. The faces will
        be swapped and rotated accordingly.
        """
        if rot == "x":
            self.b, self.d, self.f, self.u = self.u, self.b, self.d, self.f

            self.l = self.rotateFace(self.l, "ccw")
            self.r = self.rotateFace(self.r, "cw")
            self.b = self.rotateFace(self.b, "2")
            self.d = self.rotateFace(self.d, "2")
        
        elif rot == "x'":
            self.u, self.b, self.d, self.f = self.b, self.d, self.f, self.u

            self.l = self.rotateFace(self.l, "cw")
            self.r = self.rotateFace(self.r, "ccw")
            self.b = self.rotateFace(self.b, "2")
            self.u = self.rotateFace(self.u, "2")

        elif rot == "x2" or rot == "x2'":
            self.u, self.b, self.d, self.f = self.d, self.f, self.u, self.b

            self.l = self.rotateFace(self.l, "2")
            self.r = self.rotateFace(self.r, "2")
            self.f = self.rotateFace(self.f, "2")
            self.b = self.rotateFace(self.b, "2")

        elif rot == "y":
            self.f, self.r, self.b, self.l = self.r, self.b, self.l, self.f

            self.u = self.rotateFace(self.u, "cw")
            self.d = self.rotateFace(self.d, "ccw")
       
        elif rot == "y'":
            self.r, self.b, self.l, self.f = self.f, self.r, self.b, self.l

            self.u = self.rotateFace(self.u, "ccw")
            self.d = self.rotateFace(self.d, "cw")
       
        elif rot == "y2" or rot == "y2'":
            self.r, self.b, self.l, self.f = self.l, self.f, self.r, self.b

            self.u = self.rotateFace(self.u, "2")
            self.d = self.rotateFace(self.d, "2")

        elif rot == "z":
            self.u, self.l, self.d, self.r = self.l, self.d, self.r, self.u

            self.f = self.rotateFace(self.f, "cw")
            self.b = self.rotateFace(self.b, "ccw")
            self.u = self.rotateFace(self.u, "cw")
            self.d = self.rotateFace(self.d, "cw")
            self.r = self.rotateFace(self.r, "cw")
            self.l = self.rotateFace(self.l, "cw")
       
        elif rot == "z'":
            self.l, self.d, self.r, self.u = self.u, self.l, self.d, self.r

            self.f = self.rotateFace(self.f, "ccw")
            self.b = self.rotateFace(self.b, "cw")
            self.u = self.rotateFace(self.u, "ccw")
            self.d = self.rotateFace(self.d, "ccw")
            self.r = self.rotateFace(self.r, "ccw")
            self.l = self.rotateFace(self.l, "ccw")
      
        elif rot == "z2" or rot == "z2'":
            self.l, self.d, self.r, self.u = self.r, self.u, self.l, self.d

            self.f = self.rotateFace(self.f, "2")
            self.b = self.rotateFace(self.b, "2")
            self.l = self.rotateFace(self.l, "2")
            self.r = self.rotateFace(self.r, "2")
            self.u = self.rotateFace(self.u, "2")
            self.d = self.rotateFace(self.d, "2")
        else:
            raise Exception(f"\"{rot}\" is not a valid cube rotation!")


    def U(self):
        """
        Does U move
        """
        self.u = self.rotateFace(self.u, 1) # Clockwise rotation of the upper face
        self.f[0], self.r[0], self.b[0], self.l[0] = self.r[0], self.b[0], self.l[0], self.f[0]
    def Uprime(self):
        """
        Does U' move
        """
        self.u = self.rotateFace(self.u, -1) # Counterclockwise rotation of the upper face
        self.f[0], self.r[0], self.b[0], self.l[0] = self.l[0], self.f[0], self.r[0], self.b[0]
    def U2(self):
        """
        Does U2 move
        """
        self.u = self.rotateFace(self.u, 2) # 180° rotation of the upper face
        self.f[0], self.r[0], self.b[0], self.l[0] = self.b[0], self.l[0], self.f[0], self.r[0]

    # Moves only defined by cube rotations and U moves
    def move(self, mv : str):
        """
        This function applys a move to the cube using
        cube rotations and only [U, U', U2] moves.
        """
        match mv:
            case "U":
                self.U()
            case "U'":
                self.Uprime()
            case "U2" | "U2'":
                self.U2()
            case "Uw" | "u":
                self.rotation("z2"); self.U(); self.rotation("z2"); self.rotation("y")
            case "Uw'" | "u'":
                self.rotation("z2"); self.Uprime(); self.rotation("z2"); self.rotation("y'")
            case "Uw2" | "u2" | "Uw2'" | "u2'":
                self.rotation("z2"); self.U2(); self.rotation("z2"); self.rotation("y2")
            
            case "D":
                self.rotation("x2"); self.U(); self.rotation("x2")
            case "D'":
                self.rotation("x2"); self.Uprime(); self.rotation("x2")
            case "D2" | "D2'":
                self.rotation("x2"); self.U2(); self.rotation("x2")
            case "Dw" | "d":
                self.U(); self.rotation("y'")
            case "Dw'" | "d'":
                self.Uprime(); self.rotation("y")
            case "Dw2" | "d2" | "Dw2'" | "d2'":
                self.U2(); self.rotation("y2")

            case "R":
                self.rotation("z'"); self.U(); self.rotation("z")
            case "R'":
                self.rotation("z'"); self.Uprime(); self.rotation("z")
            case "R2" | "R2'":
                self.rotation("z'"); self.U2(); self.rotation("z")
            case "Rw" | "r":
                self.rotation("z"); self.U(); self.rotation("z'"); self.rotation("x")
            case "Rw'" | "r'":
                self.rotation("z"); self.Uprime(); self.rotation("z'"); self.rotation("x'")
            case "Rw2" | "r2" | "Rw2'" | "r2'":
                self.rotation("z"); self.U2(); self.rotation("z'"); self.rotation("x2")

            case "L":
                self.rotation("z"); self.U(); self.rotation("z'")
            case "L'":
                self.rotation("z"); self.Uprime(); self.rotation("z'")
            case "L2" | "L2'":
                self.rotation("z"); self.U2(); self.rotation("z'")
            case "Lw" | "l":
                self.rotation("z'"); self.U(); self.rotation("z"); self.rotation("x'")
            case "Lw'" | "l'":
                self.rotation("z'"); self.Uprime(); self.rotation("z"); self.rotation("x")
            case "Lw2" | "l2" | "Lw2'" | "l2'":
                self.rotation("z'"); self.U2(); self.rotation("z"); self.rotation("x2")
            
            case "F":
                self.rotation("x"); self.U(); self.rotation("x'")
            case "F'":
                self.rotation("x"); self.Uprime(); self.rotation("x'")
            case "F2" | "F2'":
                self.rotation("x"); self.U2(); self.rotation("x'")
            case "Fw" | "f":
                self.rotation("x'"); self.U(); self.rotation("x"); self.rotation("z")
            case "Fw'" | "f'":
                self.rotation("x'"); self.Uprime(); self.rotation("x"); self.rotation("z'")
            case "Fw2" | "f2" | "Fw2'" | "f2'":
                self.rotation("x'"); self.U2(); self.rotation("x"); self.rotation("z2")

            case "B":
                self.rotation("x'"); self.U(); self.rotation("x")
            case "B'":
                self.rotation("x'"); self.Uprime(); self.rotation("x")
            case "B2" | "B2'":
                self.rotation("x'"); self.U2(); self.rotation("x")
            case "Bw" | "b":
                self.rotation("x"); self.U(); self.rotation("x'"); self.rotation("z'")
            case "Bw'" | "b'":
                self.rotation("x"); self.Uprime(); self.rotation("x'"); self.rotation("z")
            case "Bw2" | "b2" | "Bw2'" | "b2'":
                self.rotation("x"); self.U2(); self.rotation("x"); self.rotation("z2")

            case "M":
                self.rotation("z'"); self.U(); self.rotation("z2"); self.Uprime(); self.rotation("z'"); self.rotation("x'")
            case "M'":
                self.rotation("z'"); self.Uprime(); self.rotation("z2"); self.U(); self.rotation("z'"); self.rotation("x")
            case "M2" | "M2'":
                self.rotation("z'"); self.U2(); self.rotation("z2"); self.U2(); self.rotation("z'"); self.rotation("x2")
            
            case "S":
                self.rotation("x'"); self.U(); self.rotation("x2"); self.Uprime(); self.rotation("x'"); self.rotation("z")
            case "S'":
                self.rotation("x'"); self.Uprime(); self.rotation("x2"); self.U(); self.rotation("x'"); self.rotation("z'")
            case "S2" | "S2'":
                self.rotation("x'"); self.U2(); self.rotation("x2"); self.U2(); self.rotation("x'"); self.rotation("z2")

            case "E":
                self.U(); self.rotation("z2"); self.Uprime(); self.rotation("z2"); self.rotation("y'")
            case "E'":
                self.Uprime(); self.rotation("z2"); self.U(); self.rotation("z2"); self.rotation("y")
            case "E2" | "E2'":
                self.U2(); self.rotation("z2"); self.U2(); self.rotation("z2"); self.rotation("y2")
            
            case other:
                raise Exception(f"\"{mv}\" is not a valid move!")
            
    def algorithm(self, alg : str):
        """
        A sequence of moves is applied to the Rubik's Cube.
        """
        algList = alg.split()
        for el in algList:
            if el in self.CUBE_ROTATIONS:
                self.rotation(el)
            elif el in self.CUBE_MOVES:
                self.move(el)
            else:
                raise Exception(f"\"{el}\" is neither a valid cube rotation or move!")

    def isSolved(self) -> bool:
        """
        This functions returns True if the cube
        is solved otherwise False.
        """
        # List of lists to one single list
        list_u = [color for row in self.u for color in row]
        list_d = [color for row in self.d for color in row]
        list_f = [color for row in self.f for color in row]
        list_b = [color for row in self.b for color in row]
        list_l = [color for row in self.l for color in row]
        list_r = [color for row in self.r for color in row]

        # Check if set of elements per face is 1
        return  len(set(list_u)) == 1 and \
                len(set(list_d)) == 1 and \
                len(set(list_f)) == 1 and \
                len(set(list_b)) == 1 and \
                len(set(list_l)) == 1 and \
                len(set(list_r)) == 1

    def __str__(self) -> str:
        """
        Creates a string representation of the Rubik's Cube.
        """

        # Creates list of lists for every row
        rows = self.u # upper face
        for i in range(3): rows.append(self.f[i] + self.r[i] + self.b[i] + self.l[i]) # side faces
        for i in range(3): rows.append(self.d[i]) # bottom face
        
        # Generates string
        string = ""
        for r in rows:
            string += " ".join(r) + "\n"
        return string


c = Cube()
c.algorithm("R U R' U' R' F R2 U' R' U' R U R' F'")

print(c)