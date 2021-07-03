
#include <stdio.h> 
#include <opencv2/highgui.hpp>
#include <string>
#include <iostream>
#include "./bibliothequeCpp/Opencv.h"
#include "./bibliothequeCpp/Exercice.h"
#include "./bibliothequeCpp/Matrice.h"
#include "./bibliothequeCpp/Line.h"
#include "./bibliothequeCpp/Pixel.h"
// g++ comparaisonMatrice.cpp -o comparaisonMatrice `pkg-config --cflags --libs opencv4`
using namespace std;




bool pixelIsNull(int x, int y, Matrice matriceSource){

    int color[3] = {255,255,255};
    Pixel pixelNone = Pixel(x, y, color);

    return !matriceSource.getPixel(x, y).compare(pixelNone);
}




int doExercice(vector<Matrice> listPattern, int start_X, int start_Y)
{   
     int solutionId = 0;

    for(unsigned int i = 0; i < listPattern.size(); i++){
        Matrice pattern = listPattern[i];
        int r = 0;
        bool res = false;

        while (r <= 11){

            int x = 0;
            int y = int(r);
            float d = 5.0 - 4.0*r;

            res = pixelIsNull(x + start_X, y + start_Y, pattern) &&
            pixelIsNull(y + start_X, x + start_Y, pattern) &&
            pixelIsNull(-x + start_X, y + start_Y, pattern) &&
            pixelIsNull(-y + start_X, x + start_Y, pattern) &&
            pixelIsNull(x + start_X, -y + start_Y, pattern) &&
            pixelIsNull(y + start_X, -x + start_Y, pattern) &&
            pixelIsNull(-x + start_X, -y + start_Y, pattern) &&
            pixelIsNull(-y + start_X, -x + start_Y, pattern);





            while (y > x){

                if  (d > 0){
                    y = y-1;
                    d = d - 8.0*y;
                }

                x = x + 1;
                d = d + 8.0 * x + 4.0;
                res = res && pixelIsNull(x + start_X, y + start_Y, pattern) &&
                pixelIsNull(y + start_X, x + start_Y, pattern) &&
                pixelIsNull(-x + start_X, y + start_Y, pattern) &&
                pixelIsNull(-y + start_X, x + start_Y, pattern) &&
                pixelIsNull(x + start_X, -y + start_Y, pattern) &&
                pixelIsNull(y + start_X, -x + start_Y, pattern) &&
                pixelIsNull(-x + start_X, -y + start_Y, pattern) &&
                pixelIsNull(-y + start_X, -x + start_Y, pattern);
            }


            r++;
        }
        if (res){
            return solutionId;
        }

        solutionId += 1;
    }

    return -1;
}



string testAlgo(string nameExercice, int resultat, int nbMatriceResult){
    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(resultat, nameExercice);
    vector<Matrice> listPatternInit = opencv.initExercice();

    int start_X = int(opencv.sizeImage / 2);
    int start_Y = int(opencv.sizeImage / 2);

    int solution_user = doExercice(listPatternInit, start_X, start_Y);
    cout << solution_user << endl;

    return exercice.assertRes(solution_user, resultat);
}



int main(int argc, char *argv[])
{
    string nameExercice = "comparaisonCercle";
    int resultat = 3;
    int nbMatriceResult = 0;

    cout << testAlgo(nameExercice, resultat, nbMatriceResult) << endl;

}