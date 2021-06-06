
### Ajouté par l'API avant l'envoie à judge0


class Pixel:
    def __init__(self ,red ,green, blue):
        self.red =red
        self.green =green
        self.blue =blue


    def equal(self, other):
        if isinstance(other, self.__class__):
            return self.red == other.red and \
                   self.green == other.green and \
                   self.blue == other.blue
        else:
            return False





matriceInputToFind = [ [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(255 ,255 ,255), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)]
                       ]


matriceInputPattern1 = [ [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(255 ,255 ,255), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(255 ,255 ,255)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)]
                       ]

matriceInputPattern2 = [ [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(255 ,255 ,255), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)]
                       ]

matriceInputPattern3 = [ [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(255 ,255 ,255), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)],
                       [Pixel(0 ,0 ,0), Pixel(0 ,0 ,0), Pixel(0 ,0 ,0),       Pixel(0 ,0 ,0), Pixel(0 ,0 ,0)]
                       ]

listPattern = [matriceInputPattern1, matriceInputPattern2, matriceInputPattern3]
resultat = 2


def testAlgo():
    solution_user = doExercice(listPattern, matriceInputToFind)

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

    for pattern in listPattern:
        ligneInputPattern = 0

        equal = True
        solutionId = -1

        for lignePixel in pattern:
            colonneInputPattern = 0
            for pixel in lignePixel:

                if not pixel.equal(matriceInputToFind[ligneInputPattern][colonneInputPattern]):
                    equal = False

                colonneInputPattern = colonneInputPattern +1

            ligneInputPattern = ligneInputPattern +1

        if equal :
            solutionId = currentId
        currentId = currentId + 1

    return solutionId


### FIN  Algo crée par l'utilisateur



if __name__ == '__main__':

    print(testAlgo())
