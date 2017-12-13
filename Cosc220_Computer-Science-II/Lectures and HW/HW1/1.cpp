//
// Created by Richard Flores on 2/10/2017.
//

#include <iostream>
using namespace std;
// func prototypes
int input();
void output(int a);
// user inputs an integer and the program outputs a prompt that many times
int main()
{
    int x = input();
    output(x);
    return 0;
}

int input() // returns the integer the user inputs
{
    cout << "How many times should I say it? ";
    int a;
    cin >> a;
    return a;
}

void output(int a) // outputs prompt int a times
{
    for (int i = 1; i <= a; i++)
    {
        cout << "COSC 220 is Awesome!" << endl;
    }
}