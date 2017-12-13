//
// Created by Richard Flores on 2/13/2017.
//

#include <iostream>
using namespace std;

const int SENTINEL = 0;
// func prototypes
void output1();
int input1();
int sort(int a, int b);
void output2(int a);
// program takes all user inputs before inputting sentinel then outputs the greatest number
int main()
{
    output1();
    int x, y = 0; // x is the user input, y is the current greatest number
    while (true)
    {
        x = input1();
        y = sort(x, y);
        if (x == SENTINEL)
        {
            break;
        }
    }
    output2(y);
    return 0;
}

void output1() // instructs user
{
    cout << "Enter random integers to sort. When you want to know which is greatest,\ntype in \"0\"." << endl;
}

int input1() // returns integer that user inputs
{
    cout << "> ";
    int x;
    cin >> x;
    return x;
}

int sort(int a, int b) // returns largest between int a and int b
{
    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

void output2(int a) // outputs int a
{
    cout << "The greatest number is: " << a << endl;
}