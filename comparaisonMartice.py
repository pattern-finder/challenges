
### Ajouté par l'API avant l'envoie à judge0

from bibliothequePython import bib

import cv2 as cv

from bibliothequePython.bib import Matrice

result = cv.imread("./pattern/comparaisonMatrice/result.png")
option1 = cv.imread("./pattern/comparaisonMatrice/option1.png")
option2 = cv.imread("./pattern/comparaisonMatrice/option2.png")
option3 = cv.imread("./pattern/comparaisonMatrice/option3.png")
option4 = cv.imread("./pattern/comparaisonMatrice/option4.png")
option5 = cv.imread("./pattern/comparaisonMatrice/option5.png")





listPatternInit = [option1, option2, option3, option4,option5 ]
resultat = 1

size_matrice = 23

def initExercice():
    newListPattern=[]

    for pattern in listPatternInit:
        newMatrice = Matrice(size_matrice)
        newMatrice.initContent(pattern)
        newListPattern.append(newMatrice)


    return newListPattern




def testAlgo():

    listMatrice = initExercice()
    matrice_result = Matrice(size_matrice)
    matrice_result.initContent(result)

    solution_user = doExercice(listMatrice, matrice_result)

    return assertRes(solution_user ,resultat)


def assertRes(solution_user ,resultat):
    if solution_user == resultat:
        return "SUCCESS"
    else:
        return "ERROR"


### FIN Ajouté par l'API avant l'envoie à judge0


#Consigne: Vous disposez d'une image résultat et d'une liste d'image.
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver l'image d'entrée dans la liste d'image de sortie
#
#
#Donnée: Image a trouver => matrice_result
#        Liste d'images a traiter => listMatrice

#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...)


### Algo crée par l'utilisateur

def doExercice(listMatrice, matriceInputToFind):
    currentId = 0
    solutionId = -1

    for matrice in listMatrice:
        ligneInputPattern = 0

        equal = True
        print("")
        matrice.toStringPixel()

        for lignePixel in matrice.getMatriceContent():
            colonneInputPattern = 0

            for pixel in lignePixel:

                if not compatrePixel(colonneInputPattern, ligneInputPattern, matrice, matriceInputToFind):
                    equal = False

                colonneInputPattern = colonneInputPattern +1

            ligneInputPattern = ligneInputPattern +1

        if equal :
            solutionId = currentId

        currentId = currentId + 1

    return solutionId


def compatrePixel(x, y, matriceSource, matriceCible):

    return matriceSource.getPixel(x, y).compare(matriceCible.getPixel(x, y)) and\
           matriceSource.getPixel(x, y).compare(matriceCible.getPixel(x, y)) and \
           matriceSource.getPixel(x, y).compare(matriceCible.getPixel(x, y))


### FIN  Algo crée par l'utilisateur




if __name__ == '__main__':
    print("EXO 1")
    print(testAlgo())
