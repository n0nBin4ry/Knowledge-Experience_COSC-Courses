//
// Created by Richard Flores on 4/19/2017.
//

#include <iostream>
using namespace std;

unsigned int fib(int n);

int main() {
    cout << "Input a positive integer, I will find the fibonacci sequence at that number:\n> ";
    int in;
    cin >> in;
    cout << "Calculating. . .\n";
    cout << in << "th number in the Fibonacci Sequence is: " << fib(in);
    return 0;
}

unsigned int fib(int n)
{
    if (n == 0) {return 1;}
    else if (n == 1) {return 1;}
    else {
        return fib(n - 1) + fib(n - 2);
    }
}