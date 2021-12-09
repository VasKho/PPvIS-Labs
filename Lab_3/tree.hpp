#ifndef _TREE_H_
#define _TREE_H_
#include <memory>
#include <iostream>


enum Operators
{
    ADD = '+',
    SUBTRACT = '-',
    MULTIPLY = '*',
    DIVIDE = '/'
};

class Node
{
    protected:
        std::shared_ptr<Node> parent;
        std::shared_ptr<Node> left_child;
        std::shared_ptr<Node> right_child;
        std::string value;
    public:
        Node();
        Node(std::string);
        void insert_left(std::string);
        void insert_right(std::string);
        void set_parent(std::shared_ptr<Node> parent) { this->parent = parent; };
        void set_left_child(std::shared_ptr<Node> new_child) { this->left_child = new_child; };
        void set_right_child(std::shared_ptr<Node> new_child) { this->right_child = new_child; };
        void set_value (std::string new_value) { this->value = new_value; };
        std::shared_ptr<Node> get_parent() { return this->parent; };
        std::shared_ptr<Node> get_left_child() { return this->left_child; };
        std::shared_ptr<Node> get_right_child() { return this->right_child; };
        std::string get_value() { return this->value; };
        virtual void evaluate() {};
};


class Add_node : public Node
{
    public:
        Add_node(): Node("+") {};
        void evaluate() override;
};


class Subtract_node : public Node
{
    public:
        Subtract_node(): Node("-") {};
        void evaluate() override;
};


class Multiply_node : public Node
{
    public:
        Multiply_node(): Node("*") {};
        void evaluate() override;
};


class Divide_node : public Node
{
    public:
        Divide_node(): Node("/") {};
        void evaluate() override;
};
#endif
