#include <regex>
#include "grammar.hpp"


int find_operator_position(std::string& input)
{
    //1+4-9*(4/2)
    if (std::regex_match(input, std::regex("\\(((_?[a-z|A-Z]+_?\\d*)|\\d+)[\\+\\-\\*\\/]((_?[a-z|A-Z]+_?\\d*)|\\d+)\\)")))
        input = input.substr(1, input.length() - 2);
    int parenthesis_number = 0;
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] == '(') ++parenthesis_number;
        if (input[i] == ')')
        {
            --parenthesis_number;
            if (parenthesis_number < 0) throw std::invalid_argument("Brackets parsing error at position: " + std::to_string(i+1));
        }
        if ((input[i] == '+' || input[i] == '-') && parenthesis_number == 0) return i;
    }
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] == '(') ++parenthesis_number;
        if (input[i] == ')')
        {
            --parenthesis_number;
            if (parenthesis_number < 0) throw std::invalid_argument("Brackets parsing error at position: " + std::to_string(i+1));
        }
        if ((input[i] == '*' || input[i] == '/') && parenthesis_number == 0) return i;
    }
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] == '(') ++parenthesis_number;
        if (input[i] == ')')
        {
            --parenthesis_number;
        if (parenthesis_number < 0) throw std::invalid_argument("Brackets parsing error at position: " + std::to_string(i+1));
        }
        if ((input[i] == '+' || input[i] == '-') && parenthesis_number == 1) return i;
    }
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] == '(') ++parenthesis_number;
        if (input[i] == ')')
        {
            --parenthesis_number;
            if (parenthesis_number < 0) throw std::invalid_argument("Brackets parsing error at position: " + std::to_string(i+1));
        }
        if ((input[i] == '*' || input[i] == '/') && parenthesis_number == 1) return i;
    }
    return -1;
}
