### Ajouté par l'API avant l'envoie à judge0

import cv2 as cv
import numpy
import math

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

patternTest3 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

patternTest4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]



patternTest5 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]



listPattern = [patternTest5]

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
        list_form = []
        listPixelSegment = []
        init_list_pixel_form = []
        listSegmentFormParcourtDroit = []

        currentLigne = 0
        currentColonne = 0
        pixelParcourtBalayageCurrent = (currentColonne,currentLigne)
        pixelParcourtBalayageEnd = (size_picture-1,size_picture-1)
        stop = False

        while pixelParcourtBalayageCurrent != pixelParcourtBalayageEnd and not stop:

            pixelFormNotExplore = False
            pixelStart = findStartFigure(pattern,pixelParcourtBalayageCurrent, list_form)
            pixelParcourtBalayageCurrent = pixelStart
       #     print(pixelParcourtBalayageCurrent)
            print(pixelStart)

            if pixelStart != pixelParcourtBalayageEnd:



                pixelInit = pixelStart


                if pixelStart != None:
                    count_line = 0

                listPixelPolygon = trouverPlusLongChemin(pixelStart, pattern, init_list_pixel_form, pixelStart, pixelStart)

                for pixel_current in listPixelPolygon:

                    if testLine(pixelStart, pixel_current, pattern, listPixelSegment):
                        listPixelSegment.append(pixel_current)

                    else:

                        count_line = count_line + 1
                        pixelStart = pixel_current
                        listSegmentFormParcourtDroit.append(listPixelSegment)
                        initPixel = listPixelSegment[len(listPixelSegment)-1]
                        listPixelSegment = []
                        listPixelSegment.append(initPixel)
                        listPixelSegment.append(pixelStart)





                count_line = count_line + 1
                listPixelSegment.append(pixelInit)
                listSegmentFormParcourtDroit.append(listPixelSegment)
                print(listSegmentFormParcourtDroit)
                list_form.append(listSegmentFormParcourtDroit)
                listSegmentFormParcourtDroit = []
                listPixelSegment=[]
             #   print("Segment")
            #    print(listSegmentFormParcourtDroit)
               # print(count_line)
                id = 1

                for first_segment in listSegmentFormParcourtDroit:

                    second_segment = listSegmentFormParcourtDroit[id]

                    angle = calculAngle(first_segment[0], first_segment[len(first_segment)-1], second_segment[len(second_segment)-1])

                 #   print(angle)

                    id = id+1
                    if id > (len(listSegmentFormParcourtDroit)-1):
                        id = 0

            else:
                stop = True




    return count_line


def calculNorme(dx, dy):
    return numpy.sqrt(dx * dx + dy * dy)

def calculProduitScalaire(dx1, dy1, dx2, dy2):
    #return 1/2 * (abs(calculNorme(dx1+dx2, dy1+dy2)*calculNorme(dx1+dx2, dy1+dy2)) - calculNorme(dx1, dy1)*calculNorme(dx1, dy1) - calculNorme(dx2, dy2)*calculNorme(dx2, dy2))
    return dx1*dx2 + dy1*dy2

def valAbs(a, b):

    res = b-a
    if res < 0:
        return -res
    else:
        return res


def calculAngle(pixelBegin, pixelMiddle, pixelEnd):

    dx1 = (pixelBegin[0]- pixelMiddle[0])
    dy1 = (pixelBegin[1]- pixelMiddle[1])
    dx2 = (pixelEnd[0]- pixelMiddle[0])
    dy2 = (pixelEnd[1]- pixelMiddle[1])

  #  print(pixelBegin)
  #  print(pixelMiddle)
  #  print(pixelEnd)

  #  print(dx1)
   # print(dy1)

 #   print(dx2)
#    print(dy2)

    produitScalaire = calculProduitScalaire(dx1, dy1, dx2, dy2)
    normeP1 = calculNorme(dx1, dy1)
    normeP2 = calculNorme(dx2, dy2)

    cos_angle = round(produitScalaire / (normeP1*normeP2),3)

   # print("cos_angle " + str(cos_angle))
 #   print("produitScalaire " + str(produitScalaire))
   # print("normeP1 " + str(normeP1))
   # print("normeP2 " + str(normeP2))

    radiant = math.acos(cos_angle)
   # print("cos_angle " + str(radiant))

    angle_degree = math.degrees(radiant)

    return round(angle_degree, 3)




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

   # switcher = {
   # pattern[y][x + 1] == 1 and (x + 1, y) not in cheminCourant:
   #     lisPotentielPixelNext.append((x + 1, y)),

   # pattern[y + 1][x] == 1 and (x, y + 1) not in cheminCourant:
   #     lisPotentielPixelNext.append((x, y + 1)),

   # pattern[y][x - 1] == 1 and (x - 1, y) not in cheminCourant:
   #     lisPotentielPixelNext.append((x - 1, y)),

   # pattern[y - 1][x] == 1 and (x, y - 1) not in cheminCourant:
   #     lisPotentielPixelNext.append((x, y - 1)),

    #pattern[y + 1][x + 1] == 1 and (x + 1, y + 1) not in cheminCourant:
    #    lisPotentielPixelNext.append((x + 1, y + 1)),

    #pattern[y - 1][x - 1] == 1 and (x - 1, y - 1) not in cheminCourant:
     #   lisPotentielPixelNext.append((x - 1, y - 1)),

    #pattern[y + 1][x - 1] == 1 and (x - 1, y + 1) not in cheminCourant:
    #    lisPotentielPixelNext.append((x - 1, y + 1)),

    #pattern[y - 1][x + 1] == 1 and (x + 1, y - 1) not in cheminCourant:
    #    lisPotentielPixelNext.append((x + 1, y - 1))
    #}

    #switcher.get(True)

    return lisPotentielPixelNext









def marquePixel(listPixels, pattern, currentpixel):
    try:
        listPixels.append(currentpixel)
       # pattern[currentpixel[1]][currentpixel[0]] = -1
    except:
        print("TEST")



def findStartFigure(pattern, pixelstart, list_form):

    ligne = pixelstart[1]
    colonne = pixelstart[0]



    pixelStart = None
    while ligne < size_picture:
        while colonne < size_picture:

            if pixelAllumeInit(pattern,colonne, ligne):
                pixelStart = (colonne, ligne)
                pixelFormNotExplore = True

                for form in list_form:
                    for segment in form:
                        if pixelStart in segment:
                            pixelFormNotExplore = False



                if pixelFormNotExplore:
                    return pixelStart





            colonne = colonne +1

        colonne = 0
        ligne = ligne +1


    return (size_picture-1, size_picture-1)

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
