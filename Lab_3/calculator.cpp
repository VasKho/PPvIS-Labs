#include <iostream>
#include <regex>
#include "calculator.hpp"
#include "grammar.hpp"
#include "tree.hpp"


void print(std::shared_ptr<Node> rt, int depth=0)
{
    std::string str;
    if (rt != nullptr)
    {
        print(rt->get_right_child(), depth + 1);
        for (int i = 0; i < depth; i++) str += "    ";
        std::cout << str << rt->get_value() << std::endl;
        print(rt->get_left_child(), depth + 1);
    }
}


Parsing_tree::Parsing_tree()
{
    this->tree = nullptr;
    this->current_position = this->tree;
}


std::map<std::string, std::string> Calculator::variables;

void Calculator::start_dialog(std::istream& input_stream, std::ostream& output_stream)
{
    Calculator::variables = {};
    while (true)
    {
        try
        {
            std::string expression;
            output_stream << PROMPT_SYMBOL;
            std::getline(input_stream, expression);
            if (expression == "quit") return;  
            process_input(expression, output_stream);
        }
        catch (std::invalid_argument& ex)
        {
            output_stream << ex.what() << std::endl;
            continue;
        }
    }
}


void Calculator::process_input(std::string expression, std::ostream& output_stream)
{
    if (expression == "help")
    {
        output_stream << "print 'memprint' to show all available variables in memory" << std::endl;
        output_stream << "print 'help' to show this message" << std::endl;
        output_stream << "print 'quit' to end dialog" << std::endl;
        return;
    }
    if (expression == "memprint")
    {
        print_memory(std::cout);
        return;
    }
    if (std::regex_match(expression, std::regex("^(_?[a-z|A-Z]+_?\\d*)=((\\-?[1-9]\\d*(\\.\\d+)?)|(\\-?0\\.\\d+)|0)$")))
    {
        std::string var_name = "";
        std::string var_value = "";
        int i = 0;
        for (; expression[i] != '='; ++i) var_name += expression[i];
        ++i;
        for (; i < expression.length(); ++i) var_value += expression[i];
        add_to_memory(var_name, var_value);
        return;
    }
    if (std::regex_match(expression, std::regex(ALLOWED_OPERANDS_REGEXP))) expression = "0" + expression;
    expression.erase(std::remove_if(expression.begin(), expression.end(), ::isspace), expression.end());
    std::string result;
    std::regex_replace(std::back_inserter(result), expression.begin(), expression.end(), std::regex("-"),  "+-");

    check_input(result);
    if (result[0] == '+') result.erase(0, 1);
    
    Parsing_tree expression_1;
    parse_expression(result, expression_1);
    print(expression_1.get_tree());
    print_result(expression_1, std::cout);
    print(expression_1.get_tree());
}


void Calculator::parse_expression(std::string expression, Parsing_tree& expression_tree, std::string where)
{
    if (std::regex_match(expression, std::regex("^-?\\(((_?[a-z|A-Z]+_?\\d*)|((\\-?[1-9]\\d*(\\.\\d+)?)|(\\-?0\\.\\d+)|0))([\\+\\-\\*\\/]((_?[a-z|A-Z]+_?\\d*)|((\\-?[1-9]\\d*(\\.\\d+)?)|(\\-?0\\.\\d+)|0)))*\\)$"))) 
    {
        if (expression[0] == '-')
        {
            for (int i = 1; i < expression.length(); ++i)
            {
                if (expression[i] == '+' && expression[i+1] == '-') expression.erase(i+1, 1);
                else if (expression[i] == '+') expression.insert(i+1, "-");
            }
            if (expression[2] != '-') expression.erase(1, 1);
            else expression.erase(0, 2);
            expression.erase(expression.length() - 1, 1);
        }
        else expression = expression.substr(1, expression.length() - 2);
    }
    int split_position = find_operator_position(expression);
    //1+4-9*(4/2)
    if (split_position != -1)
    {
        std::shared_ptr<Node> new_node = expression_tree.get_current_position();
        switch (expression[split_position])
        {
            case Operators::ADD: 
                if (expression_tree.get_current_position() == nullptr) expression_tree.set_current_position(std::make_shared<Add_node>());
                else new_node = std::make_shared<Add_node>();
                break;
            case Operators::MULTIPLY:
                if (expression_tree.get_current_position() == nullptr) expression_tree.set_current_position(std::make_shared<Multiply_node>());
                else new_node = std::make_shared<Multiply_node>();
                break;
            case Operators::DIVIDE:
                if (expression_tree.get_current_position() == nullptr) expression_tree.set_current_position(std::make_shared<Divide_node>());
                else new_node = std::make_shared<Divide_node>();
                break;
        }

        if (where == "left")
        {
            expression_tree.get_current_position()->set_left_child(new_node);
            expression_tree.get_current_position()->get_left_child()->set_parent(expression_tree.get_current_position());
            expression_tree.set_current_position(expression_tree.get_current_position()->get_left_child());
        }
        else if (where == "right")
        {
            expression_tree.get_current_position()->set_right_child(new_node);
            expression_tree.get_current_position()->get_right_child()->set_parent(expression_tree.get_current_position());
            expression_tree.set_current_position(expression_tree.get_current_position()->get_right_child());
        }

        if (expression_tree.get_tree() == nullptr) expression_tree.set_tree(expression_tree.get_current_position());

        std::shared_ptr<Node> temp = expression_tree.get_current_position();
        if (std::regex_match(expression.substr(0, split_position), std::regex(ALLOWED_OPERANDS_REGEXP)))
            expression_tree.get_current_position()->insert_left(expression.substr(0, split_position));
        else 
        {
            parse_expression(expression.substr(0, split_position), expression_tree, "left");
            expression_tree.set_current_position(temp);
        }

        if (std::regex_match(expression.substr(split_position + 1), std::regex(ALLOWED_OPERANDS_REGEXP)))
            expression_tree.get_current_position()->insert_right(expression.substr(split_position + 1));
        else 
        {
            parse_expression(expression.substr(split_position + 1), expression_tree, "right");
            expression_tree.set_current_position(temp);
        }
    }
}


void Calculator::print_result(Parsing_tree& expr_tree, std::ostream& out_stream)
{
    if (expr_tree.get_current_position() == nullptr) return;
    // If left child of current position is operator then evaluate left child
    if (!std::regex_match(expr_tree.get_current_position()->get_left_child()->get_value(), std::regex(ALLOWED_OPERANDS_REGEXP)))
    {
        expr_tree.set_current_position(expr_tree.get_current_position()->get_left_child());
        print_result(expr_tree, out_stream);
    }
    // If right child of current position is operator then evaluate right child
    if (!std::regex_match(expr_tree.get_current_position()->get_right_child()->get_value(), std::regex(ALLOWED_OPERANDS_REGEXP)))
    {
        expr_tree.set_current_position(expr_tree.get_current_position()->get_right_child());
        print_result(expr_tree, out_stream);
    }
    // If left child of current position is variable then search it in memory
    if (std::regex_match(expr_tree.get_current_position()->get_left_child()->get_value(), std::regex(VARIABLES_REGEXP)))
    {
        if (Calculator::variables.find(expr_tree.get_current_position()->get_left_child()->get_value()) != Calculator::variables.end())
        {
            std::string variable = expr_tree.get_current_position()->get_left_child()->get_value();
            std::string value;
            if (variable[0] == '-') value = Calculator::variables.at(variable.substr(1));
            else value = Calculator::variables.at(variable);
            expr_tree.get_current_position()->get_left_child()->set_value(value);
        }
        else throw std::invalid_argument("Variable has no value");
    }

    // If right child of current position is variable then search it in memory
    if (std::regex_match(expr_tree.get_current_position()->get_right_child()->get_value(), std::regex(VARIABLES_REGEXP)))
    {
        if (Calculator::variables.find(expr_tree.get_current_position()->get_right_child()->get_value()) != Calculator::variables.end())
        {
            std::string variable = expr_tree.get_current_position()->get_right_child()->get_value();
            std::string value;
            if (variable[0] == '-') value = Calculator::variables.at(variable.substr(1));
            else value = Calculator::variables.at(variable);
            expr_tree.get_current_position()->get_right_child()->set_value(value);
        }
        else throw std::invalid_argument("Variable has no value");
    }
    // If everything is ok then just evaluate current position
    expr_tree.get_current_position()->evaluate();
    expr_tree.set_current_position(expr_tree.get_current_position()->get_parent());
}


void Calculator::add_to_memory(std::string variable_name, std::string variable_value)
{
    Calculator::variables.insert(std::pair<std::string, std::string> (variable_name, variable_value));
}

void Calculator::print_memory(std::ostream& output_stream)
{
    for (auto i: Calculator::variables)
        output_stream << "  " << i.first << '=' << i.second << std::endl;
}
