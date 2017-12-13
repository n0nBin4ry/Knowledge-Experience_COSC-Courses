//
// Created by Richard Flores on 3/17/2017.
//

#include <iostream>
#include "number6.h"
using namespace std;

string input();
void output(string out);

int main()
{
    string in(input());
    cout << in << "\n";
    string out(acronym(in));
    output(out);
    return 0;
}

string input()
{
    cout << "Enter Phrase\n> ";
    string out;
    getline(cin, out);
    return out;
}

void output(string out)
{
    cout << "Making acronym. . . Done:\n" << out;
}