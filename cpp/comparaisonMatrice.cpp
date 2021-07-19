
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
// g++ comparaisonMatrice.cpp -o comparaisonMatrice `pkg-config --cflags --libs opencv4`


int doExercice(vector<Matrice> listPattern, Matrice result){
    int currentId = 0;
    int x = 0;
    int y = 0;

    for(unsigned int i = 0; i < listPattern.size(); i++){
        x = 0;
        y = 0;

        bool equaL = true;
        Matrice matrice = listPattern[i];
        while( y < result.getSize() && equaL){
            
            while( x < result.getSize() && equaL){

                if( ! (matrice.getPixel(x,y).compare(result.getPixel(x,y)))){

                    equaL = false;
                }
                x++;
           
            }
            x=0;
            y++;
           
            }

             if(equaL){
                return currentId;
            }else{
                currentId++;
        }

    }
    return -1;
}





std::string testAlgo(std::string nameExercice, int resultat, int nbMatriceResult){

    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(resultat, nameExercice);
    Exercice(resultat, nameExercice);
    std::vector<Matrice> listPatternInit = opencv.initExercice();
    Matrice matrice_result = opencv.matriceResult();

    int solution_user = doExercice(listPatternInit, matrice_result);
    return exercice.assertRes(solution_user, resultat);
    
    return 0;
}





int main(int argc, char *argv[])
{
    std::string nameExercice = "comparaisonMatrice";
    int resultat = 2;
    int nbMatriceResult = 1;

    cout << testAlgo(nameExercice, resultat, nbMatriceResult) << endl;
}