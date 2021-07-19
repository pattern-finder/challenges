
#include <stdio.h> 
#include <opencv2/highgui.hpp>
#include <string>
#include <iostream>
#include <math.h>
#include "./lib/Opencv.h"
#include "./lib/Exercice.h"
#include "./lib/Matrice.h"
#include "./lib/Line.h"
#include "./lib/Pixel.h"
// g++ comparaisonMatrice.cpp -o comparaisonMatrice `pkg-config --cflags --libs opencv4`
using namespace std;

bool pixelIsNull(int x, int y, Matrice matriceSource){

    int color[3] = {255,255,255};
    Pixel pixelNone = Pixel(x, y, color);

    return !matriceSource.getPixel(x, y).compare(pixelNone);
}




double calculNorme(double dx, double dy){
    return sqrt(dx * dx + dy * dy);
}

double calculProduitScalaire(double dx1, double dy1, double dx2, double dy2){
    return dx1*dx2 + dy1*dy2;
}

double valAbs(double a, double b){

    double res = b-a ;
    if (res < 0){
        return -res;
    }else{
        return res;
    }
}


double calculAngle(Pixel pixelBegin, Pixel pixelMiddle, Pixel pixelEnd){

    double dx1 = (pixelBegin.getX() - pixelMiddle.getX());
    double dy1 = (pixelBegin.getY() - pixelMiddle.getY());
    double dx2 = (pixelEnd.getX() - pixelMiddle.getX());
    double dy2 = (pixelEnd.getY() - pixelMiddle.getY());

    double produitScalaire = calculProduitScalaire(dx1, dy1, dx2, dy2);

    double normeP1 = calculNorme(dx1, dy1);
    double normeP2 = calculNorme(dx2, dy2);

    double cos_angle = produitScalaire / (normeP1*normeP2);

    double radiant = acos(cos_angle);

    double angle_degree = radiant*180/3.14159265358979323846;
    cout << angle_degree << endl;

    return round(angle_degree);
}




bool testLine(int x1, int y1, int x2, int y2, Matrice patternTest){

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





vector<double> doExercice(vector<Matrice> listPattern, vector<Line> listeListePixelParImage, vector<double> dict_resultat, int size_matrice){

      for(unsigned int i = 0; i < listPattern.size(); i++){

        Line listeListeInit = listeListePixelParImage[i];

        Pixel p0 = listeListeInit.getPixelFromLine(0);
        Pixel p1 = listeListeInit.getPixelFromLine(1);
        Pixel p2 = listeListeInit.getPixelFromLine(2);

        if(p0.getX() >= 0 && p0.getY() >= 0 && p1.getX()  >= 0 && p1.getY() >= 0 && p2.getX()  >= 0 && p2.getY() >= 0 &&
                p0.getX()  < size_matrice && p0.getY() < size_matrice && p1.getX()  < size_matrice && p1.getY() < size_matrice && p2.getX()  < size_matrice && p2.getY() < size_matrice){


            double angle = calculAngle(p0, p1, p2);
            dict_resultat.push_back(angle);

        }else{
            dict_resultat.push_back(-1);

        }
    }

    return dict_resultat;
}










string testAlgo(string nameExercice, int nbMatriceResult){
    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(-1, nameExercice);
    vector<Matrice> listPatternInit = opencv.initExercice();
  

    vector<double> dict_resultat;



    vector<double> resultat_valide;
    resultat_valide.push_back(90.0);
    resultat_valide.push_back(45.0);
    resultat_valide.push_back(135.0);
  

    int color1[3] = {0,0,0};
    int color2[3] = {0,0,0};
    int color3[3] = {0,0,0};
    int color4[3] = {0,0,0};
    int color5[3] = {0,0,0};
    int color6[3] = {0,0,0};
    int color7[3] = {0,0,0};
    int color8[3] = {0,0,0};
    int color9[3] = {0,0,0};
    int color10[3] = {0,0,0};
    int color11[3] = {0,0,0};
    int color12[3] = {0,0,0};

    Pixel p10 = Pixel(4,2,color1);
    Pixel p11 = Pixel(4,14,color2);
    Pixel p12 = Pixel(19,14,color3);
    Line list1;
    list1.insertPixel(p10);
    list1.insertPixel(p11);
    list1.insertPixel(p12);

  

    Pixel p30 = Pixel(16,2,color7);
    Pixel p31 = Pixel(4,14,color8);
    Pixel p32 = Pixel(19,14,color9);
    Line list3;
    list3.insertPixel(p30);
    list3.insertPixel(p31);
    list3.insertPixel(p32);

    Pixel p40 = Pixel(4,8,color10);
    Pixel p41 = Pixel(10,14,color11);
    Pixel p42 = Pixel(19,14,color12);
    Line list4;
    list4.insertPixel(p40);
    list4.insertPixel(p41);
    list4.insertPixel(p42);

    vector<Line> listeListePixelParImage;
    listeListePixelParImage.push_back(list1);
    listeListePixelParImage.push_back(list3);
    listeListePixelParImage.push_back(list4);


    vector<double> solution_user = doExercice(listPatternInit, listeListePixelParImage, dict_resultat,opencv.sizeImage);

    return exercice.assertResMult(solution_user, resultat_valide);
}







int main(int argc, char *argv[]){
    string nameExercice = "comparaisonAngle";
    int resultat = 0;
    int nbMatriceResult = 0;

    cout << testAlgo(nameExercice, nbMatriceResult) << endl;
}