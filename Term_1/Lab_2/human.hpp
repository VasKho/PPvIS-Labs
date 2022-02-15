/// @file human.hpp
/// @author Vasili Khoroshavin
/// @date 14.10.2021

#ifndef _HUMAN_H_
#define _HUMAN_H_


#include <iostream>
namespace Human
{
    class Human
    {
        protected:
            std::string name;
            std::string education;
        public:
            /**
            * @brief Constructor of class Human
            * @param [in] name_of_person - name of specified person
            * @param [in] education_of_person - education of specified person (Default value is "")
            */
            Human(std::string name_of_person, std::string education_of_person = ""):
            name(name_of_person), education(education_of_person)
            {};
            /**
            * @brief Function for receiving education of specified person
            * @param [in] new_education - new education of specified person
            */
            void receive_education(std::string new_education) { this->education = new_education; };
            std::string get_name() { return name; };
            std::string get_education() { return education; };
    };
}
#endif
