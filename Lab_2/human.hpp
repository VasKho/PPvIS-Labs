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
        Human(std::string name_of_person, std::string education_of_person = ""):
        name(name_of_person), education(education_of_person)
        {};
        void receive_education(std::string new_education) { this->education = new_education; };
        std::string get_name() { return name; };
        std::string get_education() { return education; };
    };


    class Soldier : public Human
    {
    private:
        std::string rank;
    public:
        void set_rank(std::string new_rank) { this->rank = new_rank; };
        Soldier(std::string name_of_soldier, std::string rank_of_soldier = "", std::string education_of_person = ""):
        Human(name_of_soldier, education_of_person), rank(rank_of_soldier)
        {};
        std::string get_rank() { return rank; };
    };
}
#endif
