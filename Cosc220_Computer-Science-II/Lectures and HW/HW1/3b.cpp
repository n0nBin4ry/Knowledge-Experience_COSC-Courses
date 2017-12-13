//
// Created by Richard Flores on 2/10/2017.
// decimating loop

#include <iostream>
using namespace std;

int input();
double factorial(int a);
void output(int a, double b);
// exact same as 3a, except the factorial function is decimating
int main()
{
    int in = input();

    double out = factorial(in);

    output(in, out);
    return 0;
}

int input()
{
    cout << "What number will you take the factorial of? ";
    int a;
    cin >> a;
    return a;
}

double factorial(int a)
{
    double prod = 1;
    for (int i = (a - 1); i >= 0; i--) // i decimates
    {
        prod = prod * (a - i);
    }
    return prod;
}

void output(int a, double b)
{
    cout << a << "! = " << b << endl;
}