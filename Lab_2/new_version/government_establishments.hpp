/// @file government_establishments.hpp
/// @author Vasili Khoroshavin
/// @date 16.10.2021

#ifndef _GOVERNMENT_ESTABLISHMENTS_H_
#define _GOVERNMENT_ESTABLISHMENTS_H_


#include <iostream>
#include "human.hpp"

namespace Government_establishments
{

    class Government_establishments
    {
        protected:
            std::string establishment_name;
            std::string director;
        public:
            /**
            * @brief Government_establishments constructor
            * @param [in] nm - name of of establishment
            * @param [in] director_name - name of director of the establishment
            */
            Government_establishments(std::string nm, std::string director_name):
            establishment_name(nm), director(director_name)
            {};
            /**
            * @brief Function for setting new director of establishment
            * @param [in] new_director_name - name of new director
            */
            void appoint_director(std::string new_director_name) { this->director = new_director_name; };
            std::string get_director() {return director;};
    };


    class Educational_establishment : public Government_establishments
    {
        protected:
            std::string type;
            /**
            * @brief Function for changing education of object of type <b>Human</b>
            * @param [in] human - person whose education will be changed
            */
            void give_education(Human::Human human);
        public:
            /**
            * @brief Educational_establishment constructor
            * @param [in] tp - type of educational establishment (i.e. university)
            * @param [in] director_name - name of director of educational establishment
            */
            Educational_establishment(std::string tp, std::string director_name):
            type(tp), Government_establishments("Educational establishment", director_name)
            {};
            std::string get_type_of_educational_establishment() { return type; };
    };
}
#endif
