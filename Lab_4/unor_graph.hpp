#ifndef _UNOR_GRAPH_H_
#define _UNOR_GRAPH_H_
#include <vector>
#include <iostream>

template<class Type>
class unor_graph
{
    private:
        std::vector<Type> vertexes;
        std::vector<std::pair<Type, Type>> edges;
    public:
        unor_graph() {};
        bool empty();
        void clear();
        void add_vertex(Type);
        void add_edge(const Type&, const Type&);
        void remove_vertex(const Type&);
        void remove_edge(const Type&, const Type&);
        bool find_vertex(const Type&);
        bool are_connected(const Type&, const Type&);
        std::size_t get_number_of_vertexes() { return vertexes.size(); };
        std::size_t get_number_of_edges() { return edges.size(); };
        std::size_t find_power_of_vertex(const Type&);
        std::size_t find_power_of_edge(const Type&, const Type&);

        typedef typename std::vector<Type>::iterator vertex_iterator;
        typedef typename std::vector<Type>::reverse_iterator vertex_riterator;
        typedef typename std::vector<Type>::const_iterator vertex_citerator;

        typedef typename std::vector<std::pair<Type, Type>>::iterator edges_iterator;
        typedef typename std::vector<std::pair<Type, Type>>::const_iterator edges_citerator;
        typedef typename std::vector<std::pair<Type, Type>>::reverse_iterator edges_riterator;

        vertex_iterator vertexes_begin() { return vertexes.begin(); };
        vertex_iterator vertexes_end() { return vertexes.end(); };
        vertex_citerator vertexes_cbegin() { return vertexes.cbegin(); };
        vertex_citerator vertexes_cend() { return vertexes.cend(); };
        vertex_riterator vertexes_rbegin() { return vertexes.rbegin(); };
        vertex_riterator vertexes_rend() { return vertexes.rend(); };

        edges_iterator edges_begin() { return edges.begin(); };
        edges_iterator edges_end() { return edges.end(); };
        edges_citerator edges_cbegin() { return edges.cbegin(); };
        edges_citerator edges_cend() { return edges.cend(); };
        edges_riterator edges_rbegin() { return edges.rbegin(); };
        edges_riterator edges_rend() { return edges.rend(); };

        void remove_vertex(vertex_iterator);
        void remove_edge(edges_iterator it) { edges.erase(it); };


        friend bool operator==(const unor_graph<Type>&, const unor_graph<Type>&);
        friend bool operator!=(const unor_graph<Type>&, const unor_graph<Type>&);
};


template<class Type>
bool unor_graph<Type>::empty()
{
    return vertexes.empty();
}


template<class Type>
void unor_graph<Type>::clear()
{
    vertexes.clear();
    edges.clear();
}


template<class Type>
void unor_graph<Type>::add_vertex(Type vertex)
{
    this->vertexes.push_back(vertex);
}


template<class Type>
void unor_graph<Type>::add_edge(const Type& v_1, const Type& v_2)
{
    if (!find_vertex(v_1)) throw ("Vertex " + std::to_string(v_1) + " not in graph");
    if (!find_vertex(v_2)) throw ("Vertex " + std::to_string(v_2) + " not in graph");
    this->edges.push_back(std::pair<Type, Type>(v_1, v_2));
}


template<class Type>
void unor_graph<Type>::remove_vertex(const Type& vertex)
{
    if (!find_vertex(vertex)) return;
    for (auto i : edges)
        if (i.first == vertex || i.second == vertex) edges.erase(i);
    vertexes.erase(vertexes.at(vertex));
}


template<class Type>
void unor_graph<Type>::remove_edge(const Type& v_1, const Type& v_2)
{
    if (!find_vertex(v_1)) return;
    if (!find_vertex(v_2)) return;
    if (!this->are_connected(v_1, v_2)) return;
    for (auto i = edges.begin(); i != edges.end(); ++i)
    {
        if (((*i).first == v_1 && (*i).second == v_2) || ((*i).first == v_2 && (*i).second == v_1))
        {
            if (i == edges.begin())
            {
                edges.erase(i);
                i = edges.begin();
                return;
            }
            else
            {
                auto tmp = i;
                --tmp;
                edges.erase(i);
                i = tmp;
                return;
            }
        }
    }
}


template<class Type>
bool unor_graph<Type>::find_vertex(const Type& vertex)
{
    for (auto i : vertexes) if (i == vertex) return true;
    return false;
}


template<class Type>
bool unor_graph<Type>::are_connected(const Type& v_1, const Type& v_2)
{
    if (!find_vertex(v_1)) throw ("Vertex " + std::to_string(v_1) + " not in graph");
    if (!find_vertex(v_2)) throw ("Vertex " + std::to_string(v_2) + " not in graph");

    for (auto i : edges) 
        if ((i.first == v_1 && i.second == v_2) || (i.first == v_2 && i.second == v_1)) return true;
    return false;
}


template<class Type>
std::size_t unor_graph<Type>::find_power_of_vertex(const Type& vertex)
{
    if (!find_vertex(vertex)) throw ("Vertex " + std::to_string(vertex) + " not in graph");

    std::size_t power = 0;
    for (auto i : edges) if (i.first == vertex || i.second == vertex) ++power;

    return power;
}


template<class Type>
std::size_t unor_graph<Type>::find_power_of_edge(const Type& v_1, const Type& v_2)
{
    if (!find_vertex(v_1)) throw ("Vertex " + std::to_string(v_1) + " not in graph");
    if (!find_vertex(v_2)) throw ("Vertex " + std::to_string(v_2) + " not in graph");
    if (!this->are_connected(v_1, v_2)) throw ("Edge between " + std::to_string(v_1) + " and " + std::to_string(v_2) + " doesn't in graph");
    std::size_t power = 0;
    for (auto i : edges)
        if ((i.first == v_1 && i.second == v_2) || (i.first == v_2 && i.second == v_1)) ++power;
    return power;
}


template<class Type>
void unor_graph<Type>::remove_vertex(vertex_iterator it)
{
    for (auto i = edges.begin(); i != edges.end(); ++i)
    {
        if ((*i).first == *it || (*i).second == *it)
        {
            if (i == edges.begin())
            {
                edges.erase(i);
                i = edges.begin();
            }
            else
            {
                auto tmp = i;
                --tmp;
                edges.erase(i);
                i = tmp;
            }
        }
    }
    vertexes.erase(it);
}


template<class Type>
bool operator==(const unor_graph<Type>& g1, const unor_graph<Type>& g2)
{
    return (g1.vertexes == g2.vertexes && g1.edges == g2.vertexes);
}


template<class Type>
bool operator!=(const unor_graph<Type>& g1, const unor_graph<Type>& g2)
{
    return !(g1 == g2);
}
#endif
