### Ajouté par l'API avant l'envoie à judge0


import cv2 as cv

from lib.bib import Matrice, Opencv, Exercice, Pixel


def testAlgo(nameExercice, resultat):
    opencv = Opencv(nameExercice)
    opencv.getNumberImage()
    opencv.extractImage()
    opencv.initSizeImage()
    exercice = Exercice(resultat, nameExercice)
    listPatternInit = opencv.initExercice(opencv.sizeImage)
    pixelStartX = 0
    pixelStartY = 51

    size = opencv.sizeImage

    solution_user = doExercice(listPatternInit, pixelStartX, pixelStartY, size)
    return exercice.assertRes(solution_user, resultat)




###Donnée à l'utilisateur


### FIN Ajouté par l'API avant l'envoie à judge0


#Consigne:
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver la valeur d'une fonctionde kosh
#le résultat sera à donner sous forme de tableau
#


### Algo crée par l'utilisateur

def doExercice(listMatrice, pixelStartX, pixelStartY, size):
    res = []
    for matrice in listMatrice:
        pixelStartX=0
        t = find_t(matrice, pixelStartX, pixelStartY)

        k=0

        while size/3**k-t!=0 :
            k +=1
        res.append(k)

    return res

def find_t(matrice, pixelX, pixelY):

    notFind = True

    while pixelX < matrice.size and notFind:

        if pixelIsNull(pixelX, pixelY, matrice):
            notFind = False
        else:
            pixelX += 1

    return pixelX

def pixelIsNull(x, y, matriceSource):
    pixelNone = Pixel(x, y, (255, 255, 255))
    return matriceSource.getPixel(x, y).compare(pixelNone)

### FIN  Algo crée par l'utilisateur




if __name__ == '__main__':
    nameExercice = "comparaisonKosh"
    resultat = [1,2,0]

    print(testAlgo(nameExercice, resultat))

