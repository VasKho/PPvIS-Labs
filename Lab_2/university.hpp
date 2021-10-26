#ifndef _UNIVERSITY_H_
#define _UNIVERSITY_H_


#include "government_establishments.hpp"
#include "human.hpp"

namespace University
{
    class University : public Government_establishments::Educational_establishment
    {
    private:
        std::string university_name;
    public:
        University(std::string name, std::string director_name):
        university_name(name), Educational_establishment("University", director_name),
        Government_establishments("Educational establishment", director_name)
        {};
        void give_education(Human::Human& human) { human.receive_education("High education"); };
        std::string get_university_name() { return university_name; };
    };


    class Structural_units_of_university : protected University
    {
    protected:
        std::string unit_name;
        std::string type;
        std::string director;
    public:
        Structural_units_of_university(std::string tp, std::string university_name, std::string unit_director_name, std::string university_director_name):
        type(tp), director(unit_director_name),
        University(university_name, university_director_name),
        Government_establishments("Educational establishment", university_director_name)
        {};
        std::string get_establishment_director() { return University::director; };
        std::string get_unit_director() { return director; };
        void appoint_unit_director(std::string new_director_name) { this->director = new_director_name; };
    };


    class Faculty : public Structural_units_of_university
    {
    public:
        Faculty(std::string name_of_faculty, std::string university_name, std::string unit_director_name, std::string university_director_name):
        Structural_units_of_university("Faculty", university_name, unit_director_name, university_director_name),
        Government_establishments("Educational establishment", university_director_name)
        {
            this->unit_name = name_of_faculty;
        };
    };


    class Military_faculty : public Faculty, private Government_establishments::Ministry_of_defence
    {
    public:
        Military_faculty(std::string university_name, std::string unit_director_name, std::string university_director_name):
        Faculty("Military faculty", university_name, unit_director_name, university_director_name),
        Ministry_of_defence(),
        Government_establishments("Educational establishment", university_director_name)
        {};
        std::string get_director() { return Government_establishments::get_director(); };
        void appoint_director(std::string new_director_name) { Government_establishments::appoint_director(new_director_name); };
        void change_rank(Human::Soldier& soldier, std::string new_rank) { Ministry_of_defence::give_a_rank(soldier, new_rank); };
    };


    class Student : public Human::Human
    {
    protected:
        int id;
        University university;
        Faculty faculty;
    public:
    };
}
#endif
