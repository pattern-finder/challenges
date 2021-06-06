### Ajouté par l'API avant l'envoie à judge0


from math import *
import cv2 as cv




result = cv.imread("./pattern/rotation/result.png")
option1 = cv.imread("./pattern/rotation/option1.png")
option2 = cv.imread("./pattern/rotation/option2.png")
option3 = cv.imread("./pattern/rotation/option3.png")
option4 = cv.imread("./pattern/rotation/option4.png")
option5 = cv.imread("./pattern/rotation/option5.png")


listPattern = [option1, option2, option3, option4,option5 ]

# taille de l'image en pixel
size_picture = 23

# position de départ de la figure
start_X = 11
start_Y = 1



resultat = 3


def testAlgo():
    XY1 = (4, 7)
    XY2 = (18, 7)
    XY3 = (18, 15)
    XY4 = (4, 15)

    solution_user = doExercice(XY1, XY2, XY3, XY4)

    return assertRes(solution_user, resultat)


def assertRes(solution_user, resultat):
    if solution_user == resultat:
        return "SUCCESS"
    else:
        return "ERROR"


### FIN Ajouté par l'API avant l'envoie à judge0


### Algo crée par l'utilisateur


def doExercice(XY1, XY2, XY3, XY4):

    centreFigure=(11,11)
    idSolution = -1
    id = 0

    for pattern in listPattern:
        angle = 0
        while angle < 180:

                XY1_bis = rotate(XY1,centreFigure, angle)

                XY2_bis = rotate(XY2,centreFigure, angle)

                XY3_bis = rotate(XY3,centreFigure, angle)

                XY4_bis = rotate(XY4,centreFigure, angle)

                res = verifLine(XY1_bis[0], XY1_bis[1], XY2_bis[0], XY2_bis[1], pattern) and \
                verifLine(XY2_bis[0], XY2_bis[1], XY3_bis[0], XY3_bis[1], pattern) and \
                verifLine(XY3_bis[0], XY3_bis[1], XY4_bis[0], XY4_bis[1], pattern) and \
                verifLine(XY4_bis[0], XY4_bis[1], XY1_bis[0], XY1_bis[1], pattern)

                if res:
                    idSolution = id

                angle = angle + 1

        id = id + 1


    print(idSolution)
    return idSolution

def rotate (M, O, angle) :

    angle = angle*pi / 180;
    xM = M[0] - O[0];
    yM = M[1] - O[1];
    x = xM * cos (angle) + yM * sin(angle) + O[0];
    y = - xM * sin(angle) + yM * cos(angle) + O[1];
    return (round(x),round(y));




def verifLine(x1, y1, x2, y2, pattern):


    dx = x2 - x1
    if dx != 0:
        if dx > 0:
            dy = y2 - y1
            if dy !=0:

                if dy > 0:

                    if dx >= dy:
                        e = dx
                        dx = 2*e
                        dy = dy *2

                        if not pixelIsUp(x1, y1, pattern):
                            return False
                            print("")
                        while  x1 != x2:
                            if not pixelIsUp(x1, y1, pattern):
                                return False
                                print("")
                            x1 = x1 + 1
                            e = e - dy

                            if e < 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        if not pixelIsUp(x1, y1, pattern):
                            return False
                            print("")
                        while  y1 != y2:
                            if not pixelIsUp(x1, y1, pattern):
                                return False
                                print("")
                            y1 = y1 + 1
                            e = e - dx

                            if e < 0:
                                x1 = x1 + 1
                                e = e + dy

                else:

                    if dx >= -dy:
                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        if not pixelIsUp(x1, y1, pattern):
                            return False
                            print("")
                        while x1 != x2:
                            if not pixelIsUp(x1, y1, pattern):
                                return False
                                print("")
                            x1 = x1 + 1
                            e = e + dy

                            if e < 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        if not pixelIsUp(x1, y1, pattern):
                            return False
                            print("")
                        while y1 != y2:
                            if not pixelIsUp(x1, y1, pattern):
                                return False
                                print("")
                            y1 = y1 - 1
                            e = e + dx

                            if e > 0:
                                x1 = x1 + 1
                                e = e + dy
            else:
                while x1 != x2:
                    if not pixelIsUp(x1, y1, pattern):
                        return False
                        print("")
                    x1 = x1 + 1


        else:
            dy = y2 - y1
            if dy != 0:

                if dy > 0:

                    if -dx >= dy:
# 4eme octant

                        e = dx
                        dx = 2 * e
                        dy = dy * 2


                        if not pixelIsUp(x1, y1, pattern):
                            return False
                            print("")
                        while  x1 != x2:
                            if not pixelIsUp(x1, y1, pattern):
                                return False
                                print("")
                            x1 = x1 - 1
                            e = e + dy

                            if e >= 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        if not pixelIsUp(x1, y1, pattern):
                            return False
                            print("")
                        while y1 != y2:
                            if not pixelIsUp(x1, y1, pattern):
                                return False
                                print("")
                            y1 = y1 + 1
                            e = e + dx

                            if e <= 0:
                                x1 = x1 - 1
                                e = e + dy

                else:
# 5eme octant
                    if dx <= dy:
                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        if not pixelIsUp(x1, y1, pattern):
                            return False
                            print("")
                        while x1 != x2:
                            if not pixelIsUp(x1, y1, pattern):
                                return False
                                print("")
                            x1 = x1 - 1
                            e = e - dy

                            if e >= 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        if not pixelIsUp(x1, y1, pattern):
                            return False
                            print("")
                        while y1 != y2:
                            if not pixelIsUp(x1, y1, pattern):
                                return False
                                print("")
                            y1 = y1 - 1
                            e = e - dx

                            if e >= 0:
                                x1 = x1 - 1
                                e = e + dy

            else:
                if not pixelIsUp(x1, y1, pattern):
                    return False
                    print("")
                while x1 != x2:
                    x1 = x1 - 1
                    if not pixelIsUp( x1, y1, pattern):
                        return False
                        print("")
    else:
        dy = y2 - y1
        if dy != 0:
            if dy > 0:
                while y1 != y2:
                    y1 = y1 + 1
                    if not pixelIsUp( x1, y1, pattern):
                        return False
                        print("")
            else:
                while y1 != y2:
                    y1 = y1 - 1
                    if not pixelIsUp( x1, y1, pattern):
                        return False
                        print("")
    return True









def tailleCarre(hauteur):
    return 2 * hauteur + 1


def printMatrice(matrice):

    for line in matrice:
        print(getLine(line, 0))


def getLine(line, pos):

    if pos < len(line):
        return str(line[pos]) + getLine(line, pos+1)

    else:
        return ""


def pixelIsUp(x, y, matriceSource):

    return matriceSource[y][x][0] == 0 and matriceSource[y][x][0] == 0 and matriceSource[y][x][0] == 0









### FIN  Algo crée par l'utilisateur


if __name__ == '__main__':
    print("EXO 2")
    print(testAlgo())
