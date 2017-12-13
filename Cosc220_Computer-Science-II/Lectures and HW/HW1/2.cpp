//
// Created by Richard Flores on 2/13/2017.
//

#include <iostream>
using namespace std;
// func prototypes
void prompt1();
double avgOfInputs();
void prompt2(double a);
// sentinel that stops input when input by user
const float SENTINEL = 0.0;
// user inputs integers, when the sentinel is inputted program outputs avg of all integers entered before 0
int main()
{
    prompt1();
    prompt2(avgOfInputs());
    return 0;
}

void prompt1() // instructs user
{
    cout << "Input numbers. When you want to take the average of all the inputted numbers, type \"0\" or a string." << endl;
}

double avgOfInputs() // returns avg of all integers inputted before sentinel
{
    int i = 0;
    float x;
    double sum = 0, out;
    while (true)
    {
        cout << "> ";
        cin >> x;
        if (x == SENTINEL)
        {
            break;
        }
        else
        {
            i++;
            sum = sum + x;
        }
    }
    out = sum / i;
    return out;
}

void prompt2(double a) // outputs double a
{
    cout << "The average of all the inputted numbers is: " << a << endl;
}