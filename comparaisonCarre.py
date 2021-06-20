### Ajouté par l'API avant l'envoie à judge0


import cv2 as cv

from bibliothequePython.bib import Matrice, Pixel

option1 = cv.imread("./pattern/comparaisonCarre/option1.png")
option2 = cv.imread("./pattern/comparaisonCarre/option2.png")
option3 = cv.imread("./pattern/comparaisonCarre/option3.png")
option4 = cv.imread("./pattern/comparaisonCarre/option4.png")


listPatternInit = [option1, option2, option3, option4]
resultat = 1


def initExercice():
    newListPattern=[]

    for pattern in listPatternInit:
        newMatrice = Matrice(size_matrice)
        newMatrice.initContent(pattern)
        newListPattern.append(newMatrice)

    return newListPattern


###Donnée à l'utilisateur
size_matrice = 23
start_X = (size_matrice/2)-1
start_Y = (size_matrice/2)-1






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
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver le pattern de carrée
#
#
#Donnée: Liste d'images a traiter => listMatrice
#        le centre de la figure
#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à un carré



### Algo crée par l'utilisateur

def doExercice(listPattern):
    solutionId = -1
    id = 0
    equal = False

    for pattern in listPattern:

        posX = int(start_X)
        posY = int(start_Y)
        decalage = 0

        while posX >= 0 and posY >= 0 and not equal:
            decalage = decalage + 1
            posX = posX - 1
            posY = posY - 1

            if compatrePixel(posX, posY, pattern):

                taille_forme = tailleCarre(decalage)+1

                if parcourtPatternX(posX, posY, posX + taille_forme, pattern) and \
                        parcourtPatternX(posX, posY + taille_forme, posX + taille_forme, pattern) and \
                        parcourtPatternY(posX, posY, posY + taille_forme, pattern) and \
                        parcourtPatternY(posX + taille_forme, posY, posY + taille_forme, pattern):

                    equal = True
                    solutionId = id


                else:
                    posX = posX - 1
                    posY = posY - 1
                    decalage = decalage + 1

        id = id + 1

    return solutionId





def tailleCarre(hauteur):
    return 2 * hauteur + 1



def compatrePixel(x, y, matriceSource):

    pixelNone = Pixel(x, x, (255, 255, 255))

    return not matriceSource.getPixel(x, y).compare(pixelNone)


def parcourtPatternX(posX, posY, endX, pattern):

    if posX == endX:
        return compatrePixel(posX ,posY, pattern)
    else:
        if compatrePixel(posX ,posY, pattern):

            return parcourtPatternX(posX + 1, posY, endX, pattern)
        else:
            return False


def parcourtPatternY(posX, posY, endY, pattern):

    if posY == endY:

        return compatrePixel(posX ,posY, pattern)
    else:
        if compatrePixel(posX, posY, pattern):
            return parcourtPatternY(posX, posY + 1, endY, pattern)
        else:

            return False


### FIN  Algo crée par l'utilisateur


if __name__ == '__main__':
    print("EXO 2")
    print(testAlgo())
