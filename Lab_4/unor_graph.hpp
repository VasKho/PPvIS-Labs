#ifndef _UNOR_GRAPH_H_
#define _UNOR_GRAPH_H_
#include <vector>
#include <iostream>

template<class Type>
class unor_graph
{
    private:
        std::vector<Type> vertexes;
        std::vector<std::vector<std::size_t>> adj_matrix;
        std::size_t number_of_vertexes;
        std::size_t number_of_edges;
        int at(const Type&);
    public:
        unor_graph() : number_of_edges(0), number_of_vertexes(0) {};
        void add_vertex(Type);
        void add_edge(const Type&, const Type&);
        void remove_vertex(const Type&);
        void remove_edge(const Type&, const Type&);
        bool find(const Type&);
        bool are_connected(const Type&, const Type&);
        std::size_t get_number_of_vertexes() { return this->number_of_vertexes; };
        std::size_t get_number_of_edges() { return this->number_of_edges; };
        std::size_t find_power_of_vertex(const Type&);
        std::size_t find_power_of_edge(const Type&, const Type&);

        typedef typename std::vector<Type>::iterator vertex_iterator;
        typedef typename std::vector<Type>::reverse_iterator vertex_riterator;
        typedef typename std::vector<Type>::const_iterator vertex_citerator;

        typedef typename std::vector<std::pair<Type&, Type&>>::iterator edges_iterator;
        typedef typename std::vector<std::pair<Type&, Type&>>::const_iterator edges_citerator;
        typedef typename std::vector<std::pair<Type&, Type&>>::reverse_iterator edges_riterator;

        vertex_iterator vertexes_begin() { return vertexes.begin(); };
        vertex_iterator vertexes_end() { return vertexes.end(); };
        vertex_citerator vertexes_cbegin() { return vertexes.cbegin(); };
        vertex_citerator vertexes_cend() { return vertexes.cend(); };
        vertex_riterator vertexes_rbegin() { return vertexes.rbegin(); };
        vertex_riterator vertexes_rend() { return vertexes.rend(); };
};


template<class Type>
int unor_graph<Type>::at(const Type& vertex)
{
    for (int i = 0; i < number_of_vertexes; ++i) if (this->vertexes[i] == vertex) return i;
    return -1;
}


template<class Type>
void unor_graph<Type>::add_vertex(Type vertex)
{
    this->vertexes.push_back(vertex);
    this->adj_matrix.push_back(std::vector<std::size_t>(this->number_of_vertexes));
    ++this->number_of_vertexes;
    for(int i = 0; i < number_of_vertexes; ++i) adj_matrix[i].resize(number_of_vertexes);
}


template<class Type>
void unor_graph<Type>::add_edge(const Type& v_1, const Type& v_2)
{
    long pos_1 = this->at(v_1);
    long pos_2 = this->at(v_2);
    if (pos_1 < 0) throw ("Vertex " + std::to_string(v_1) + " not in graph");
    if (pos_2 < 0) throw ("Vertex " + std::to_string(v_2) + " not in graph");
    ++this->adj_matrix[pos_1][pos_2];
    ++this->number_of_edges;
}


template<class Type>
void unor_graph<Type>::remove_vertex(const Type& vertex)
{
    long pos = this->at(vertex);
    if (pos < 0) return;
    for(int i = 0; i < number_of_vertexes; ++i) adj_matrix[i].erase(adj_matrix[i].begin() + pos);
    this->adj_matrix.erase(adj_matrix.begin() + pos);
    --this->number_of_vertexes;
}


template<class Type>
void unor_graph<Type>::remove_edge(const Type& v_1, const Type& v_2)
{
    long pos_1 = this->at(v_1);
    long pos_2 = this->at(v_2);
    if (pos_1 < 0 || pos_2 < 0) return;
    if (!this->are_connected(v_1, v_2)) return;
    --this->adj_matrix[pos_1][pos_2];
    --this->number_of_edges;
}


template<class Type>
bool unor_graph<Type>::find(const Type& vertex)
{
    for (int i = 0; i < number_of_vertexes; ++i) if (this->vertexes[i] == vertex) return true;
    return false;
}


template<class Type>
bool unor_graph<Type>::are_connected(const Type& v_1, const Type& v_2)
{
    long pos_1 = this->at(v_1);
    long pos_2 = this->at(v_2);
    if (pos_1 < 0) throw ("Vertex " + std::to_string(v_1) + " not in graph");
    if (pos_2 < 0) throw ("Vertex " + std::to_string(v_2) + " not in graph");

    if (this->adj_matrix[pos_1][pos_2] != 0) return true;
    return false;
}


template<class Type>
std::size_t unor_graph<Type>::find_power_of_vertex(const Type& vertex)
{
    long pos = this->at(vertex);
    if (pos < 0) throw ("Vertex " + std::to_string(vertex) + " not in graph");

    std::size_t power = 0;
    for (auto i : adj_matrix[pos]) if (i != 0) ++power;

    return power;
}


template<class Type>
std::size_t unor_graph<Type>::find_power_of_edge(const Type& v_1, const Type& v_2)
{
    long pos_1 = this->at(v_1);
    long pos_2 = this->at(v_2);
    if (pos_1 < 0) throw ("Vertex " + std::to_string(v_1) + " not in graph");
    if (pos_2 < 0) throw ("Vertex " + std::to_string(v_2) + " not in graph");
    if (!this->are_connected(v_1, v_2)) throw ("Edge between " + std::to_string(v_1) + " and " + std::to_string(v_2) + " doesn't in graph");
    return this->adj_matrix[pos_1][pos_2];
}
#endif
