#include <regex>
#include "grammar.hpp"


int find_operator_position(std::string input)
{
    //1+4-9*(4/2)
    int parenthesis_number = 0;
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] == '(') ++parenthesis_number;
        if (input[i] == ')')
        {
            --parenthesis_number;
            if (parenthesis_number < 0) throw std::invalid_argument("Brackets parsing error");
        }
    }
    if (parenthesis_number != 0) throw std::invalid_argument("Brackets parsing error");
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] == '(') ++parenthesis_number;
        if (input[i] == ')') --parenthesis_number;
        if (input[i] == '+' && parenthesis_number == 0) return i;
    }
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] == '(') ++parenthesis_number;
        if (input[i] == ')') --parenthesis_number;
        if ((input[i] == '*' || input[i] == '/') && parenthesis_number == 0) return i;
    }
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] == '(') ++parenthesis_number;
        if (input[i] == ')') --parenthesis_number;
        if (input[i] == '+' && parenthesis_number == 1) return i;
    }
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] == '(') ++parenthesis_number;
        if (input[i] == ')') --parenthesis_number;
        if ((input[i] == '*' || input[i] == '/') && parenthesis_number == 1) return i;
    }
    return -1;
}


bool check_input(std::string expr)
{ 
    std::string error_msg;
    std::string allowed_symbols = "qwertyuiopasdfghjklzxcvbnm1234567890(),./*-+=_^";
    for (auto i : expr) if (allowed_symbols.find(i) > allowed_symbols.length()) 
    {
        error_msg = "Unexpected symbol '";
        error_msg += i;
        error_msg += '\'';
    }
    if (std::regex_match(expr, std::regex("((_?[a-z|A-Z]+_?\\d*)|((\\-?[1-9]\\d*(\\.\\d+)?)|(\\-?0\\.\\d+)|0))=(_?[a-z|A-Z]+_?\\d*)")))
        error_msg = "Invalid statement '<variable>=<variable>' or '<number>=<variable>'";
    if (std::regex_match(expr, std::regex("((\\-?[1-9]\\d*(\\.\\d+)?)|(\\-?0\\.\\d+)|0)=((\\-?[1-9]\\d*(\\.\\d+)?)|(\\-?0\\.\\d+)|0)")))
        error_msg = "Invalid statement '<number>=<number>'";
    if (expr.find("=") != expr.rfind("="))
        error_msg = "Invalid statement. Two or more '=' signs";
    if (std::regex_search(expr, std::regex("\\(\\)")))
        error_msg = "Empty parenthesis";
    if (!error_msg.empty()) throw std::invalid_argument(error_msg);
    return true;
}
