#ifndef _CALCULATOR_H_
#define _CALCULATOR_H_

#define PROMPT_SYMBOL "> "

#include <iostream>
#include <map>
#include <regex>
#include "tree.hpp"


class Parsing_tree
{
    private:
        std::shared_ptr<Node> tree;
        std::shared_ptr<Node> current_position;
    public:
        Parsing_tree();
        void set_current_position(std::shared_ptr<Node> new_pos) { this->current_position = new_pos; };
        void set_tree(std::shared_ptr<Node> new_tree) { this->tree = new_tree; };
        std::shared_ptr<Node> get_current_position() { return this->current_position; };
        std::shared_ptr<Node> get_tree() { return this->tree; };
};


class Calculator
{
    private:
        static std::map<std::string, std::string> variables;
        static bool check_input(std::string);
    public:
        static void start_dialog(std::istream&, std::ostream&);
        static void parse_expression(std::string, Parsing_tree&, std::string="null");
        static void process_input(std::string, std::ostream&);
        static void add_to_memory(std::string, std::string = "");
        static void print_memory(std::ostream&);
        static void print_result(Parsing_tree&, std::ostream&);
};

#endif
