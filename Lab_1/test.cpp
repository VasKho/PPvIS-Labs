#define CATCH_CONFIG_MAIN
#include "large.hpp"
#include <catch2/catch.hpp>

TEST_CASE("Comparison for Large?Large")
{
    Large number_1("452111231412432412");
    Large number_2("12345678910");
    Large number_3("12345678910");

    REQUIRE((number_1 == number_2) == false);
    
    REQUIRE((number_2 == number_3) == true);

    REQUIRE((number_1 > number_2) == true);

    REQUIRE((number_2 >= number_3) == true);

    REQUIRE((number_2 > number_1) == false);

    REQUIRE((number_1 < number_2) == false);

    REQUIRE((number_2 <= number_3) == true);

    REQUIRE((number_2 < number_1) == true);
}

TEST_CASE("Comparison")
{
    Large number_1("452111231412432412");
    Large number_2("12345678910");
    Large number_3("12345678910");

    REQUIRE((number_1 > number_2) == true);

    REQUIRE((number_2 >= number_3) == true);

    REQUIRE((number_1 < number_2) == false);

    REQUIRE((number_2 <= number_3) == true);

    REQUIRE((number_2 < number_1) == true);
}

TEST_CASE("Comparison for Large?int")
{
    Large number_1("21673843327782823");
    int number_2 = 1234341;
    Large number_3("-1234341");

    REQUIRE((number_1 == number_2) == false);

    REQUIRE((number_1 != number_2) == true);

    REQUIRE((number_1 > number_2) == true);

    REQUIRE((number_1 >= number_2) == true);

    REQUIRE((number_1 < number_2) == false);

    REQUIRE((number_2 == number_3) == false);
}

TEST_CASE("Comparison_2")
{
    Large number_1("21673843327782823");
    int number_2 = 1234341;
    Large number_3("-1234341");

    REQUIRE((number_1 != number_2) == true);

    REQUIRE((number_1 > number_2) == true);

    REQUIRE((number_1 < number_2) == false);

    REQUIRE((number_2 == number_3) == false);
}

TEST_CASE("Addition for Large + Large")
{
    Large number_1("542212143432");
    Large number_2("-233354334233234");
    Large number_3("-232812122089802");
    Large number_4("336432344");
    Large number_5("542548575776");

    REQUIRE((number_1 + number_2) == number_3);

    REQUIRE((number_1 + number_4) == number_5);

    REQUIRE((number_2 + number_1) == number_3);
}

TEST_CASE("Addition for")
{
    Large number_1("9874661155");
    Large number_2("-78943224");
    Large number_3("35733542");
    Large number_4("9874707742");

    REQUIRE((number_1 + 46587) == number_4);

    REQUIRE((number_2 + 874236552) == 795293328);

    REQUIRE((number_3 + (-654788221)) == -619054679);

    REQUIRE((number_1 + 0) == number_1);
}

TEST_CASE("Addition for Large + int")
{
    Large number_1("9874661155");
    Large number_2("-78943224");
    Large number_3("35733542");
    Large number_4("9874707742");

    REQUIRE((number_2 + 874236552) == 795293328);

    REQUIRE((number_1 + 0) == number_1);
}

TEST_CASE("Subtraction for Large - Large")
{
    Large number_1("45687883");
    Large number_2("-78946");
    Large number_3("-1336448");
    Large number_4("78961166");

    REQUIRE((number_1 - number_4) == -33273283);

    REQUIRE((number_2 - number_3) == 1257502);

    REQUIRE((number_2 - number_4) == -79040112);

    REQUIRE((number_1 - number_2) == 45766829);
}

TEST_CASE("Subtraction for Large - int")
{
    Large number_1("45677");
    Large number_2("-6554371");

    REQUIRE((number_1 - 15366547) == -15320870);

    REQUIRE((-7991332 - number_1) == -8037009);

    REQUIRE((number_2 - (-9987460)) == 3433089);
}

TEST_CASE("Multiplication for Large * Large")
{
    Large number_1("-7894");
    Large number_2("196436546");
    Large number_3("-15365");
    Large number_4("0");
    Large number_5("-1550670094124");

    REQUIRE((number_1 * number_2) == number_5);

    REQUIRE((number_1 * number_4) == 0);

    REQUIRE((number_1 * number_3) == 121291310);
}

TEST_CASE("Multiplication for Large")
{
    Large number_1("-7894");
    Large number_2("196436546");
    Large number_3("-15365");
    Large number_4("0");
    Large number_5("-1550670094124");

    REQUIRE((number_1 * number_2) == number_5);

    REQUIRE((number_1 * number_3) == 121291310);
}

TEST_CASE("Multiplication test for Large * int")
{
    Large number_1("-79164");
    Large number_2("651570");

    REQUIRE((number_1 * 5) == -395820);

    REQUIRE((number_2 * -791) == -515391870);

    REQUIRE((number_1 * -70) == 5541480);
}

TEST_CASE("Division test for Large / Large")
{
    Large number_1("12345234223");
    Large number_2("123");
    Large number_3("-56645488");

    REQUIRE((number_1 / number_2) == 100367757);

    REQUIRE((number_2 / number_1) == 0);

    REQUIRE((number_1 / number_3) == -217);
}

TEST_CASE("Division test for Large")
{
    Large number_1("238934794576");
    Large number_2("-564");
    Large number_3("-1365466");

    REQUIRE((number_1 / 6548823) == 36485);

    REQUIRE((number_2 / 1000) == 0);

    REQUIRE((number_3 / -564) == 2421);

    REQUIRE((number_1 / -456778912) == -523);
}

TEST_CASE("Division test for Large / int")
{
    Large number_1("238934794576");
    Large number_2("-564");
    Large number_3("-1365466");

    REQUIRE((number_1 / 6548823) == 36485);

    REQUIRE((number_3 / -564) == 2421);
}

TEST_CASE("Sum with assignment for Large += Large")
{
    Large number_1("542212143432");
    Large number_2("-233354334233234");
    Large number_3("542548575776");

    REQUIRE((number_1 += number_2) == number_1);

    REQUIRE((number_2 += number_3) == number_2);

    REQUIRE((number_2 += number_1) == number_2);
}

TEST_CASE("Sum with assignment for Large += int")
{
    Large number_1("9874661155");
    Large number_2("-78943224");
    Large number_3("35733542");

    REQUIRE((number_1 += 46587) == number_1);

    REQUIRE((number_2 += 874236552) == number_2);

    REQUIRE((number_3 += (-654788221)) == number_3);

    REQUIRE((number_1 += 0) == number_1);
}

TEST_CASE("Subtraction with assignment for Large -= Large")
{
    Large number_1("45677");
    Large number_2("-6554371");

    REQUIRE((number_1 -= 15366547) == number_1);

    REQUIRE((number_2 -= (-9987460)) == number_2);
}

TEST_CASE("Multiplication with assignment for Large *= Large")
{
    Large number_1("-7894");
    Large number_2("196436546");
    Large number_3("-15365");
    Large number_4("0");

    REQUIRE((number_1 *= number_2) == number_1);

    REQUIRE((number_1 *= number_4) == number_1);

    REQUIRE((number_3 *= number_2) == number_3);
}

TEST_CASE("Multiplication with assignment for Large *= int")
{
    Large number_1("-79164");
    Large number_2("651570");

    REQUIRE((number_1 *= 5) == number_1);

    REQUIRE((number_2 *= -791) == number_2);

    REQUIRE((number_1 *= -70) == number_1);
}

TEST_CASE("Division with assignment for Large / Large")
{
    Large number_1("12345234223");
    Large number_2("123");
    Large number_3("-56645488");

    REQUIRE((number_1 /= number_2) == number_1);

    REQUIRE((number_2 /= number_1) == number_2);

    REQUIRE((number_1 /= number_3) == number_1);
}

TEST_CASE("Division with assignment for Large")
{
    Large number_1("12345234223");
    Large number_2("123");
    Large number_3("-56645488");

    REQUIRE((number_2 /= number_1) == number_2);

    REQUIRE((number_1 /= number_3) == number_1);
}

TEST_CASE("Division with assignment for Large /= int")
{
    Large number_1("238934794576");
    Large number_2("-564");
    Large number_3("-1365466");

    REQUIRE((number_1 /= 6548823) == number_1);

    REQUIRE((number_2 /= 1000) == number_2);

    REQUIRE((number_3 /= -564) == number_3);

    REQUIRE((number_1 /= -456778912) == number_1);
}

TEST_CASE("Increment")
{
    Large number_1("-1");
    Large number_2("2411345");

    REQUIRE(number_1++ == -1);

    REQUIRE(number_1 == 0);

    REQUIRE(number_2++ == 2411345);

    REQUIRE(number_2 == 2411346);

    REQUIRE(++number_1 == 1);

    REQUIRE(++number_2 == 2411347);
}

TEST_CASE("Increment_2")
{
    Large number_1("-1");
    Large number_2("2411345");

    REQUIRE(number_2++ == 2411345);

    REQUIRE(number_2 == 2411346);

    REQUIRE(++number_1 == 0);

    REQUIRE(++number_2 == 2411347);
}

TEST_CASE("Decrement")
{
    Large number_1("-1");
    Large number_2("2411345");

    REQUIRE(number_1-- == -1);

    REQUIRE(number_1 == -2);

    REQUIRE(number_2-- == 2411345);

    REQUIRE(number_2 == 2411344);

    REQUIRE(--number_1 == -3);

    REQUIRE(--number_2 == 2411343);
}

TEST_CASE("Decrement_2")
{
    Large number_1("-1");
    Large number_2("2411345");

    REQUIRE(number_1-- == -1);

    REQUIRE(number_1 == -2);

    REQUIRE(number_2-- == 2411345);

    REQUIRE(--number_2 == 2411343);
}

TEST_CASE("Converting")
{
    Large number_1("791136554");
    Large number_2("-781235");
    Large number_3("16677664445513");

    REQUIRE((int)number_1 == 791136554);

    REQUIRE((int)number_2 == -781235);

    REQUIRE((int)number_3 == 1667766444);
}

TEST_CASE("Converting_2")
{
    Large number_1("791136554");
    Large number_2("-781235");
    Large number_3("16677664445513");

    REQUIRE((int)number_2 == -781235);

    REQUIRE((int)number_3 == 1667766444);
}

TEST_CASE("Input/Output test")
{
    Large number_1;

    std::ostringstream out;
    std::istringstream in("12345");
    in >> number_1;
    out << number_1;

    REQUIRE(number_1 == 12345);

    REQUIRE(out.str() == "12345");
}
