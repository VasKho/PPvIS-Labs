#ifndef _ITERATORS_H_
#define _ITERATORS_H_
#include <vector>
#include <algorithm>
#include "unor_graph.hpp"

template<class Type>
class adjacent_iterator
{
    private:
        std::vector<Type> vertexes;
    public:
        adjacent_iterator(unor_graph<Type>&, const Type&);

        typedef typename std::vector<Type>::iterator adj_iterator; 
        typedef typename std::vector<Type>::reverse_iterator adj_riterator;
        typedef typename std::vector<Type>::const_iterator adj_citerator;

        adj_iterator adj_begin() { return vertexes.begin(); };
        adj_iterator adj_end() { return vertexes.end(); };
        adj_riterator adj_rbegin() { return vertexes.rbegin(); };
        adj_riterator adj_rend() { return vertexes.rend(); };
        adj_citerator adj_cbegin() { return vertexes.cbegin(); };
        adj_citerator adj_cend() { return vertexes.cend(); };
};

template<class Type>
class incident_iterator
{
     private:
       std::vector<std::pair<Type, Type>> edges; 
    public:
        incident_iterator(unor_graph<Type>&, const Type&);

        typedef typename std::vector<std::pair<Type, Type>>::iterator inc_iterator; 
        typedef typename std::vector<std::pair<Type, Type>>::reverse_iterator inc_riterator;
        typedef typename std::vector<std::pair<Type, Type>>::const_iterator inc_citerator;

        inc_iterator adj_begin() { return edges.begin(); };
        inc_iterator adj_end() { return edges.end(); };
        inc_riterator adj_rbegin() { return edges.rbegin(); };
        inc_riterator adj_rend() { return edges.rend(); };
        inc_citerator adj_cbegin() { return edges.cbegin(); };
        inc_citerator adj_cend() { return edges.cend(); };   
};


template<class Type>
adjacent_iterator<Type>::adjacent_iterator(unor_graph<Type>& g, const Type& vrtx)
{
    for (auto i = g.vertexes_begin(); i != g.vertexes_end(); ++i)
    {
        for (auto j = g.vertexes_begin(); j != g.vertexes_end(); ++j)
        {
            if (g.are_connected(*i, *j))
            {
                if (*i == vrtx) 
                {
                    if (std::find(vertexes.begin(), vertexes.end(), *j) == std::end(vertexes))
                        vertexes.push_back(*j);
                }
                else if (std::find(vertexes.begin(), vertexes.end(), *i) == std::end(vertexes)) vertexes.push_back(*i);
            }
        }
    }
}
#endif
