//
// Created by Richard Flores on 2/9/2017.
// incrementing loop; 2nd version, re-done using double variables; goes up to 170!

#include <iostream>
using namespace std;
// func prototypes
int input();
double factorial(int a);
void output(int a, double b);
// user inputs integer and program takes factorial of the integer
int main()
{
    int in = input();

    double out = factorial(in);

    output(in, out);
    return 0;
}

int input() // returns integer user inputs
{
    cout << "What number will you take the factorial of? ";
    int a;
    cin >> a;
    return a;
}

double factorial(int a) // returns factorial of int a
{
    double prod = 1; //  initialize the output
    for (int i = 1; i <= a; i++) // incrementing i
    {
        prod = prod * i; // multiplies every number from 1 to int a and outs it in prod
    }
    return prod;
}

void output(int a, double b) // user sees results
{
    cout << a << "! = " << b << endl;
}