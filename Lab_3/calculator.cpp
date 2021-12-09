#include <iostream>
#include <stack>
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


bool Calculator::check_input(std::string expr)
{
    expr.erase(std::remove_if(expr.begin(), expr.end(), ::isspace), expr.end());
    std::string error_msg;
    std::string allowed_symbols = "qwertyuiopasdfghjklzxcvbnm1234567890(),./*-+=_^";
    for (auto i : expr) if (allowed_symbols.find(i) > allowed_symbols.length()) 
    {
        error_msg = "Unexpected symbol '";
        error_msg += i;
        error_msg += '\'';
    }
    if (std::regex_match(expr, std::regex("((_?[a-z|A-Z]+_?\\d*)|\\d+)=_?[a-z|A-Z]+_?\\d*"))) 
        error_msg = "Invalid statement '<variable>=<variable>' or '<number>=<variable>'";
    if (std::regex_match(expr, std::regex("\\d+=\\d+")))
        error_msg = "Invalid statement '<number>=<number>'";
    if (expr.find("=") != expr.rfind("="))
        error_msg = "Invalid statement. Two or more '=' signs";
    if (!error_msg.empty()) throw std::invalid_argument(error_msg);
    return true;
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
    if (expression == "memprint") print_memory(std::cout);
    check_input(expression);
    if (std::regex_match(expression, std::regex("_?\\w+_?\\d*=\\d+")))
    {
        std::string var_name = "";
        std::string var_value = "";
        int i = 0;
        for (; expression[i] != '='; ++i) var_name += expression[i];
        ++i;
        for (; i < expression.length(); ++i) var_value += expression[i];
        add_to_memory(var_name, var_value);
    }
    Parsing_tree expression_1;
    parse_expression(expression, expression_1);
    print_result(expression_1, std::cout);
    print(expression_1.get_tree());
}


void Calculator::parse_expression(std::string expression, Parsing_tree& expression_tree, std::string where)
{
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
            case Operators::SUBTRACT:
                if (expression_tree.get_current_position() == nullptr) expression_tree.set_current_position(std::make_shared<Subtract_node>());
                else new_node = std::make_shared<Subtract_node>();
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
        if (std::regex_match(expression.substr(0, split_position), std::regex("((_?[a-z|A-Z]+_?\\d*)|\\d+)")))
            expression_tree.get_current_position()->insert_left(expression.substr(0, split_position));
        else 
        {
            parse_expression(expression.substr(0, split_position), expression_tree, "left");
            expression_tree.set_current_position(temp);
        }

        if (std::regex_match(expression.substr(split_position + 1), std::regex("((_?[a-z|A-Z]+_?\\d*)|\\d+)")))
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
    if (!std::regex_match(expr_tree.get_current_position()->get_left_child()->get_value(), std::regex("((_?[a-z|A-Z]+_?\\d*)|\\d+)")))
    {
        expr_tree.set_current_position(expr_tree.get_current_position()->get_left_child());
        print_result(expr_tree, out_stream);
    }
    if (!std::regex_match(expr_tree.get_current_position()->get_right_child()->get_value(), std::regex("((_?[a-z|A-Z]+_?\\d*)|\\d+)")))
    {
        expr_tree.set_current_position(expr_tree.get_current_position()->get_right_child());
        print_result(expr_tree, out_stream);
    }
    if (std::regex_match(expr_tree.get_current_position()->get_left_child()->get_value(), std::regex("(_?[a-z|A-Z]+_?\\d*)")))
        if (Calculator::variables.find(expr_tree.get_current_position()->get_left_child()->get_value()) != Calculator::variables.end())
            expr_tree.get_current_position()->get_left_child()->set_value(Calculator::variables.at(expr_tree.get_current_position()->get_left_child()->get_value()));

    if (std::regex_match(expr_tree.get_current_position()->get_right_child()->get_value(), std::regex("(_?[a-z|A-Z]+_?\\d*)")))
        if (Calculator::variables.find(expr_tree.get_current_position()->get_right_child()->get_value()) != Calculator::variables.end())
        expr_tree.get_current_position()->get_right_child()->set_value(Calculator::variables.at(expr_tree.get_current_position()->get_right_child()->get_value()));
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
