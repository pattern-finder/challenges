### Ajouté par l'API avant l'envoie à judge0

import cv2 as cv
import numpy

##ALGO:
#Etape 1: trouver le sommet de la forme
#Etape 2: trouver et sauvegarder le plus long chemin de pixel sans passer 2 fois par le même pixel (a l'exception du premier pixel qui est le dernier)
#Etape 3: Parcourir le chemin de pixel en appliquant l'algo de trace de ligne et déterminer quel pixel appartient à quel ligne
#Etape 4: Dès qu'un pixel n'appartient plus à la ligne, on change le point de départ de la ligne et on incrémente le compteur de ligne
#



patternTest = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

patternTest2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
listPattern = [patternTest, patternTest2]

# taille de l'image en pixel
size_picture = 17





resultat = 4


def testAlgo():
    solution_user = doExercice()

    return assertRes(solution_user, resultat)


def assertRes(solution_user, resultat):
    if solution_user == resultat:
        return "SUCCESS"
    else:
        return "ERROR"


### FIN Ajouté par l'API avant l'envoie à judge0


### Algo crée par l'utilisateur



def doExercice():


    for pattern in listPattern:
        count_line = 0

        listPixelSegment = []
        init_list_pixel_form = []

        pixelStart = findStartFigure(pattern)

        if pixelStart != None:
            count_line = 1

        listPixelForme = trouverPlusLongChemin(pixelStart, pattern, init_list_pixel_form, pixelStart, pixelStart)
        listPixelForme.append(pixelStart)

        print(listPixelForme)
        for pixel_current in listPixelForme:

            if testLine(pixelStart, pixel_current, pattern, listPixelSegment):
                listPixelSegment.append(pixel_current)

            else:
                count_line = count_line + 1
                pixelStart = pixel_current
                listPixelSegment = []
                listPixelSegment.append(pixelStart)

        print(count_line)

    return count_line


def trouverPlusLongChemin(pixelCurent, pattern, cheminCourant, pixelStart, insertPixel):

    cheminCourant = cheminCourant + [insertPixel]
    plusLongChemin = cheminCourant
    pixelsSuivant = trouverPixelSuivant(pixelCurent, pattern, cheminCourant)


    for pixel in pixelsSuivant:
        chemintmp = cheminCourant

        if pixel not in cheminCourant:

            nouveauChemin = trouverPlusLongChemin(pixel, pattern, chemintmp, pixelStart, pixel)

            if nouveauChemin != None:


                if len(nouveauChemin) > len(plusLongChemin):
                    plusLongChemin = nouveauChemin

    return plusLongChemin



def trouverPixelSuivant(pixelStart, pattern, cheminCourant):
    x = pixelStart[0]
    y = pixelStart[1]

    lisPotentielPixelNext = []

    if pattern[y][x + 1] == 1 and (x + 1, y) not in cheminCourant:
        lisPotentielPixelNext.append((x + 1, y))

    if pattern[y + 1][x] == 1 and (x, y + 1) not in cheminCourant:
        lisPotentielPixelNext.append((x, y + 1))

    if pattern[y][x - 1] == 1 and (x - 1, y) not in cheminCourant:
        lisPotentielPixelNext.append((x - 1, y))

    if pattern[y - 1][x] == 1 and (x, y - 1) not in cheminCourant:
        lisPotentielPixelNext.append((x, y - 1))

    if pattern[y + 1][x + 1] == 1 and (x + 1, y + 1) not in cheminCourant:
        lisPotentielPixelNext.append((x + 1, y + 1))

    if pattern[y - 1][x - 1] == 1 and (x - 1, y - 1) not in cheminCourant:
        lisPotentielPixelNext.append((x - 1, y - 1))

    if pattern[y + 1][x - 1] == 1 and (x - 1, y + 1) not in cheminCourant:
        lisPotentielPixelNext.append((x - 1, y + 1))

    if pattern[y - 1][x + 1] == 1 and (x + 1, y - 1) not in cheminCourant:
        lisPotentielPixelNext.append((x + 1, y - 1))


    return lisPotentielPixelNext









def marquePixel(listPixels, pattern, currentpixel):
    try:
        listPixels.append(currentpixel)
       # pattern[currentpixel[1]][currentpixel[0]] = -1
    except:
        print("TEST")



def findStartFigure(pattern):

    ligne = 0
    colonne = 0

    while ligne < size_picture:
        while colonne < size_picture:

            if pixelAllumeInit(pattern,colonne, ligne):
                return (colonne, ligne)

            colonne = colonne +1

        colonne = 0
        ligne = ligne +1



def testLine(pixelStart, currentPixel, pattern, listPixels):
    x1 = pixelStart[0]
    y1 = pixelStart[1]

    x2 = currentPixel[0]
    y2 = currentPixel[1]

    isLine = True

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

                        isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                        while  x1 != x2:
                            isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                            x1 = x1 + 1
                            e = e - dy

                            if e < 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                        while  y1 != y2:
                            isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
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

                        isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                        while x1 != x2:
                            isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                            x1 = x1 + 1
                            e = e + dy

                            if e < 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                        while y1 != y2:
                            isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                            y1 = y1 - 1
                            e = e + dx

                            if e > 0:
                                x1 = x1 + 1
                                e = e + dy
            else:
                while x1 != x2:
                    isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
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

                        isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                        while  x1 != x2:
                            isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                            x1 = x1 - 1
                            e = e + dy

                            if e >= 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                        while y1 != y2:
                            isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
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

                        isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                        while x1 != x2:
                            isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                            x1 = x1 - 1
                            e = e - dy

                            if e >= 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)

                        while y1 != y2:
                            isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)
                            y1 = y1 - 1
                            e = e - dx

                            if e >= 0:
                                x1 = x1 - 1
                                e = e + dy

            else:
                isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)

                while x1 != x2:
                    x1 = x1 - 1
                    isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)

    else:
        dy = y2 - y1
        if dy != 0:
            if dy > 0:
                while y1 != y2:
                    y1 = y1 + 1
                    isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)

            else:
                while y1 != y2:
                    y1 = y1 - 1
                    isLine = isLine and pixelAllume(pattern, x1, y1, listPixels)


    return isLine





def printMatrice(matrice):

    for line in matrice:
        print(getLine(line, 0))


def getLine(line, pos):

    if pos < len(line):
        return str(line[pos]) + getLine(line, pos+1)

    else:
        return ""





def pixelAllumeInit(matrice, x, y):

    return matrice[y][x] == 1

def pixelAllume(matrice, x, y, listPixels):


    return matrice[y][x] == 1
    #return not ((x,y) in listPixels)
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
