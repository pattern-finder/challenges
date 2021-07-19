
#include <stdio.h> 
#include <opencv2/highgui.hpp>
#include <string>
#include <iostream>
#include "./lib/Opencv.h"
#include "./lib/Exercice.h"
#include "./lib/Matrice.h"
#include "./lib/Line.h"
#include "./lib/Pixel.h"

using namespace std;







int tailleCarre(int hauteur)
{
   return 2*hauteur +1;
}

int comparePixel(int x, int y, Matrice matriceSource){

    int color[3] = {255,255,255};
    Pixel pixelNone = Pixel(x, y, color);
    Pixel pixel = matriceSource.getPixel(x, y);

    return !pixel.compare(pixelNone);

}


bool parcourtPatternX(int posX, int posY, int endX, Matrice pattern){
  

    if (posX == endX){
        return comparePixel(posX ,posY, pattern);
    }else{
        
        if (comparePixel(posX ,posY, pattern))
            return parcourtPatternX(posX + 1, posY, endX, pattern);

        else
            return false;
    }
}

bool parcourtPatternY(int posX, int posY, int endY, Matrice pattern){
    if (posY == endY){
        return comparePixel(posX ,posY, pattern);
    }else{
        
        if (comparePixel(posX ,posY, pattern))
            return parcourtPatternY(posX, posY+1, endY, pattern);

        else
            return false;
    }
}




int doExercice(vector<Matrice> listPattern, int start_X, int start_Y)
{   

    bool equal = false;
    int currentId = 0;
    int x = 0;
    int y = 0;
    int posX;
    int posY;
    int solutionId = -1;

    for(unsigned int i = 0; i < listPattern.size(); i++){
        Matrice pattern = listPattern[i];
        posX = start_X;
        posY = start_Y;
      

        int decalage = 0;
        int taille_forme;
        while (posX > 0 && posY > 0 && ! equal){


            if (comparePixel(posX, posY, pattern)){

                taille_forme = tailleCarre(decalage)+1;

                if (parcourtPatternX(posX, posY, posX + taille_forme, pattern) &&
                        parcourtPatternX(posX, posY + taille_forme, posX + taille_forme, pattern) &&
                        parcourtPatternY(posX, posY, posY + taille_forme, pattern) &&
                        parcourtPatternY(posX + taille_forme, posY, posY + taille_forme, pattern)){

                    equal = true;
                    solutionId = currentId;


                }
            }
            decalage = decalage + 1;
            posX = posX - 1;
            posY = posY - 1;
        }

        currentId++;

    }
     cout <<solutionId<< endl;
    return solutionId;
}


std::string testAlgo(std::string nameExercice, int resultat, int nbMatriceResult){
    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(resultat, nameExercice);
    vector<Matrice> listPatternInit = opencv.initExercice();


    int start_X = int(opencv.sizeImage / 2) - 1;
    int start_Y = int(opencv.sizeImage / 2) - 1;

    int solution_user = doExercice(listPatternInit, start_X, start_Y);

    return exercice.assertRes(solution_user, resultat);
}




int main(int argc, char *argv[])
{
    std::string nameExercice = "comparaisonCarre";
    int resultat = 3;
    int nbMatriceResult = 0;

    
    cout << testAlgo(nameExercice, resultat, nbMatriceResult) << endl;

}