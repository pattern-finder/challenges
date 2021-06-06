### Ajouté par l'API avant l'envoie à judge0

import cv2 as cv
import matplotlib
import numpy



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
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

listPattern = [patternTest2]

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

        listPixels = []
        count = 0
        pixelStart = findStartFigure(pattern)
        pixelStartLine = pixelStart
       # listPixels.append(pixelStart)




        #pixelStartLine = pixelStart
        #newPixel = findNext(pattern, pixelStart, (-1,-1), listPixels, pixelStart)

       # currentpixel = newPixel

      #  listPixels.append(currentpixel)
        #testLine(pixelStartLine[0], pixelStartLine[1], currentpixel[0], currentpixel[1], pattern, listPixels)

        stop = False
        while not stop:

            currentpixel = pixelStart

            l1 = []
            l2 = []
            l1.append(currentpixel)
            l2.append(currentpixel)

            newPixels = findNextPixel(currentpixel, pattern, listPixels, pixelStartLine, l1, l2)
            print(len(newPixels))
            print("test "+ str(newPixels))

            currentpixel = newPixels[len(newPixels)-1]


            print("newPixel " + str(currentpixel))



            print("countFLAG")
            count = count +1
            pixelStartLine = currentpixel

            for pixel in newPixels:
                listPixels.append(pixel)

            if pixelStart[0] == currentpixel[0] and pixelStart[1] == currentpixel[1]:
                stop = True
                print("stop")
                print(pixelStart)
                print(currentpixel)

                count = count +1


    print("count")

    print(count)
    return count

def findNext(pattern, pixel, lastPixel,listPixels, pixelStart):

    x = pixel[0]
    y = pixel[1]

    lisPotentielPixelNext = []

    if pattern[y][x + 1] == 1 and ((x + 1, y) not in listPixels or (x + 1, y) == pixelStart and len(listPixels) > 2):
        lisPotentielPixelNext.append((x + 1, y))

    if pattern[y + 1][x] == 1 and ((x, y + 1) not in listPixels or (x, y + 1) == pixelStart and len(listPixels) > 2):
        lisPotentielPixelNext.append((x, y + 1))

    if pattern[y][x - 1] == 1 and ((x - 1, y) not in listPixels or (x - 1, y) == pixelStart and len(listPixels) > 2):
        lisPotentielPixelNext.append((x - 1, y))

    if pattern[y - 1][x] == 1 and ((x, y - 1) not in listPixels or (x, y - 1) == pixelStart and len(listPixels) > 2):
        lisPotentielPixelNext.append((x, y - 1))

    if pattern[y + 1][x + 1] == 1 and (
            (x + 1, y + 1) not in listPixels or (x + 1, y + 1) == pixelStart and len(listPixels) > 2):
        lisPotentielPixelNext.append((x + 1, y + 1))

    if pattern[y - 1][x - 1] == 1 and (
            (x - 1, y - 1) not in listPixels or (x - 1, y - 1) == pixelStart and len(listPixels) > 2):
        lisPotentielPixelNext.append((x - 1, y - 1))

    if pattern[y + 1][x - 1] == 1 and (
            (x - 1, y + 1) not in listPixels or (x - 1, y + 1) == pixelStart and len(listPixels) > 2):
        lisPotentielPixelNext.append((x - 1, y + 1))

    if pattern[y - 1][x + 1] == 1 and (
            (x + 1, y - 1) not in listPixels or (x + 1, y - 1) == pixelStart and len(listPixels) > 2):
        lisPotentielPixelNext.append((x + 1, y - 1))


    for pixel in lisPotentielPixelNext:
        if testLine(pixelStart[0], pixelStart[1], pixel[0], pixel[1], pattern, listPixels):
            return (pixel[0], pixel[1])


    return lisPotentielPixelNext[0]



def findNextPixel(pixel, pattern, listPixels, pixelStart, currentListPixel, resListPixel):
    lisPotentielPixelNext = []
    x = pixel[0]
    y = pixel[1]



    if pattern[y][x + 1] == 1 and ((x + 1, y) not in currentListPixel or (x + 1, y) == pixelStart and len(currentListPixel) > 2):
        lisPotentielPixelNext.append((x + 1, y))

    if pattern[y + 1][x] == 1 and ((x, y + 1) not in currentListPixel or (x, y + 1) == pixelStart and len(currentListPixel) > 2):
        lisPotentielPixelNext.append((x, y + 1))

    if pattern[y][x - 1] == 1 and ((x - 1, y) not in currentListPixel or (x - 1, y) == pixelStart and len(currentListPixel) > 2):
        lisPotentielPixelNext.append((x - 1, y))

    if pattern[y - 1][x] == 1 and ((x, y - 1) not in currentListPixel or (x, y - 1) == pixelStart and len(currentListPixel) > 2):
        lisPotentielPixelNext.append((x, y - 1))

    if pattern[y + 1][x + 1] == 1 and (
            (x + 1, y + 1) not in currentListPixel or (x + 1, y + 1) == pixelStart and len(currentListPixel) > 2):
        lisPotentielPixelNext.append((x + 1, y + 1))

    if pattern[y - 1][x - 1] == 1 and (
            (x - 1, y - 1) not in currentListPixel or (x - 1, y - 1) == pixelStart and len(currentListPixel) > 2):
        lisPotentielPixelNext.append((x - 1, y - 1))

    if pattern[y + 1][x - 1] == 1 and (
            (x - 1, y + 1) not in currentListPixel or (x - 1, y + 1) == pixelStart and len(currentListPixel) > 2):
        lisPotentielPixelNext.append((x - 1, y + 1))

    if pattern[y - 1][x + 1] == 1 and (
            (x + 1, y - 1) not in currentListPixel or (x + 1, y - 1) == pixelStart and len(currentListPixel) > 2):
        lisPotentielPixelNext.append((x + 1, y - 1))


    resListPixelMax = []

    print("lisPotentielPixelNext " + str(lisPotentielPixelNext))
    #print("resListPixelMax " + str(resListPixelMax))

    for pixel in lisPotentielPixelNext:

       # print("x1" + str(pixel[0]))
       # print("x2" + str(pixel[1]))

        if testLine(pixelStart[0], pixelStart[1], pixel[0], pixel[1], pattern, listPixels) and pixel not in currentListPixel:
            print("testLine")
            print("pixel" + str(pixel))
            print("ligne" + str(lisPotentielPixelNext))

            currentListPixel.append(pixel)
            resListPixel = findNextPixel(pixel, pattern, listPixels, pixelStart, currentListPixel, resListPixel)

            if len(resListPixelMax) < len(currentListPixel):
                resListPixelMax = currentListPixel



    return resListPixelMax





  #  switcher = {
    #    pattern[y][x+1] == 1 and ((x+1,y) not in listPixels or (x+1,y) == pixelStart and len(listPixels) > 2) : (x+1, y),
     #   pattern[y+1][x] == 1 and ((x,y+1) not in listPixels or (x,y+1) == pixelStart and len(listPixels) > 2): (x, y+1),
    #    pattern[y][x - 1] == 1 and ((x-1,y) not in listPixels or (x-1,y) == pixelStart and len(listPixels) > 2): (x - 1, y),
    #    pattern[y - 1][x] == 1 and ((x,y-1) not in listPixels or (x,y-1) == pixelStart and len(listPixels) > 2): (x, y - 1),
   # }




   # if switcher.get(True) == None:
    #    switcher = {
    #        pattern[y + 1][x + 1] == 1 and ((x+1,y+1) not in listPixels or (x+1,y+1) == pixelStart and len(listPixels) > 2): (x + 1, y + 1),
     #       pattern[y - 1][x - 1] == 1 and ((x-1,y-1) not in listPixels or (x-1,y-1) == pixelStart and len(listPixels) > 2): (x - 1, y - 1),
     #       pattern[y + 1][x - 1] == 1 and ((x-1,y+1) not in listPixels or (x-1,y+1) == pixelStart and len(listPixels) > 2): (x - 1, y + 1),
    #        pattern[y - 1][x + 1] == 1 and ((x+1,y-1) not in listPixels or (x+1,y-1) == pixelStart and len(listPixels) > 2): (x + 1, y - 1),
       # }

  #  res = switcher.get(True)
  #  if res == (pixelStart[0], pixelStart[1]):
     #   return res
    #print("res")
    #print(switcher.get(True))

    #if pixelStart[0] == x and pixelStart[1] == y and len(listPixels)>1:
       # return (pixelStart[0],pixelStart[1])

   # return switcher.get(True)




def marquePixel(listPixels, pattern, currentpixel):
    try:
        listPixels.append(currentpixel)
       # pattern[currentpixel[1]][currentpixel[0]] = -1
    except:
        print("TEST")



def findStartFigure(pattern):

    ligne = 0
    colonne = 0

    while ligne < size_picture:
        while colonne < size_picture:

            if pixelAllumeInit(pattern,colonne, ligne):
                return (colonne, ligne)

            colonne = colonne +1

        colonne = 0
        ligne = ligne +1



def testLine(x1, y1, x2, y2, pattern, listPixels):
    isLine = True
   # print("x1 " + str(x1))
   # print("x2 " + str(x2))
    #print("y1 " + str(y1))
  ##  print("y2 " + str(y2))
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
