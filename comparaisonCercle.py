### Ajouté par l'API avant l'envoie à judge0

import cv2 as cv
import numpy

from bibliothequePython.bib import Matrice, Pixel

option1 = cv.imread("./pattern/comparaisonCercle/option1.png")
option2 = cv.imread("./pattern/comparaisonCercle/option2.png")
option3 = cv.imread("./pattern/comparaisonCercle/option3.png")
option4 = cv.imread("./pattern/comparaisonCercle/option4.png")




listPatternInit = [option1, option2, option3, option4]
resultat = 3

#donnée à l'utilisateur
size_matrice = 23
start_X = 11
start_Y = 11

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
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver le pattern de cercle
#l'algorithme a utiliser est l'algorithme de tracé de cercle de bresenham
#
#Donnée: Liste d'images a traiter => listMatrice
#        le centre de la figure
#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à un cercle de bresenham



### Algo crée par l'utilisateur
def doExercice(listPattern):

    solutionId = 0

    for pattern in listPattern:
        r = 0

        pattern.toStringPixel()
        while r <= 11:

            x = 0
            y = int(r)
            d = 5 - 4.0*r

            res = pixelIsNull(x + start_X, y + start_Y, pattern) and \
            pixelIsNull(y + start_X, x + start_Y, pattern) and \
            pixelIsNull(-x + start_X, y + start_Y, pattern) and \
            pixelIsNull(-y + start_X, x + start_Y, pattern) and \
            pixelIsNull(x + start_X, -y + start_Y, pattern) and \
            pixelIsNull(y + start_X, -x + start_Y, pattern) and \
            pixelIsNull(-x + start_X, -y + start_Y, pattern) and \
            pixelIsNull(-y + start_X, -x + start_Y, pattern)

            print("res init")
            print(res)


            while (y > x):

                if  d > 0:
                    y = y-1
                    d = d - 8.0*y

                x = x + 1
                d = d + 8.0 * x + 4.0
                res = res and pixelIsNull(x + start_X, y + start_Y, pattern) and \
                pixelIsNull(y + start_X, x + start_Y, pattern) and \
                pixelIsNull(-x + start_X, y + start_Y, pattern) and \
                pixelIsNull(-y + start_X, x + start_Y, pattern) and \
                pixelIsNull(x + start_X, -y + start_Y, pattern) and \
                pixelIsNull(y + start_X, -x + start_Y, pattern) and \
                pixelIsNull(-x + start_X, -y + start_Y, pattern) and \
                pixelIsNull(-y + start_X, -x + start_Y, pattern)
                print("res clac")
                print(res)
                print(r)

            r +=1

        if res == True:
            return solutionId

        solutionId += 1



def pixelIsNull(x, y, matriceSource):

    pixelNone = Pixel(x, x, (255, 255, 255))
    print("PIXEL")

    print(matriceSource.getPixel(x, y).getX())
    print(matriceSource.getPixel(x, y).getY())

    return not matriceSource.getPixel(x, y).compare(pixelNone)






### FIN  Algo crée par l'utilisateur


if __name__ == '__main__':
    print("EXO 2")
    print(testAlgo())
