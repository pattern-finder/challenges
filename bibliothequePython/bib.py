

class Matrice:
    def __init__(self, size, matrice_content):
        self.size = size
        self.matrice = matrice_content


    def getSize(self):
        return self.size

    def getPixel(self, x, y):
        return self.matrice_content[x][y]

    def toString(self):

        for line in self.matrice:
            print(self.getLine(line, 0))


    def getLine(self, line, pos):

        if pos < len(line):
            return str(line[pos]) + self.getLine(line, pos+1)

        else:
            return ""







class Pixel:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getColor(self):
        return self.color

    def compare(self, pixel):
        return self.color[0] == pixel.color[0] and self.color[1] == pixel.color[1] and self.color[2] == pixel.color[2]



