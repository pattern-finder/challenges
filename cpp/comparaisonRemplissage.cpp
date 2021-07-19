
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



int remplissageBalayage(vector<Matrice> listPattern, int size_matrice){
    int idSolution = 0;

    for(unsigned int i = 0; i < listPattern.size(); i++){
            Matrice pattern = listPattern[i];
            pattern.toStringPixel();
            bool echec = false;
            int ligne = 0;
            int colonne = 0;

        while (ligne < size_matrice-1 && !echec){

                int cpt_bordure = 0;
                bool inForm = false;


            while (colonne < size_matrice-1 && !echec){
  

                if (cpt_bordure > 2 && cpt_bordure != 0){
                    echec = true;
                }

                if (pixelIsNull(colonne, ligne, pattern)){

                    if (!inForm){
                        inForm = true;
                        cpt_bordure += 1;
                    }

                }else{

                    if (inForm){
                        inForm = false;
                        cpt_bordure += 1;
                    }
                }



                colonne = colonne + 1;

            }
            colonne = 0;
            ligne = ligne + 1;
        }



        if (!echec){
            return idSolution;
        }
        idSolution++;
        }

    return -1;
    }



int doExercice(vector<Matrice> listPatternInit,int size_matrice){

    int res1 = remplissageBalayage(listPatternInit, size_matrice);
    return res1;
}



string testAlgo(string nameExercice, int resultat, int nbMatriceResult){
    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(resultat, nameExercice);
    vector<Matrice> listPatternInit = opencv.initExercice();

    int solution_user = doExercice(listPatternInit, opencv.getSizeImage());
    cout << "SOLUTION" << endl;
    cout << solution_user << endl;

    return exercice.assertRes(solution_user, resultat);
}


int main(int argc, char *argv[])
{
    string nameExercice = "comparaisonRemplissage";
    int resultat = 2;
    int nbMatriceResult = 0;

    cout << testAlgo(nameExercice, resultat, nbMatriceResult) << endl;

}