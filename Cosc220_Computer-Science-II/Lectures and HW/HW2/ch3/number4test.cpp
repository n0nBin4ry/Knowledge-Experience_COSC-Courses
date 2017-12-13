//
// Created by Richard Flores on 3/16/2017.
//

#include <iostream>
#include "number4.h"

int main()
{
    cout << "Enter a word to capitalize.\n> ";
    string in;
    cin >> in;
    string out(capitalize(in));
    cout << "Capitalizing. . . Done:\n" << out;
    return 0;
}