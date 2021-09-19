/// @file large.hpp
/// @author Vasili Khoroshavin
/// @date 17.09.2021
#ifndef _LARGE_H_
#define _LARGE_H_
#include <iostream>
#include <string>
#include <string.h>
#include <vector>

/**
 * @brief Class Large implements large signed numbers.
 *
 * It provides all overloaded operators for interaction with objects
 * of this class and simple integer numbers.
 */
class Large
{
private:
    enum Sign {POSITIVE, NEGATIVE};
    Sign sign;
    std::vector<int> number;
    short compare_absolutes(const Large&) const;
    Large& str_to_large(const std::string&);
    Large get_absolute() const;
public:
    /** @brief Constructor of class
     *
     *  Default value is 0
     *
     * @param[in] rvalue The reference to string to convert to large number
     */
    Large(const std::string& = "0");
    Large(const Large&);
    /** @brief Assigns new contents to the number, replacing its current contents.
     *  @param[in] assign_num The reference to the number of type Large to assign
     *  @return this
     */
    Large& operator=(const Large&);
    /** @brief Overloaded <b>output</b> operator
     *  @param[in, out] output The reference to specified output stream
     *  @param[in] num The reference to the number of type Large to out
     */
    friend std::ostream& operator<<(std::ostream&, const Large&);
    /** @brief Overloaded <b>input</b> operator
     *  @param[in, out] input The reference to specified input stream
     *  @param[in] in_destination The reference to the number of type Large to in
     */
    friend std::istream& operator>>(std::istream&, Large&);
    /** @brief Overloaded <b>equal to</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type Large to compare with
     */
    friend bool operator==(const Large&, const Large&);
    /** @brief Overloaded <b>equal to</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type int to compare with
     */
    friend bool operator==(const Large&, const int&);
    /** @brief Overloaded <b>not equal</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type Large to compare with
     */
    friend bool operator!=(const Large&, const Large&);
    /** @brief Overloaded <b>not equal</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type int to compare with
     */
    friend bool operator!=(const Large&, const int&);
    /** @brief Overloaded <b>greater than</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type Large to compare with
     */
    friend bool operator>(const Large&, const Large&);
    /** @brief Overloaded <b>greater than</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type int to compare with
     */
    friend bool operator>(const Large&, const int&);
    /** @brief Overloaded <b>greater than or equal to</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type Large to compare with
     */
    friend bool operator>=(const Large&, const Large&);
    /** @brief Overloaded <b>greater than or equal to</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type int to compare with
     */
    friend bool operator>=(const Large&, const int&);
    /** @brief Overloaded <b>lesser than</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type Large to compare with
     */
    friend bool operator<(const Large&, const Large&);
    /** @brief Overloaded <b>lesser than</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type int to compare with
     */
    friend bool operator<(const Large&, const int&);
    /** @brief Overloaded <b>lesser than or equal to</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type Large to compare with
     */
    friend bool operator<=(const Large&, const Large&);
    /** @brief Overloaded <b>lesser than or equal to</b> operator
     *  @param[in] num_1 The reference to the number of type Large to compare
     *  @param[in] num_2 The reference to the number of type int to compare with
     */
    friend bool operator<=(const Large&, const int&);
    /** @brief Overloaded <b>plus</b> operator  
     *  @param[in] num_1 The augend of type Large
     *  @param[in] num_2 The addend of type Large
     */
    friend Large operator+(const Large&, const Large&);
    /** @brief Overloaded <b>plus</b> operator  
     *  @param[in] num_1 The augend of type Large
     *  @param[in] num_2 The addend of type int
     */
    friend Large operator+(const Large&, const int&);
    /** @brief Overloaded <b>minus</b> operator  
     *  @param[in] num_1 The minued of type Large
     *  @param[in] num_2 The subtrahend of type Large
     */
    friend Large operator-(const Large&, const Large&);
    /** @brief Overloaded <b>minus</b> operator  
     *  @param[in] num_1 The minued of type Large
     *  @param[in] num_2 The subtrahend of type int 
     */
    friend Large operator-(const Large&, const int&);
    /** @brief Overloaded <b>multiply</b> operator
     *  @param[in] num_1 The multiplicand of type Large
     *  @param[in] num_2 The multiplier of type Large
     */
    friend Large operator*(const Large&, const Large&);
    /** @brief Overloaded <b>multiply</b> operator
     *  @param[in] num_1 The multiplicand of type Large
     *  @param[in] num_2 The multiplier of type int
     */
    friend Large operator*(const Large&, const int&);
    /** @brief Overloaded <b>divide</b> operator
     *  @param[in] num_1 The divident of type Large
     *  @param[in] num_2 The divisor of type Large
     */
    friend Large operator/(const Large&, const Large&);
    /** @brief Overloaded <b>divide</b> operator
     *  @param[in] num_1 The divident of type Large
     *  @param[in] num_2 The divisor of type int
     */
    friend Large operator/(const Large&, const int&);
    /** @brief Overloaded <b>addition assign</b> operator
     *  @param[in] num_2 The addend of type Large
     */
    Large operator+=(const Large&);
    /** @brief Overloaded <b>addition assign</b> operator
     *  @param[in] num_2 The addend of type int
     */
    Large operator+=(const int&);
    /** @brief Overloaded <b>subtraction assign</b> operator
     *  @param[in] num_2 The subtrahend of type Large
     */
    Large operator-=(const Large&);
    /** @brief Overloaded <b>subtraction assign</b> operator
     *  @param[in] num_2 The subtrahend of type int
     */
    Large operator-=(const int&);
    /** @brief Overloaded <b>multiplication assign</b> operator
     *  @param[in] num_2 The multiplier of type Large
     */
    Large operator*=(const Large&);
    /** @brief Overloaded <b>multiplication assign</b> operator
     *  @param[in] num_2 The multiplier of type int
     */
    Large operator*=(const int&);
    /** @brief Overloaded <b>division assign</b> operator
     *  @param[in] num_2 The divisor of type Large
     */
    Large operator/=(const Large&);
    /** @brief Overloaded <b>division assign</b> operator
     *  @param[in] num_2 The divisor of type int
     */
    Large operator/=(const int&);
    /** @brief Overloaded <b>pre-increment</b> operator
     *  
     *  This increment operator increments (adds one) and returns the value
     *  after incrementing.
     */
    Large& operator++();
    /** @brief Overloaded <b>post-increment</b> operator
     *  
     *  This increment operator increments (adds one) and returns the value
     *  before incrementing.
     */
    Large operator++(int);
    /** @brief Overloaded <b>pre-decrement</b> operator
     *  
     *  This decrement operator decrements (subtracts one) and returns the value
     *  after decrementing.
     */
    Large& operator--();
    /** @brief Overloaded <b>pre-decrement</b> operator
     *  
     *  This decrement operator decrements (subtracts one) and returns the value
     *  before decrementing.
     */
    Large operator--(int);
    /** @brief Overloaded <b>type-casting</b> operator
     *
     *  Converts an expression of type Large into integer type. If given 
     *  number is larger than integer size, than lower digits are discarded.
     */
    operator int() const;
};
#endif
