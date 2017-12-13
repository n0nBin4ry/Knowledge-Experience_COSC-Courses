//
// Created by Richard Flores on 3/16/2017.
//

#include <iostream>
#include <string>
#include "number3.h"
using namespace std;

int main()
{
    bool choice;
    cout << "Use an n or not? (to determine length of substring)\n[1]: use n   [0] don't use n\n> ";
    cin >> choice;
    cin.clear();
    cin.ignore();
    cout << "Enter string:\n> ";
    string in;
    getline(cin, in);
    cout << "Enter position:\n> ";
    int pos;
    cin >> pos;
    cin.clear();
    cin.ignore();
    string out;
    if (choice == 1)
    {
        cout << "Enter n (length of substring):\n> ";
        int n;
        cin >> n;
        cin.clear();
        cin.ignore();
        out = sbStr(in, pos, n);
    }
    else
    {
        out = sbStr(in, pos);
    }
    cout << "Your substring is:\n" << out;
    return 0;
}