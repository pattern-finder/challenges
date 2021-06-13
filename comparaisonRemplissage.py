### Ajouté par l'API avant l'envoie à judge0
#JEPSEN

import cv2 as cv




option1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

option2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

]


listPattern = [option1, option2]



# taille de l'image en pixel
size_picture = 17

# position de départ de la figure
start_X = 8
start_Y = 8

resultat = 1


def testAlgo():
    solution_user = remplissageBalayage(listPattern)

    return assertRes(solution_user, resultat)


def assertRes(solution_user, resultat):
    if solution_user == resultat:
        return "SUCCESS"
    else:
        return "ERROR"


### FIN Ajouté par l'API avant l'envoie à judge0

###Donnée à l'utilisateur
SIZE_SCREEN = 17


### Algo crée par l'utilisateur

def remplissageDiffusion(listPattern):

    for pattern in listPattern:
        decalePixel(start_X, start_Y, pattern)

        for ligne in pattern:
            print(ligne)
    return 0

def remplissageBalayage(listPattern):

    for pattern in listPattern:
        isInForm = False
        savePixelInFormMatrice = []

        print("")

        for ligne in pattern:
            print(ligne)

        print("")

        ligne = 0
        colonne = 0
        isOnFigure = False

        while ligne < SIZE_SCREEN-1:
            savePixelInFormLigne = []

            while colonne < SIZE_SCREEN-1:

                if pattern[colonne][ligne] == 1:
                    isInForm = not isInForm
                    isOnFigure = True

                else:
                    isOnFigure = False

                if isInForm and not isOnFigure:
                    savePixelInFormLigne.append((ligne,colonne))

                else:
                    print(savePixelInFormLigne)

                    for pixel in savePixelInFormLigne:
                        savePixelInFormMatrice.append(pixel)

                    savePixelInFormLigne = []

                colonne = colonne + 1

            colonne = 0
            ligne = ligne + 1


        for pixel in savePixelInFormMatrice:
            x = pixel[0]
            y = pixel[1]

            pattern[y][x] = 1

        for ligne in pattern:
            print(ligne)



    return 0


def decalePixel(x, y, pattern):
    if pattern[x][y] == 0:
        pattern[x][y] = 1

        decalePixel(x+1,y,pattern)
        decalePixel(x,y+1,pattern)
        decalePixel(x-1,y,pattern)
        decalePixel(x,y-1,pattern)






### FIN  Algo crée par l'utilisateur




if __name__ == '__main__':
    print("EXO 2")
    print(testAlgo())
