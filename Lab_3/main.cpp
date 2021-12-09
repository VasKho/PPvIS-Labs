#include "calculator.hpp"
#include "grammar.hpp"
/* #include "tree.hpp" */
#include <iostream>


/* void print(std::shared_ptr<Node> rt, int depth=0) */
/* { */
/*     std::string str; */
/*     if (rt != nullptr) */
/*     { */
/*         print(rt->get_right_child(), depth + 1); */
/*         for (int i = 0; i < depth; i++) str += "    "; */
/*         std::cout << str << rt->get_value() << std::endl; */
/*         print(rt->get_left_child(), depth + 1); */
/*     } */
/* } */

int main()
{
    /* std::shared_ptr<Node> root = std::make_shared<Add_node>(); */
    /* root->get_left_child() = std::shared_ptr<Add_node>(); */
    /* print(root); */

    Calculator::start_dialog(std::cin, std::cout);
    return 0;
}
