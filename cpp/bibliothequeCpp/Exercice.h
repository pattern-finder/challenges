

#ifndef DEF_EXERCICE // include guard
#define  DEF_EXERCICE 


class Exercice{
        public :
        
        int resultat;
        std::string nameExercice;

        Exercice(int resultat, std::string nameExercice);
        std::string assertRes(int solution_user, int resultat);
        std::string assertResMult(std::vector<double> solution_user, std::vector<double> resultat);
        std::string assertResMultInt(std::vector<int> solution_user, std::vector<int> resultat);

    };

#endif /* MY_CLASS_H */
