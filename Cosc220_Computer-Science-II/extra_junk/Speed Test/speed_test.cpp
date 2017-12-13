#include <iostream>
using namespace std; //std::cout, std::fixed
#include <iomanip> // std::setprecision
# include <ctime>


/*
* Code that prompts user to enter integer N and then sums all
* numbers from 1 to N and outputs the result
 */


int main()
{
    float start_s=clock();
    double sum = 0;
    double j = 1;
    int N = 100000000;
    //cout << "Enter an integer N and we'll sum the squares and cubes of the numbers from 1 to N: ";
    //cin >> N;

    for (int i = 1; i <= N; i++)
    {
        j = double(i); // convert int i into double for comp'tn accuracy
        sum += j + j*j + j*j*j;
    }
    cout << "sum of the numbers from 1 to " << setprecision(32) << N << " is = " << sum << endl;

    float stop_s=clock();
    cout << "time: " << (stop_s-start_s)/CLOCKS_PER_SEC << " secs" << endl; // secs

}