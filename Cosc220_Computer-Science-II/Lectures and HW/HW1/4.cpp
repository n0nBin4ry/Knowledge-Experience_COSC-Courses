//
// Created by Richard Flores on 2/9/2017.
//

#include <iostream>
using namespace std;
// func prototypes
void init();
double calculate();
void output(double a);
// calculates pi when sentinel entered
int main()
{
    init();
    double out = calculate();
    output(out);
    return 0;
}

void init() // instructs user
{
    const string SENTINEL = "start";
    string a;
    cout << "Enter \"start\" when you wish to begin the calculation." << endl;
    while (true)
    {
        cout << "> ";
        cin >> a;
        if (a == SENTINEL)
        {
            break;
        }
    }
    cout << "Calculating..." << endl;
}

double calculate() // calculates pi and returns it
{
    double sum = 1;
    // cout << "Its been calculated." << endl; // test
    for (long int i = 1; i <= 10000; i++)
    {
        double n = i;
        if ((i % 2) != 0)
        {
            sum = sum - (1 / (n + (n + 1)));
        }
        else if ((i % 2) == 0)
        {
            sum = sum + (1 / (n + (n + 1)));
        }
    }
    sum = sum * 4;
    return sum;
}

void output(double a) // outputs double a
{
    cout << "pi = " << a << endl;
}