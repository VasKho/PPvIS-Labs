#include "tree.hpp"


Node::Node()
{
    this->parent = nullptr;
    this->left_child = nullptr;
    this->right_child = nullptr;
}

Node::Node(std::string val): value(val)
{
    this->parent = nullptr;
    this->left_child = nullptr;
    this->right_child = nullptr;
}

void Node::insert_left(std::string left_value) { this->left_child = std::make_shared<Node>(left_value); }

void Node::insert_right(std::string right_value) { this->right_child = std::make_shared<Node>(right_value); }


void Add_node::evaluate()
{
    double result = std::stod(left_child->get_value()) + std::stod(right_child->get_value());
    this->value = std::to_string(result);
    this->left_child = nullptr;
    this->right_child = nullptr;
}

void Multiply_node::evaluate()
{
    double result = std::stod(left_child->get_value()) * std::stod(right_child->get_value());
    this->value = std::to_string(result);
    this->left_child = nullptr;
    this->right_child = nullptr;
}

void Divide_node::evaluate()
{
    double result = std::stod(left_child->get_value()) / std::stod(right_child->get_value());
    this->value = std::to_string(result);
    this->left_child = nullptr;
    this->right_child = nullptr;
}
