#include "university.hpp"


int main()
{
    Government_establishments::Government_establishments a("Some department", "Director of some department");
    Government_establishments::Educational_establishment b("University", "Director of university");
    University::University c("Name of university", "Its director");
    University::Structural_units_of_university d("Faculty", "Name of university", "Faculty director", "University director");
    University::Faculty e("Faculty name", "University name", "Faculty director", "University director");
    University::Military_faculty unit("Name of university", "Name of faculty dir", "uni director name");
    std::cout << "Educational_establishment test" << std::endl;
    std::cout << b.get_director() << std::endl;
    b.appoint_director("director = new director");
    std::cout << b.get_director() << std::endl;
    std::cout << "University test" << std::endl;
    std::cout << c.get_director() << std::endl;
    c.appoint_director("New director name");
    std::cout << c.get_director() << std::endl;
    std::cout << "Military_faculty test" << std::endl;
    std::cout << unit.get_unit_director() << std::endl;
    unit.appoint_unit_director("New unit director");
    std::cout << unit.get_unit_director() << std::endl;
    std::cout << unit.get_director() << std::endl;
    unit.appoint_director("new university director");
    std::cout << unit.get_director() << std::endl;
    Human::Human person_1("Some_name");
    c.give_education(person_1);
    std::cout << person_1.get_education() << std::endl;
    return 0;
}
