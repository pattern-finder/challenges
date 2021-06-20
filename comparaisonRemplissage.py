### Ajouté par l'API avant l'envoie à judge0
#JEPSEN

import cv2 as cv

from bibliothequePython.bib import Matrice, Pixel

option1 = cv.imread("pattern/comparaisonRemplissage/option1.png")
option2 = cv.imread("pattern/comparaisonRemplissage/option2.png")
option3 = cv.imread("pattern/comparaisonRemplissage/option3.png")




listPatternInit = [option1, option2, option3]
resultat = 2

# taille de l'image en pixel
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

    solution_user = remplissageBalayage(listMatrice)

    return assertRes(solution_user, resultat)


def assertRes(solution_user, resultat):
    if solution_user == resultat:
        return "SUCCESS"
    else:
        return "ERROR"


### FIN Ajouté par l'API avant l'envoie à judge0

#Consigne: Vous disposez d'une liste d'image.
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver le pattern remplie (dont tous les pixels intèriueurs sont noir)
#
#
#Donnée: Liste d'images a traiter => listMatrice

#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à une forme pleine


### Algo crée par l'utilisateur

def remplissageDiffusion(listPattern):
    idSolution = -1

    for pattern in listPattern:
        pattern.toStringPixel()
        listPixelContent = []
        res = decalePixel(start_X, start_Y, pattern, listPixelContent)
        if res:
            return idSolution
        idSolution +=1

    return -1


def remplissageBalayage(listPattern):
    idSolution = 0

    for pattern in listPattern:

        ligne = 0
        colonne = 0
        echec = False

        while ligne < size_matrice-1 and not echec:

            cpt_bordure = 0
            inForm = False

            while colonne < size_matrice-1 and not echec:

                if cpt_bordure > 2 and cpt_bordure != 0:
                    echec = True


                if pixelIsNotNull(colonne, ligne, pattern):


                    if not inForm:
                        print("PIXEL enter IN")
                        print(colonne)
                        print(ligne)

                        inForm = True
                        cpt_bordure += 1

                else:

                    if inForm:
                        print("PIXEL enter OUT")
                        print(colonne)
                        print(ligne)

                        inForm = False
                        cpt_bordure += 1



                colonne = colonne + 1

            colonne = 0
            ligne = ligne + 1



        print("idSolution" + str(idSolution))
        print(cpt_bordure)

        if not echec:
            return idSolution


        idSolution +=1


    return 0


def decalePixel(x, y, pattern, listPixelForme):

        if x <= size_matrice-1 and y<= size_matrice-1:

            if (x, y) not in listPixelForme :

                if pixelIsNotNull(x,y,pattern):


                    listPixelForme.append((x, y))

                    return decalePixel(x+1,y,pattern, listPixelForme) and \
                    decalePixel(x,y+1,pattern, listPixelForme) and \
                    decalePixel(x-1,y,pattern, listPixelForme) and \
                    decalePixel(x,y-1,pattern, listPixelForme)

                else:
                    return False

            else:
                return True

        else :
            return False


def pixelIsNotNull(x, y, matriceSource):

    pixelNone = Pixel(x, x, (255, 255, 255))

    return not matriceSource.getPixel(x, y).compare(pixelNone)




### FIN  Algo crée par l'utilisateur




if __name__ == '__main__':
    print("EXO 2")
    print(testAlgo())
