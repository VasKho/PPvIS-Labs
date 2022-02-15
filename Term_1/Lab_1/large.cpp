#include "large.hpp"


short Large::compare_absolutes(const Large& num_2) const
{
    if (this->number.size() < num_2.number.size()) return -1;
    if (this->number.size() > num_2.number.size()) return 1;
    for (int i = 0; i < this->number.size(); i++)
    {
        if (this->number[i] > num_2.number[i]) return 1;
        else if (this->number[i] < num_2.number[i]) return -1;
    }
    return 0;
}

Large& Large::str_to_large(const std::string& str)
{
    Large converted(str);
    *this = converted;
    return *this;
}

Large Large::get_absolute() const
{
    Large number_absolute(*this);
    number_absolute.sign = POSITIVE;
    return number_absolute;
}

Large::Large(const std::string& rvalue)
{
    const char* allowed_sym = "0123456789-";
    if ((rvalue[0] == '-' && rvalue[1] == '0' && rvalue.length() != 2) || (rvalue[0] == '0' && rvalue.length() != 1))
    {
        std::cout << "Invalid input" << std::endl;
        exit(1);
    }
    for (int i = 0; i < rvalue.length(); i++)
    {
        if (strchr(allowed_sym, rvalue[i]) == nullptr)
        {
            std::cout << "Invalid input" << std::endl;
            exit(1);
        }
    } 
    int i = 0;
    if (rvalue[0] == '-') 
    {
        sign = NEGATIVE;
        i = 1;
    }
    else sign = POSITIVE;

    for (; i < rvalue.length(); i++)
    {
        number.push_back(rvalue[i] - '0');
    }
}

Large::Large(const Large& copy_num)
{
    sign = copy_num.sign;
    number = copy_num.number;
}

Large& Large::operator=(const Large& assign_num)
{
    if (this == &assign_num) return *this;
    else
    {
        sign = assign_num.sign;
        number = assign_num.number;
    }
    return *this;
}

std::ostream& operator<<(std::ostream& output, const Large& num)
{
    if (num.sign == Large::NEGATIVE)
    {
        output << '-';
        for (auto i : num.number) output << i;
    }
    else 
    {
        for (auto i : num.number) output << i;
    }
    return output;
}

std::istream& operator>>(std::istream& input, Large& in_destination)
{
    std::string buffer;
    input >> buffer;
    in_destination.str_to_large(buffer);
    return input;
}

bool operator==(const Large& num_1, const Large& num_2)
{
    if (num_1.sign != num_2.sign) return false;
    if (num_1.number.size() == num_2.number.size())
    {
        for (int i = 0; i < num_1.number.size(); i++)
        {
            if (num_1.number[i] != num_2.number[i]) return false;
        }
    }
    else return false;
    return true;
}

bool operator==(const Large& num_1, const int& num_2)
{
    Large num_2_transformed(std::to_string(num_2));
    return num_1 == num_2_transformed;
}

bool operator!=(const Large& num_1, const Large& num_2)
{
    if (num_1.sign != num_2.sign) return true;
    if (num_1.number.size() == num_2.number.size())
    {
        for (int i = 0; i < num_1.number.size(); i++)
        {
            if (num_1.number[i] != num_2.number[i]) return true;
        }
    }
    else return true;
    return false;
}

bool operator!=(const Large& num_1, const int& num_2)
{
    Large num_2_transformed(std::to_string(num_2));
    return num_1 != num_2_transformed;
}

bool operator>(const Large& num_1, const Large& num_2)
{
    if (num_1.sign == Large::NEGATIVE && num_2.sign == Large::POSITIVE) return false;
    if (num_1.sign == Large::POSITIVE && num_2.sign == Large::NEGATIVE) return true;
    if (num_1.number.size() < num_2.number.size()) return false;
    if (num_1.number.size() > num_2.number.size()) return true;
    for (int i = 0; i < num_1.number.size(); i++)
    {
        if (num_1.number[i] > num_2.number[i]) return true;
        else if (num_1.number[i] < num_2.number[i]) return false;
    }
    return false;
}

bool operator>(const Large& num_1, const int& num_2)
{
    Large num_2_transformed(std::to_string(num_2));
    return num_1 > num_2_transformed;
}

bool operator>=(const Large& num_1, const Large& num_2)
{
    if (num_1.sign == Large::NEGATIVE && num_2.sign == Large::POSITIVE) return false;
    if (num_1.sign == Large::POSITIVE && num_2.sign == Large::NEGATIVE) return true;
    if (num_1.number.size() < num_2.number.size()) return false;
    if (num_1.number.size() > num_2.number.size()) return true;
    for (int i = 0; i < num_1.number.size(); i++)
    {
        if (num_1.number[i] > num_2.number[i]) return true;
        else if (num_1.number[i] < num_2.number[i]) return false;
    }
    return true;
}

bool operator>=(const Large& num_1, const int& num_2)
{
    Large num_2_transformed(std::to_string(num_2));
    return num_1 >= num_2_transformed;
}

bool operator<(const Large& num_1, const Large& num_2)
{
    if (num_1 > num_2) return false;
    if (num_2 > num_1) return true;
    return false;
}

bool operator<(const Large& num_1, const int& num_2)
{
    Large num_2_transformed(std::to_string(num_2));
    return num_1 < num_2_transformed;
}

bool operator<=(const Large& num_1, const Large& num_2)
{
    if (num_1 > num_2) return false;
    if (num_2 > num_1) return true;
    return true;
}

bool operator<=(const Large& num_1, const int& num_2)
{
    Large num_2_transformed(std::to_string(num_2));
    return num_1 <= num_2_transformed;
}

Large operator+(const Large& num_1, const Large& num_2)
{
    Large sum;
    sum.number.clear();
    Large min, max;
    bool overflow = false;
    if (num_1.compare_absolutes(num_2) != 1)
    {
        min = num_1;
        max = num_2;
    }
    else
    {
        min = num_2;
        max = num_1;
    }
    auto min_iter = --min.number.end();
    auto max_iter = --max.number.end();
    if (min.sign == max.sign)
    {
        sum.sign = min.sign;
        for (; min_iter != (min.number.begin() - 1); --min_iter)
        {
            short temp_res = (*min_iter) + (*max_iter) + overflow;
            sum.number.insert(sum.number.begin(), temp_res % 10);
            overflow = temp_res / 10;
            --max_iter;
        }
        for (; max_iter != (max.number.begin() - 1); --max_iter)
        {
            short temp_res = (*max_iter) + overflow;
            sum.number.insert(sum.number.begin(), temp_res%10);
            overflow = temp_res / 10;
        }
        if (overflow) sum.number.insert(sum.number.begin(), overflow);
    }
    else
    {
        Large max_absolute = max.get_absolute();
        Large min_absolute = min.get_absolute();
        sum = max_absolute - min_absolute;
        if (num_1.sign == Large::POSITIVE)
        {
            if (num_1 == max) sum.sign = Large::POSITIVE;
            else sum.sign = Large::NEGATIVE;
        }
        else
        {
            if (num_1 == max) sum.sign = Large::NEGATIVE;
            else sum.sign = Large::POSITIVE;
        }
    }
    return sum;
}

Large operator+(const Large& num_1, const int& num_2)
{
    Large num_2_transformed;
    num_2_transformed.str_to_large(std::to_string(num_2));
    return num_1 + num_2_transformed;
}

Large operator-(const Large& num_1, const Large& num_2)
{
    Large subtraction;
    subtraction.number.clear();
    Large min, max;
    if (num_1.compare_absolutes(num_2) != 1)
    {
        min = num_1;
        max = num_2;
    }
    else
    {
        min = num_2;
        max = num_1;
    }
    if (max.sign != min.sign)
    {
        Large max_absolute = max.get_absolute();
        Large min_absolute = min.get_absolute();
        subtraction = max_absolute + min_absolute;
        if (max == num_1)
        {
            if (max.sign == Large::POSITIVE) subtraction.sign = Large::POSITIVE;
            else subtraction.sign = Large::NEGATIVE;
        }
        else
        {
            if (min.sign == Large::POSITIVE) subtraction.sign = Large::POSITIVE;
            else subtraction.sign = Large::NEGATIVE;
        }
    }
    else
    {
        bool borrow = false;
        auto min_iter = --min.number.end();
        auto max_iter = --max.number.end();
        for (; max_iter != (max.number.begin() - 1); --max_iter)
        { 
            short temp_res;
            if(min_iter > (min.number.begin() - 1)) temp_res = (*max_iter) - (*min_iter) - borrow;
            else temp_res = (*max_iter) - borrow;
            if (temp_res < 0)
            {
                temp_res += 10;
                borrow = true;
            }
            else borrow = 0;
            subtraction.number.insert(subtraction.number.begin(), temp_res);
            --min_iter;
        }
        while(true)
        {
            if(subtraction.number[0] == 0 && subtraction.number.size() != 1) subtraction.number.erase(subtraction.number.begin());
            else break;
        }
        if (min == num_1 && min.sign == Large::POSITIVE) subtraction.sign = Large::NEGATIVE;
        else subtraction.sign = Large::POSITIVE;
    }
    return subtraction;
}

Large operator-(const Large& num_1, const int& num_2)
{
    Large transformed;
    transformed.str_to_large(std::to_string(num_2));
    return num_1 - transformed;
}

Large operator*(const Large& num_1, const Large& num_2)
{
    Large product;
    if(num_1 == 0 || num_2 == 0) return product;
    product.number.resize(num_1.number.size() + num_2.number.size());
    for (int iter_1 = (num_1.number.size() - 1); iter_1 >= 0; iter_1--)
    {
        for (int iter_2 = (num_2.number.size() - 1); iter_2 >= 0; iter_2--)
        {
            short temp_res = num_1.number[iter_1] * num_2.number[iter_2] + product.number[iter_1 + iter_2 + 1];
            product.number[iter_1 + iter_2 + 1] = temp_res % 10;
            product.number[iter_1 + iter_2] += temp_res / 10;
        }
    }
    if (product.number[0] == 0) product.number.erase(product.number.begin());
    if (num_1.sign == num_2.sign) product.sign = Large::POSITIVE;
    else product.sign = Large::NEGATIVE;
    return product;
}

Large operator*(const Large& num_1, const int& num_2)
{
    Large transformed;
    transformed.str_to_large(std::to_string(num_2));
    return num_1 * transformed;
}

Large operator/(const Large& num_1, const Large& num_2)
{
    Large result;
    Large num_1_absolute = num_1.get_absolute();
    Large num_2_absolute = num_2.get_absolute();
    if(num_1_absolute < num_2_absolute) return result;
    if (num_2 == 0)
    {
        std::cout << "DivideByZero error" << std::endl;
        exit(1);
    }
    result.number.clear();
    result.number.resize(num_1.number.size() - num_2.number.size() + 1);
    result.number[0] = 1;
    Large remaining;
    if((result * num_2_absolute) > num_1_absolute)
    {
        result.number.resize(num_1.number.size() - num_2.number.size());
        result.number[0] = 1;
    }
    remaining = num_1_absolute - (result * num_2_absolute);
    while(remaining >= num_2_absolute)
    {
        Large temp_res;
        temp_res.number.resize(remaining.number.size() - num_2.number.size() + 1);
        temp_res.number[0] = 1;
        if((temp_res * num_2_absolute) > remaining)
        {
            temp_res.number.resize(remaining.number.size() - num_2.number.size());
            temp_res.number[0] = 1;
        }
        result += temp_res;
        remaining -= temp_res * num_2_absolute;
    }
    if(num_1.sign != num_2.sign) result.sign = Large::NEGATIVE;
    return result;
}

Large operator/(const Large& num_1, const int& num_2)
{
    Large transformed;
    transformed.str_to_large(std::to_string(num_2));
    return num_1 / transformed;
}

Large Large::operator+=(const Large &num_2) { return *this = *this + num_2; }

Large Large::operator+=(const int &num_2) { return *this = *this + num_2; }

Large Large::operator-=(const Large &num_2) { return *this = *this - num_2; }

Large Large::operator-=(const int &num_2) { return *this = *this - num_2; }

Large Large::operator*=(const Large &num_2) { return *this = *this * num_2; }

Large Large::operator*=(const int &num_2) { return *this = *this * num_2; }

Large Large::operator/=(const Large &num_2) { return *this = *this / num_2; }

Large Large::operator/=(const int &num_2) { return *this = *this / num_2; }

Large& Large::operator++()
{
    *this += 1;
    return *this;
}

Large Large::operator++(int)
{
    Large temp = *this;
    ++(*this);
    return temp;
}

Large& Large::operator--()
{
    *this -= 1;
    return *this;
}

Large Large::operator--(int)
{
    Large temp = *this;
    --(*this);
    return temp;
}

Large::operator int() const
{
    std::string result = "";
    Large example("2147483647");
    if (this->compare_absolutes(example) == 1)
    {
        for(int i = 0; i < 10; ++i) result += std::to_string(this->number[i]);
        Large temp(result);
        if (temp > example) result.pop_back();
    }
    else for(auto i : this->number) result += std::to_string(i);
    if (this->sign == NEGATIVE) result.insert(0, 1, '-');
    return stoi(result);
}
