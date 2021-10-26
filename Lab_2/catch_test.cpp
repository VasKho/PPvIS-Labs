#define CATCH_CONFIG_MAIN
#include "university.hpp"
#include <catch2/catch.hpp>

TEST_CASE("Government_Establishment test")
{
    Government_establishments::Government_establishments test_1("Test_establishment", "Test_director");

    REQUIRE(test_1.get_director() == "Test_director");

    test_1.appoint_director("New test director");

    REQUIRE(test_1.get_director() == "New test director");
}


TEST_CASE("Educational_establishment test")
{
    Government_establishments::Educational_establishment test_2("Test_type_of_establishment", "director name");

    REQUIRE(test_2.get_director() == "director name");

    REQUIRE(test_2.get_type_of_educational_establishment() == "Test_type_of_establishment");
}


TEST_CASE("Ministry_of_defence test")
{
    Government_establishments::Ministry_of_defence test_3("Director_name");

    REQUIRE(test_3.get_director() == "Director_name");

    Human::Soldier person_2("Test_name", "Test_rank");

    test_3.give_a_rank(person_2, "New rank");

    REQUIRE(person_2.get_rank() == "New rank");
}


TEST_CASE("Soldier tests")
{
    Human::Soldier person_1("Name", "Rank", "Education");

    REQUIRE(person_1.get_name() == "Name");

    REQUIRE(person_1.get_rank() == "Rank");

    REQUIRE(person_1.get_education() == "Education");
}


TEST_CASE("University test")
{
    University::University test_4("University name", "Director name"); 

    REQUIRE(test_4.get_director() == "Director name");

    REQUIRE(test_4.get_university_name() == "University name");
    
    REQUIRE(test_4.get_type_of_educational_establishment() == "University");

    Human::Human person_test("Name", "current_education");

    test_4.give_education(person_test);

    REQUIRE(person_test.get_education() == "High education");

    test_4.appoint_director("new_director_name");

    REQUIRE(test_4.get_director() == "new_director_name");
}


TEST_CASE("Structural_units_of_university test")
{
    University::Structural_units_of_university some_unit("Type_of_unit", "Name of owner establishment", "unit director", "Establishment director");

    REQUIRE(some_unit.get_establishment_director() == "Establishment director");

    REQUIRE(some_unit.get_unit_director() == "unit director");

    some_unit.appoint_unit_director("new_director_name");

    REQUIRE(some_unit.get_unit_director() == "new_director_name");
}


TEST_CASE("Faculty test")
{
    University::Faculty test_5("Name_of_faculty", "university_name", "unit_director_name", "university_director_name");

    REQUIRE(test_5.get_unit_director() == "unit_director_name");

    REQUIRE(test_5.get_establishment_director() == "university_director_name");

    test_5.appoint_unit_director("new");

    REQUIRE(test_5.get_unit_director() == "new");
}


TEST_CASE("Military_faculty test")
{
    University::Military_faculty test_6("University_name", "Faculty_director", "University_director");

    REQUIRE(test_6.get_unit_director() == "Faculty_director");

    REQUIRE(test_6.get_establishment_director() == "University_director");

    test_6.appoint_unit_director("new_faculty_director_name");

    REQUIRE(test_6.get_unit_director() == "new_faculty_director_name");

    Human::Soldier test_soldier("Name", "Rank");
    
    test_6.change_rank(test_soldier, "New_Rank");

    REQUIRE(test_soldier.get_rank() == "New_Rank");
}
