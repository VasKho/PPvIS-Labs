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

    REQUIRE(some_unit.get_unit_director() == "unit director");

    some_unit.appoint_unit_director("new_director_name");

    REQUIRE(some_unit.get_unit_director() == "new_director_name");
}


TEST_CASE("Faculty test")
{
    University::Faculty test_5("Name_of_faculty", "university_name", "unit_director_name", "university_director_name");

    REQUIRE(test_5.get_unit_director() == "unit_director_name");

    test_5.appoint_unit_director("new");

    REQUIRE(test_5.get_unit_director() == "new");
}


TEST_CASE("Student test")
{
    University::University test_4("University name", "Director name");
    University::Student person_1("Some_name", 12345, test_4, test_4.get_faculty());

    REQUIRE(person_1.get_faculty().get_faculty_name() == test_4.get_faculty().get_faculty_name());

    REQUIRE(person_1.get_id() == 12345);

    REQUIRE(person_1.get_university().get_university_name() == test_4.get_university_name());

    REQUIRE(person_1.get_name() == "Some_name");

    REQUIRE(person_1.get_education() == "");
}


TEST_CASE("Group_monitor test")
{
    University::University test_4("University name", "Director name");
    University::Group_monitor person_1("Some_name", 12345, test_4, test_4.get_faculty());

    REQUIRE(person_1.check_attendance(13, 5) == 8);

    REQUIRE(person_1.get_education() == "");

    REQUIRE(person_1.get_university().get_university_name() == test_4.get_university_name());
}
