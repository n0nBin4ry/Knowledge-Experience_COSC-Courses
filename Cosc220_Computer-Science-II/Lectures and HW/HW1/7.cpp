//
// Created by Richard Flores on 2/13/2017.
//

#include <iostream>
using namespace std;
// func prototypes
void output1();
int input1();
int sort1(int a, int b);
int sort2(int a, int b, int c);
void output2(int a, int b);

const int SENTINEL = 0;
// user inputs integers, program outputs the two largest when sentinel is inputted
int main()
{
    output1();
    int x, y = 0, z = 0; // x is the user input, y is current greatest, z is current second greatest
    while (true)
    {
        x = input1();
        y = sort1(x, y);
        z = sort2(x, y, z);
        if (x == SENTINEL)
        {
            break;
        }
    }
    output2(y, z);
    return 0;
}

void output1() // instructs user
{
    cout << "Enter random integers to sort. When you want to know which is greatest,\ntype in \"0\"." << endl;
}

int input1() // returns integer user inputs
{
    cout << "> ";
    int x;
    cin >> x;
    return x;
}

int sort1(int a, int b) // returns largest between a and b
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

int sort2(int a, int b, int c) // returns int a, int b, or int c depending on condition
{
    if (a == b)
    {
        return c;
    }
    else if (a > c)
    {
        return a;
    }
    else
    {
        return c;
    }
}

void output2(int a, int b) // outputs results
{
    cout << "The largest number is:        " << a << endl;
    cout << "The second largest number is: " << b << endl;
}