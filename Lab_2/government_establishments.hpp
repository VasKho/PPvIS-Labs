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
        Government_establishments(std::string nm, std::string director_name):
        establishment_name(nm), director(director_name)
        {};
        void appoint_director(std::string new_director_name) { this->director = new_director_name; };
        std::string get_director() {return director;};
    };


    class Educational_establishment : public virtual Government_establishments
    {
    protected:
        std::string type;
        void give_education(Human::Human human);
    public:
        Educational_establishment(std::string tp, std::string director_name):
        type(tp), Government_establishments("Educational establishment", director_name)
        {};
        std::string get_type_of_educational_establishment() { return type; };
    };


    class Ministry_of_defence : public virtual Government_establishments
    {
    protected:
        Ministry_of_defence():
        Government_establishments("Ministry of defence", "")
        {};
    public:
        Ministry_of_defence(std::string director_name):
        Government_establishments("Ministry of defence", director_name)
        {};
        void give_a_rank(Human::Soldier& soldier, std::string rank) { soldier.set_rank(rank); };
        void call(Human::Human human);
    };
}
#endif
