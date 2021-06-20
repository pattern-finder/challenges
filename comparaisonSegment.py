### Ajouté par l'API avant l'envoie à judge0

import cv2 as cv
import matplotlib
import numpy

from bibliothequePython.bib import Matrice, Pixel

option1 = cv.imread("pattern/comparaisonSegment/option1.png")
option2 = cv.imread("pattern/comparaisonSegment/option2.png")
option3 = cv.imread("pattern/comparaisonSegment/option3.png")
option4 = cv.imread("pattern/comparaisonSegment/option4.png")


listPatternInit = [option1, option2, option3, option4]

resultat = 0




# Donnée à l'utilisateur
size_matrice = 23
listPosStart = [(13, 4), (13, 4), (13, 4), (16, 7)]
listPosEnd = [(9, 17), (9, 17), (9, 17), (9, 17)]

def initExercice():
    newListPattern=[]

    for pattern in listPatternInit:
        newMatrice = Matrice(size_matrice)
        newMatrice.initContent(pattern)
        newListPattern.append(newMatrice)

    return newListPattern


def testAlgo():
    listMatrice = initExercice()

    solution_user = doExercice(listMatrice)

    return assertRes(solution_user, resultat)


def assertRes(solution_user, resultat):
    if solution_user == resultat:
        return "SUCCESS"
    else:
        return "ERROR"


### FIN Ajouté par l'API avant l'envoie à judge0

#Consigne: Vous disposez d'une liste d'image.
#Implémentez la fonction doExerciceBalayage afin de créer un algoritme capable de trouver le pattern de ligne tracé par l'algo de bresenham
#
#
#Donnée: Liste d'images a traiter => listMatrice
#        Les 2 pixels aux extrémité de la figure
#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à une ligne tracé avec l'algo de bresenham



### Algo crée par l'utilisateur

def doExercice(listPattern):

    i=0

    for pattern in listPattern:

        pixelStart = listPosStart[i]
        pixelStop = listPosEnd[i]

        res = testLine(pixelStart[0], pixelStart[1], pixelStop[0], pixelStop[1], pattern)

        if res:
            return i

        i +=1



def testLine(x1, y1, x2, y2, patternTest):

    res = True
    dx = x2 - x1
    if dx != 0:
        if dx > 0:
            dy = y2 - y1
            if dy != 0:

                if dy > 0:

                    if dx >= dy:
                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        res = res and pixelIsNull(x1, y1, patternTest)
                        while x1 != x2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            x1 = x1 + 1
                            e = e - dy

                            if e < 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        res = res and pixelIsNull(x1, y1, patternTest)
                        while y1 != y2:
                            res = res and pixelIsNull(x1, y1, patternTest)
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

                        res = res and pixelIsNull(x1, y1, patternTest)
                        while x1 != x2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            x1 = x1 + 1
                            e = e + dy

                            if e < 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        res = res and pixelIsNull(x1, y1, patternTest)
                        while y1 != y2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            y1 = y1 - 1
                            e = e + dx

                            if e > 0:
                                x1 = x1 + 1
                                e = e + dy
            else:
                while x1 != x2:
                    res = res and pixelIsNull(x1, y1, patternTest)
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

                        res = res and pixelIsNull(x1, y1, patternTest)

                        while x1 != x2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            x1 = x1 - 1
                            e = e + dy

                            if e >= 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2



                        res = res and pixelIsNull(x1, y1, patternTest)

                        while y1 != y2:
                            print("oko")
                            print(pixelIsNull(x1, y1, patternTest))
                            res = res and pixelIsNull(x1, y1, patternTest)

                            y1 = y1 + 1
                            e = e + dx

                            if e <= 0:
                                x1 = x1 - 1
                                e = e + dy
                        print("ENDDDDDDDDDDDDDDDDDDDD")
                else:
                    # 5eme octant
                    if dx <= dy:
                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        res = res and pixelIsNull(x1, y1, patternTest)
                        while x1 != x2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            x1 = x1 - 1
                            e = e - dy

                            if e >= 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        res = res and pixelIsNull(x1, y1, patternTest)

                        while y1 != y2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            y1 = y1 - 1
                            e = e - dx

                            if e >= 0:
                                x1 = x1 - 1
                                e = e + dy

            else:
                res = res and pixelIsNull(x1, y1, patternTest)

                while x1 != x2:
                    x1 = x1 - 1
                    res = res and pixelIsNull(x1, y1, patternTest)

    else:
        dy = y2 - y1
        if dy != 0:
            if dy > 0:
                while y1 != y2:
                    y1 = y1 + 1
                    res = res and pixelIsNull(x1, y1, patternTest)

            else:
                while y1 != y2:
                    y1 = y1 - 1
                    res = res and pixelIsNull(x1, y1, patternTest)


    return res

def pixelIsNull(x, y, matriceSource):

    pixelNone = Pixel(x, y, (255, 255, 255))
    print("PIXEL")

    print(matriceSource.getPixel(x, y).getX())
    print(matriceSource.getPixel(x, y).getY())

    return not matriceSource.getPixel(x, y).compare(pixelNone)









### FIN  Algo crée par l'utilisateur


if __name__ == '__main__':
    print("EXO 2")
    print(testAlgo())
