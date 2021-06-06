### Ajouté par l'API avant l'envoie à judge0

import cv2 as cv
import matplotlib
import numpy

matrice = cv.imread("./pattern/exo3/repCercle.png")

class Pixel:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def comparePixelColor(self, other):
        if isinstance(other, self.__class__):
            return self.red == other.red and \
                   self.green == other.green and \
                   self.blue == other.blue
        else:
            return False


concepte = "cercle"

matriceInputPattern2 = [[0,0,0,0,0,1,1,1,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0,0],


                        ]

matriceInputPattern1 = [[0,0,0,1,1,1,1,1,1,1,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,1,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,1,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,1,1,1,1,1,1,1,0,0,0],


                        ]
matriceInputPattern3 = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0,0],


                        ]


matricetest2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

patternTest =           [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         ]


listPattern2 = [matriceInputPattern1, matriceInputPattern2, matriceInputPattern3]
listPattern = [matrice]

# taille de l'image en pixel
size_picture = 24

# position de départ de la figure
start_X = 12
start_Y = 12



resultat = 0


def testAlgo():
    solution_user = doExercice3(0,10,10,10)

    return assertRes(solution_user, resultat)


def assertRes(solution_user, resultat):
    if solution_user == resultat:
        return "SUCCESS"
    else:
        return "ERROR"


### FIN Ajouté par l'API avant l'envoie à judge0


### Algo crée par l'utilisateur

def doExercice3(x1, y1, x2, y2):

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

                        pixelAllume(patternTest, x1, y1)
                        while  x1 != x2:
                            pixelAllume(patternTest, x1, y1)
                            x1 = x1 + 1
                            e = e - dy

                            if e < 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        pixelAllume(patternTest, x1, y1)
                        while  y1 != y2:
                            pixelAllume(patternTest, x1, y1)
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

                        pixelAllume(patternTest, x1, y1)
                        while x1 != x2:
                            pixelAllume(patternTest, x1, y1)
                            x1 = x1 + 1
                            e = e + dy

                            if e < 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        pixelAllume(patternTest, x1, y1)
                        while y1 != y2:
                            pixelAllume(patternTest, x1, y1)
                            y1 = y1 - 1
                            e = e + dx

                            if e > 0:
                                x1 = x1 + 1
                                e = e + dy
            else:
                while x1 != x2:
                    pixelAllume(patternTest, x1, y1)
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

                        pixelAllume(patternTest, x1, y1)
                        while  x1 != x2:
                            pixelAllume(patternTest, x1, y1)
                            x1 = x1 - 1
                            e = e + dy

                            if e >= 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        pixelAllume(patternTest, x1, y1)
                        while y1 != y2:
                            pixelAllume(patternTest, x1, y1)
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

                        pixelAllume(patternTest, x1, y1)
                        while x1 != x2:
                            pixelAllume(patternTest, x1, y1)
                            x1 = x1 - 1
                            e = e - dy

                            if e >= 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        pixelAllume(patternTest, x1, y1)

                        while y1 != y2:
                            pixelAllume(patternTest, x1, y1)
                            y1 = y1 - 1
                            e = e - dx

                            if e >= 0:
                                x1 = x1 - 1
                                e = e + dy

            else:
                pixelAllume(patternTest, x1, y1)

                while x1 != x2:
                    x1 = x1 - 1
                    pixelAllume(patternTest, x1, y1)

    else:
        dy = y2 - y1
        if dy != 0:
            if dy > 0:
                while y1 != y2:
                    y1 = y1 + 1
                    pixelAllume(patternTest, x1, y1)

            else:
                while y1 != y2:
                    y1 = y1 - 1
                    pixelAllume(patternTest, x1, y1)

    for ligne in patternTest:
        print(ligne)

def doExercice(x1, y1, x2, y2):
    e = x2 - x1
    dx = 2*e
    dy = (y2 - y1)*2

    while x1 <= x2:
        pixelAllume(matrice, x1, y1)
        x1 = x1+1
        e = e-dy

        if e <=0:
            y1 = y1+1
            e = e + dx


    for ligne in patternTest:
        print(ligne)





def doExercice2(listPattern):
    solutionId = -1
    id = 0
    equal = False


    printMatrice(matrice)

    for pattern in listPattern:
        print("CHANGE PATTERN")
        posX = start_X
        posY = start_Y
        rayonPotentiel = 0
        test = True
        while posX >= 0 and posY < 23 and test:



            if not pixelAllume(pattern,posX, posY) and not equal:
                print("DEFINE")
                posY = posY + 1
                rayonPotentiel = rayonPotentiel + 1

            else:

                test = False

                print("START")
                x = 0
                y = rayonPotentiel

                d = 1-rayonPotentiel
                print('Rayon'+str(rayonPotentiel))

                cpt=0
                macthPixelCircle = True
                while y > x:
                    print("cpt : "+ str(cpt))

                    macthPixelCircle = macthPixelCircle
                    pixelAllume(pattern, x + start_X, y + start_Y)
                    pixelAllume(pattern, y+start_X, x+start_Y ) ;
                    pixelAllume(pattern, -x+start_X, y+start_Y ) ;
                    pixelAllume(pattern, -y+start_X, x+start_Y ) ;
                    pixelAllume(pattern, x+start_X, -y+start_Y ) ;
                    pixelAllume(pattern, y+start_X, -x+start_Y ) ;
                    pixelAllume(pattern, -x+start_X, -y+start_Y ) ;
                    pixelAllume(pattern, -y+start_X, -x+start_Y ) ;
                    cpt = cpt+1

                    if d >= 0:
                        d += 2*(x - y)+5
                        y = y-1
                    else:
                        d += 2 * x + 3


                    x +=1

                    print(d)
                    for ligne in patternTest:
                        print(ligne)


                posY = posY + 1
                if macthPixelCircle :
                    print("RESOK")

                    solutionId = id
                    equal = True


        id = id + 1



    return solutionId


def tailleCarre(hauteur):
    return 2 * hauteur + 1

def valabs(yStart,yEnd):
    if yEnd-yStart >= 0:
        return yEnd-yStart
    else :
        return yStart-yEnd

def printMatrice(matrice):

    for line in matrice:
        print(getLine(line, 0))


def getLine(line, pos):

    if pos < len(line):
        return str(line[pos]) + getLine(line, pos+1)

    else:
        return ""



def compareRayon(x,y,R):
    return x*x+y*y-R*R

    return 2 * hauteur + 1


def pixelAllume(matrice, x, y):

   # print("MATCH")
  #  print(x)
  #  print(y)

    patternTest[y][x] = 1
   # pixel = matrice[y][x]
  #  print("PIXEL")
 #   print(pixel)
 #   print(pixel[0])

 #   return pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0



def parcourtPatternX(posX, posY, endX, pattern):

    if posX == endX:
        return pixelAllume(pattern[posX][posY])
    else:
        return parcourtPatternX(posX + 1, posY, endX, pattern) and pixelAllume(pattern[posX][posY])


def parcourtPatternY(posX, posY, endY, pattern):

    if posY == endY:
        return pixelAllume(pattern[posX][posY])
    else:
        return parcourtPatternY(posX, posY + 1, endY, pattern) and pixelAllume(pattern[posX][posY])











### FIN  Algo crée par l'utilisateur


if __name__ == '__main__':
    print("EXO 2")
    print(testAlgo())
