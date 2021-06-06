
### Ajouté par l'API avant l'envoie à judge0

import cv2 as cv




result = cv.imread("./pattern/comparaisonMatrice/result.png")
option1 = cv.imread("./pattern/comparaisonMatrice/option1.png")
option2 = cv.imread("./pattern/comparaisonMatrice/option2.png")
option3 = cv.imread("./pattern/comparaisonMatrice/option3.png")
option4 = cv.imread("./pattern/comparaisonMatrice/option4.png")
option5 = cv.imread("./pattern/comparaisonMatrice/option5.png")




listPattern = [option1, option2, option3, option4,option5 ]
resultat = 1


def testAlgo():
    solution_user = doExercice(listPattern, result)

    return assertRes(solution_user ,resultat)


def assertRes(solution_user ,resultat):
    if solution_user == resultat:
        return "SUCCESS"
    else:
        return "ERROR"


### FIN Ajouté par l'API avant l'envoie à judge0





### Algo crée par l'utilisateur

def doExercice(listPattern, matriceInputToFind):
    currentId = 0
    solutionId = -1

    for pattern in listPattern:
        ligneInputPattern = 0

        equal = True

        for lignePixel in pattern:
            colonneInputPattern = 0
            for pixel in lignePixel:

                if not compatrePixel(colonneInputPattern, ligneInputPattern, pattern, matriceInputToFind):
                    equal = False

                colonneInputPattern = colonneInputPattern +1

            ligneInputPattern = ligneInputPattern +1

        if equal :
            solutionId = currentId

        currentId = currentId + 1

    return solutionId


### FIN  Algo crée par l'utilisateur


def compatrePixel(x, y, matriceSource, matriceCible):

    return matriceSource[y][x][0] == matriceCible[y][x][0] and matriceSource[y][x][1] == matriceCible[y][x][1] and matriceSource[y][x][2] == matriceCible[y][x][2]


if __name__ == '__main__':
    print("EXO 1")
    print(testAlgo())
