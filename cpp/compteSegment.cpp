
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

bool pixelInLine(Pixel pixel, Line line){
    bool isIn = false;

    for(unsigned int i = 0; i < line.getSize(); i++){

        Pixel pixel2 = line.getPixelFromLine(i);

        if(pixel2.compare(pixel) && pixel2.getX() == pixel.getX() && pixel2.getY() == pixel.getY()){
            isIn = true;
        }
    }
    return isIn;
}


Pixel findStartFigure(Matrice pattern, int size_matrice){

    int ligne = 0;
    int colonne = 0;

    while (ligne < size_matrice){
        while (colonne < size_matrice){

            if (pixelIsNull(colonne, ligne, pattern)){

                int color[3] = {0,0,0};
                Pixel pixel = Pixel(colonne, ligne, color);
                return pixel;
            }

            colonne = colonne +1;

        }
        colonne = 0;
        ligne = ligne +1;
    }
    int color2[3] = {0,0,0};
    Pixel pixelNone = Pixel(-1, -1, color2);
    return pixelNone;
}




Line trouverPixelSuivant(Pixel pixelStart,Matrice pattern, Line cheminCourant){
    int x = pixelStart.getX();
    int y = pixelStart.getY();

    Line lisPotentielPixelNext;
    int color[3] = {0,0,0};

    Pixel pixel = Pixel(x + 1, y, color);
    if (pixelIsNull(x+1, y, pattern) && !pixelInLine(pixel, cheminCourant)){
        lisPotentielPixelNext.insertPixel(pixel);
    }
    
    Pixel pixel2 = Pixel(x, y + 1, color);
    if (pixelIsNull(x, y+1, pattern) && !pixelInLine(pixel2, cheminCourant)){
        lisPotentielPixelNext.insertPixel(pixel2);
    }

    Pixel pixel3 = Pixel(x - 1, y, color);
    if (pixelIsNull(x-1, y, pattern) && !pixelInLine(pixel3, cheminCourant)){
        lisPotentielPixelNext.insertPixel(pixel3);
    }

    Pixel pixel4 = Pixel(x, y - 1, color);
    if (pixelIsNull(x, y-1, pattern) && !pixelInLine(pixel4, cheminCourant)){
        lisPotentielPixelNext.insertPixel(pixel4);
    }

    Pixel pixel5 = Pixel(x + 1, y + 1, color);
    if (pixelIsNull(x+1, y+1, pattern) && !pixelInLine(pixel5, cheminCourant)){
        lisPotentielPixelNext.insertPixel(pixel5);
    }

    Pixel pixel6 = Pixel(x - 1, y - 1, color);
    if (pixelIsNull(x-1, y-1, pattern) && !pixelInLine(pixel6, cheminCourant)){
        lisPotentielPixelNext.insertPixel(pixel6);
    }

    Pixel pixel7 = Pixel(x - 1, y + 1, color);
    if (pixelIsNull(x-1, y+1, pattern) && !pixelInLine(pixel7, cheminCourant)){
        lisPotentielPixelNext.insertPixel(pixel7);
    }

    Pixel pixel8 = Pixel(x + 1, y - 1, color);
    if (pixelIsNull(x+1, y-1, pattern) && !pixelInLine(pixel8, cheminCourant)){
        lisPotentielPixelNext.insertPixel(pixel8);
    }


    return lisPotentielPixelNext;
}



Line trouverPlusLongChemin(Pixel pixelCurent, Matrice pattern,Line cheminCourant, Pixel pixelStart, Pixel insertPixel){

    cheminCourant.insertPixel(insertPixel);
    Line plusLongChemin = cheminCourant;
    Line pixelsSuivant = trouverPixelSuivant(pixelCurent, pattern, cheminCourant);

    for(unsigned int i = 0; i < pixelsSuivant.getSize(); i++){
        Pixel pixel = pixelsSuivant.getPixelFromLine(i);
        Line chemintmp = cheminCourant;

        if (!pixelInLine(pixel, cheminCourant)){

            Line nouveauChemin = trouverPlusLongChemin(pixel, pattern, chemintmp, pixelStart, pixel);

            if (nouveauChemin.getSize() != 0){

                if (nouveauChemin.getSize() > plusLongChemin.getSize()){
                    plusLongChemin = nouveauChemin;
                }
            }
        }
    }

    return plusLongChemin;
}


void toStr(Line v){

    cout <<"Start STR "<< endl;

    for(unsigned int i = 0; i < v.getSize(); i++){
        Pixel p = v.getPixelFromLine(i);
        cout << p.getX() << endl;
        cout << p.getY() << endl;
        cout <<" "<< endl;

    }

    cout <<"End STR "<< endl;

}


vector<int> doExercice(vector<Matrice> listPattern,int size_matrice){

    int idImage = 0;
    int count_line = 0;
    vector<int> resultat_utilisateur;
   
    for(unsigned int i = 0; i < listPattern.size(); i++){
        Matrice pattern = listPattern[i];


        Line listPixelSegment;
        Line init_list_pixel_form;

        Pixel pixelStart = findStartFigure(pattern, size_matrice);
        cout << pixelStart.getX() << endl;
        cout << pixelStart.getY() << endl;

         if (pixelStart.getX() != -1 && pixelStart.getY() != -1){
            count_line = 1;

            Line listPixelForme = trouverPlusLongChemin(pixelStart, pattern, init_list_pixel_form, pixelStart, pixelStart);
            listPixelForme.insertPixel(pixelStart);
            toStr(listPixelForme);
            for(unsigned int j = 0; j < listPixelForme.getSize(); j++){
                Pixel pixel_current = listPixelForme.getPixelFromLine(j);

                if (testLine(pixelStart.getX(),pixelStart.getY(), pixel_current.getX(), pixel_current.getY(), pattern)){
                    listPixelSegment.insertPixel(pixel_current);

                }else{
                    count_line = count_line + 1;
                    pixelStart = pixel_current;
                    Pixel initPixel = listPixelSegment.getPixelFromLine(listPixelSegment.getSize()-1);
                    Line listPixelSegment;
                    listPixelSegment.insertPixel(initPixel);
                    listPixelSegment.insertPixel(pixelStart);
                }
            }
        }


        resultat_utilisateur.push_back(count_line);
        idImage += 1;
    }


    return resultat_utilisateur;
}









string testAlgo(string nameExercice,  vector<int> resultat, int nbMatriceResult){
    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(0, nameExercice);
    vector<Matrice> listPatternInit = opencv.initExercice();
    

    vector<int> solution_user = doExercice(listPatternInit, opencv.sizeImage);

    cout << "solution_user" << endl;
    cout << solution_user[0] << endl;
    cout << solution_user[1] << endl;
    cout << solution_user[2] << endl;

    return exercice.assertResMultInt(solution_user, resultat);
}


int main(int argc, char *argv[]){
    string nameExercice = "compteSegment";

    vector<int> resultat;
    resultat.push_back(0);
    resultat.push_back(3);
    resultat.push_back(6);

    int nbMatriceResult = 0;

    cout << testAlgo(nameExercice, resultat, nbMatriceResult) << endl;
}