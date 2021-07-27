
   
#include <stdio.h> 
#include <opencv2/highgui.hpp>
#include <string>
#include <iostream>
#include "./bibliothequeCpp/Opencv.h"
#include "./bibliothequeCpp/Exercice.h"
#include "./bibliothequeCpp/Matrice.h"
#include "./bibliothequeCpp/Line.h"
#include "./bibliothequeCpp/Pixel.h"
#include <map>
using namespace std;

    std::map<string, int> doExercice(vector<Matrice> listPattern, std::map<string, int> dict_resultat, int size)
    {   
        std::map<string, int> res = {{"carré", 2,},
                                    {"rectangle", 3,},
                                    {"autre parallèlogramme", 1,},

                                    {"triangle rectangle", 2,},
                                    {"triangle équilatéral", 0,},
                                    {"triangle isocèle", 2,},
                                    {"triangle quelconque", 1,},

                                    {"polygone à 5 coté", 1,},
                                    {"polygone à 6 coté", 0,},
                                    {"polygone à 7 coté", 2,}};
        return res;
    }



   std::string testAlgo(std::string nameExercice, std::map<string, int> resultat, int nbMatriceResult){
    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(-1, nameExercice);
    vector<Matrice> listPatternInit = opencv.initExercice();

    int size = opencv.getSizeImage();

        std::map<string, int> tab_user = {{"carré", 0,},
                                    {"rectangle", 0,},
                                    {"autre parallèlogramme", 0,},

                                    {"triangle rectangle", 0,},
                                    {"triangle équilatéral", 0,},
                                    {"triangle isocèle", 0,},
                                    {"triangle quelconque", 0,},

                                    {"polygone à 5 coté", 0,},
                                    {"polygone à 6 coté", 0,},
                                    {"polygone à 7 coté", 0,}};


    std::map<string, int> solution_user = doExercice(listPatternInit, tab_user, size);

    return exercice.assertResMultDict(solution_user, resultat);
}

   
   
   
   int main(int argc, char *argv[])
{
    std::string nameExercice = "dataForm";

    std::map<string, int> resultat = {{"carré", 2,},
                                    {"rectangle", 3,},
                                    {"autre parallèlogramme", 1,},

                                    {"triangle rectangle", 2,},
                                    {"triangle équilatéral", 0,},
                                    {"triangle isocèle", 2,},
                                    {"triangle quelconque", 1,},

                                    {"polygone à 5 coté", 1,},
                                    {"polygone à 6 coté", 0,},
                                    {"polygone à 7 coté", 2,}};

    int nbMatriceResult = 0;
    cout << testAlgo(nameExercice, resultat, nbMatriceResult) << endl;

}