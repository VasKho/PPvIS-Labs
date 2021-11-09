#ifndef _UNIVERSITY_H_
#define _UNIVERSITY_H_


#include "government_establishments.hpp"
#include "human.hpp"

namespace University
{
    class Structural_units_of_university
    {
        protected:
            std::string unit_name;
            std::string type;
            std::string director;
        public:
            /**
             * @brief class Structural_units_of_university constructor
             * @param [in] tp - type of unit (i.e. faculty or cathedra)
             * @param [in] university_name - name of university
             * @param [in] unit_director_name - name of director of the unit
             * @param [in] university_director_name - name of director of the university which masters the unit
             */
            Structural_units_of_university(std::string tp, std::string university_name, std::string unit_director_name, std::string university_director_name):
            type(tp), director(unit_director_name)
            {};
            std::string get_unit_director() { return director; };
            /**
            * @brief Function for changing unit director name
            * @param [in] new_director_name - name of new director
            */
            void appoint_unit_director(std::string new_director_name) { this->director = new_director_name; };
    };


    class Faculty : public Structural_units_of_university
    {
        public:
            /**
             * @brief class Faculty constructor
             * @param [in] name_of_faculty - name of specified faculty
             * @param [in] university_name - name of university which masters the faculty
             * @param [in] unit_director_name - name of faculty director
             * @param [in] university_director_name - name of university director
             */
            Faculty(std::string name_of_faculty, std::string university_name, std::string unit_director_name, std::string university_director_name):
            Structural_units_of_university("Faculty", university_name, unit_director_name, university_director_name)
            {
                this->unit_name = name_of_faculty;
            };
            Faculty get_faculty() { return *this; };
            std::string get_faculty_name() { return this->unit_name; };
    };


    class University : public Government_establishments::Educational_establishment, private Faculty
    {
        private:
            std::string university_name;
        public:
            /**
             * @brief class University constructor
             * @param [in] name - name of university
             * @param [in] director_name - name of director of the university
             */
            University(std::string name, std::string director_name):
            university_name(name), Educational_establishment("University", director_name),
            Faculty("", name, "", director_name)
            {};
            /**
             * @brief Function for giving education to object of <b>class Human</b>
             *
             * Will change education to "High education"
             * @param [in] human - person whose education will be changed
             */
            void give_education(Human::Human& human) { human.receive_education("High education"); };
            std::string get_university_name() { return university_name; };
            Faculty get_faculty() { return Faculty::get_faculty(); };
    };


    class Supervisor : public virtual Human::Human
    {
        private:
            std::string post;
        public:
            /**
             * @brief class Supervisor constructor
             * @param [in] name_of_person - name of specified supervisor
             * @param [in] education_of_person - education of specified supervisor
             * @param [in] post - post of specified supervisor
    */
            Supervisor(std::string name_of_person, std::string education_of_person, std::string post_of_person):
                Human::Human(name_of_person, education_of_person), post(post_of_person)
            {};
            /**
             * @brief function for checking attendance
             * @param [in] size_of_group - number of students in list of group
             * @param [in] present_students - number of students who present in lesson
             * @param [out] number of students who absent
             */
            int check_attendance(int size_of_group, int present_students) { return size_of_group - present_students; };
    };


    class Student : public virtual Human::Human
    {
        protected:
            int id;
            University university;
            Faculty faculty;
        public:
            /**
             * @brief class Student constructor
             * @param [in] name_of_person - name of specified person
             * @param [in] id_of_student - id number of specified student
             * @param [in] university_of_student - university where person studies
             * @param [in] faculty_of_student - faculty where person studies
             */
            Student(std::string name_of_person, int id_of_student, const University& university_of_student, const Faculty& faculty_of_student):
                Human::Human(name_of_person), id(id_of_student), university(university_of_student), faculty(faculty_of_student)
            {};
            int get_id() { return this->id; };
            University get_university() { return this->university; };
            Faculty get_faculty() { return this->faculty; };
    };


    class Group_monitor : public Student, protected Supervisor
    {
        public:
            /**
             * @brief class Group_monitor constructor
             * @param [in] name_of_person - name of specified person
             * @param [in] id_of_student - id number of specified student
             * @param [in] university_of_student - university where person studies
             * @param [in] faculty_of_student - faculty where person studies
             */
            Group_monitor(std::string name_of_person, int id_of_student, const University& university_of_student, const Faculty& faculty_of_student):
                Human::Human(name_of_person), Student(name_of_person, id_of_student, university_of_student, faculty_of_student),
                Supervisor(name_of_person, "", "")
            {};
            int check_attendance(int size_of_group, int present_students) { return Supervisor::check_attendance(size_of_group, present_students); };
    };
}
#endif
