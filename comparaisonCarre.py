### Ajouté par l'API avant l'envoie à judge0


import cv2 as cv




option1 = cv.imread("./pattern/comparaisonCarre/option1.png")
option2 = cv.imread("./pattern/comparaisonCarre/option2.png")
option3 = cv.imread("./pattern/comparaisonCarre/option3.png")
option4 = cv.imread("./pattern/comparaisonCarre/option4.png")




listPattern = [option1, option2, option3, option4]



# taille de l'image en pixel
size_picture = 23

# position de départ de la figure
start_X = (size_picture/2)-1
start_Y = (size_picture/2)-1

resultat = 1


def testAlgo():
    solution_user = doExercice(listPattern)

    return assertRes(solution_user, resultat)


def assertRes(solution_user, resultat):
    if solution_user == resultat:
        return "SUCCESS"
    else:
        return "ERROR"


### FIN Ajouté par l'API avant l'envoie à judge0


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

            if pixelIsUp(posX, posY, pattern):

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





### FIN  Algo crée par l'utilisateur

def tailleCarre(hauteur):
    return 2 * hauteur + 1


def pixelIsUp(x, y, matriceSource):
    return matriceSource[y][x][0] == 0 and matriceSource[y][x][1] == 0 and matriceSource[y][x][2] == 0


def parcourtPatternX(posX, posY, endX, pattern):

    if posX == endX:
        return pixelIsUp(posX ,posY, pattern)
    else:
        if pixelIsUp(posX ,posY, pattern):

            return parcourtPatternX(posX + 1, posY, endX, pattern)
        else:
            return False


def parcourtPatternY(posX, posY, endY, pattern):

    if posY == endY:

        return pixelIsUp(posX ,posY, pattern)
    else:
        if pixelIsUp(posX, posY, pattern):
            return parcourtPatternY(posX, posY + 1, endY, pattern)
        else:

            return False




if __name__ == '__main__':
    print("EXO 2")
    print(testAlgo())
