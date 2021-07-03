
#include <stdio.h> 
#include <opencv2/highgui.hpp>
#include <string>
#include <iostream>
#include <math.h>
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




bool verifLine(int x1, int y1, int x2, int y2, Matrice patternTest){

    bool res = true;

    int dx = x2 - x1;

    if (dx != 0){
        if (dx > 0){
            int dy = y2 - y1;

            if (dy != 0){

                if (dy > 0){

                    if (dx >= dy){
                        int e = dx;
                        dx = 2 * e;
                        dy = dy * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);
                        while (x1 != x2){

                            res = res && pixelIsNull(x1, y1, patternTest);
                            x1 = x1 + 1;
                            e = e - dy;

                            if (e < 0){
                                y1 = y1 + 1;
                                e = e + dx;
                            }
                        }

                    }else{
                        int e = dy;
                        dx = dx * 2;
                        dy = e * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);
                        while (y1 != y2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            y1 = y1 + 1;
                            e = e - dx;

                            if (e < 0){
                                x1 = x1 + 1;
                                e = e + dy;
                            }
                        }
                    }

                }else{

                    if (dx >= -dy){
                        int e = dx;
                        dx = 2 * e;
                        dy = dy * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);
                        while (x1 != x2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            x1 = x1 + 1;
                            e = e + dy;

                            if (e < 0){
                                y1 = y1 - 1;
                                e = e + dx;
                            }
                        }
                    

                    }else{
                        int e = dy;
                        dx = 2 * dx;
                        dy = e * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);
                        while (y1 != y2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            y1 = y1 - 1;
                            e = e + dx;
                        

                            if (e > 0){
                                x1 = x1 + 1;
                                e = e + dy;
                            }
                        }
                    }
                }
            }else{
                while (x1 != x2){
                    res = res && pixelIsNull(x1, y1, patternTest);
                    x1 = x1 + 1;
                }
            }


        }else{

            int dy = y2 - y1;
            if (dy != 0){

                if (dy > 0){
                    if (-dx >= dy){
                        //4eme octant

                        int e = dx;
                        dx = 2 * e;
                        dy = dy * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);

                        while (x1 != x2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            x1 = x1 - 1;
                            e = e + dy;

                            if (e >= 0){
                                y1 = y1 + 1;
                                e = e + dx;
                            }
                        }

                    }else{
                        int e = dy;
                        dx = dx * 2;
                        dy = e * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);

                        while (y1 != y2){

                            res = res && pixelIsNull(x1, y1, patternTest);
                            y1 = y1 + 1;
                            e = e + dx;

                            if (e <= 0){
                                x1 = x1 - 1;
                                e = e + dy;
                            }
                        }
                    }
                }else{
                    // 5eme octant
                    if (dx <= dy){
                        int e = dx;
                        dx = 2 * e;
                        dy = dy * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);

                        while (x1 != x2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            x1 = x1 - 1;
                            e = e - dy;
                        

                            if (e >= 0){
                                y1 = y1 - 1;
                                e = e + dx;
                            }
                        }

                    }else{
                        int e = dy;
                        dx = 2 * dx;
                        dy = e * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);

                        while (y1 != y2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            y1 = y1 - 1;
                            e = e - dx;

                            if (e >= 0){
                                x1 = x1 - 1;
                                e = e + dy;
                            }
                        }
                    }
                }

            }else{
                res = res && pixelIsNull(x1, y1, patternTest);

                while (x1 != x2){
                    x1 = x1 - 1;
                    res = res && pixelIsNull(x1, y1, patternTest);
                }
            }
        }

    }else{
        int dy = y2 - y1;
        if (dy != 0){
            if (dy > 0){
                while (y1 != y2){
                    y1 = y1 + 1;
                    res = res and pixelIsNull(x1, y1, patternTest);
                }
            }
        }else{
                while (y1 != y2){
                    y1 = y1 - 1;
                    res = res and pixelIsNull(x1, y1, patternTest);
                }
            }
    }


    return res;
}


Pixel rotate (Pixel M, Pixel O, double angle){

    angle = (angle*3.14159265358979323846) / 180.0;
    int xM = M.getX() - O.getX();
    int yM = M.getY() - O.getY();
    double x = xM * cos(angle) + yM * sin(angle) + O.getX();
    double y = - xM * sin(angle) + yM * cos(angle) + O.getY();

    int color[3] = {0,0,0};
    Pixel pixel = Pixel(round(x),round(y), color);

    return pixel;
}



int doExercice(vector<Matrice> listMatrice, Pixel XY1, Pixel XY2, Pixel XY3, Pixel XY4,  int start_X, int start_Y){

    int color[3] = {0,0,0};
    Pixel centreFigure = Pixel(start_X, start_Y, color);



    int idSolution = -1;
    int id = 0;
    bool res;
    for(unsigned int i = 0; i < listMatrice.size(); i++){
        Matrice pattern = listMatrice[i];
        int angle = 0;
        while (angle < 180){

                Pixel XY1_bis = rotate(XY1,centreFigure, double(angle));
                Pixel XY2_bis = rotate(XY2,centreFigure, double(angle));
                Pixel XY3_bis = rotate(XY3,centreFigure, double(angle));
                Pixel XY4_bis = rotate(XY4,centreFigure, double(angle));

                res = verifLine(XY1_bis.getX(), XY1_bis.getY(), XY2_bis.getX(), XY2_bis.getY(), pattern) &&
                verifLine(XY2_bis.getX(), XY2_bis.getY(), XY3_bis.getX(), XY3_bis.getY(), pattern) &&
                verifLine(XY3_bis.getX(), XY3_bis.getY(), XY4_bis.getX(), XY4_bis.getY(), pattern) &&
                verifLine(XY4_bis.getX(), XY4_bis.getY(), XY1_bis.getX(), XY1_bis.getY(), pattern);

                if(res){
                    idSolution = id;
                }

                angle = angle + 1;
        }

        id = id + 1;
    }
    return idSolution;
}







string testAlgo(string nameExercice, int resultat, int nbMatriceResult){
    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(-1, nameExercice);
    vector<Matrice> listPatternInit = opencv.initExercice();

    int start_X = 11;
    int start_Y = 11;

    int color1[3] = {0,0,0};
    int color2[3] = {0,0,0};
    int color3[3] = {0,0,0};
    int color4[3] = {0,0,0};

    Pixel XY1 = Pixel(4, 7, color1);
    Pixel XY2 = Pixel(18, 7, color2);
    Pixel XY3 = Pixel(18, 15, color3);
    Pixel XY4 = Pixel(4, 15, color4);


    int solution_user = doExercice(listPatternInit, XY1, XY2, XY3, XY4, start_X, start_Y);

    return exercice.assertRes(solution_user, resultat);
}







int main(int argc, char *argv[]){
    string nameExercice = "comparaisonRotation";
    int resultat = 2;
    int nbMatriceResult = 1;

    cout << testAlgo(nameExercice,resultat, nbMatriceResult) << endl;
}