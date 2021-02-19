/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include<vector>
#include<algorithm>
#include<iostream>
#include<iterator>
#include<functional>
using namespace std;

int square(int x){ return x*x;}

int main()
{
vector<int> v = {1,2,3,4};
vector<int> v2;
vector<int> v3;
vector<int> v4(10);
vector<int> v5;
std::cout << "Hello v1"<< endl;
copy(v.begin(), v.end(), ostream_iterator<int>(cout, " "));
transform(v.begin(), v.end(), back_inserter(v2), square);
std::cout << endl <<"v2"<< endl;
copy(v2.begin(), v2.end(), ostream_iterator<int>(cout, " "));
copy(v.begin(), v.end(), back_inserter(v3));
std::cout << endl << "v3"<< endl;
copy(v3.begin(), v3.end(), ostream_iterator<int>(cout, " "));

copy(v.begin(), v.end(), v4.begin());
std::cout << endl << "v4"<< endl;
copy(v4.begin(), v4.end(), ostream_iterator<int>(cout, " "));

transform(v.begin(), v.end(), back_inserter(v5), bind(multiplies<int>(), placeholders::_1,10));
std::cout << endl <<"v5"<< endl;
copy(v5.begin(), v5.end(), ostream_iterator<int>(cout, " "));
}
