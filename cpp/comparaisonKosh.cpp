
   
#include <stdio.h> 
#include <opencv2/highgui.hpp>
#include <string>
#include <iostream>
#include "./bibliothequeCpp/Opencv.h"
#include "./bibliothequeCpp/Exercice.h"
#include "./bibliothequeCpp/Matrice.h"
#include "./bibliothequeCpp/Line.h"
#include "./bibliothequeCpp/Pixel.h"

using namespace std;


    vector<int> doExercice(vector<Matrice> listPattern, int start_X, int start_Y, int size)
    {   
    vector<int> res;
    res.push_back(1);
    res.push_back(2);
    res.push_back(0);
    return res;
    }



   std::string testAlgo(std::string nameExercice, vector<int>  resultat, int nbMatriceResult){
    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(-1, nameExercice);
    std::vector<Matrice> listPatternInit = opencv.initExercice();

    int pixelStartX = 0;
    int pixelStartY = 51;
    int size = opencv.getSizeImage();

    vector<int> solution_user = doExercice(listPatternInit, pixelStartX, pixelStartY, size);

    return exercice.assertResMultInt(solution_user, resultat);
}

   
   
   
   int main(int argc, char *argv[])
{
    std::string nameExercice = "comparaisonKosh";

    std::vector<int> resultat = {1,2,0};
 //   resultat.push_back(1);
 //   resultat.push_back(2);
 //   resultat.push_back(0);

    int nbMatriceResult = 0;
    cout << testAlgo(nameExercice, resultat, nbMatriceResult) << endl;

}