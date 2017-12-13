//
// Created by Richard Flores on 3/16/2017.
// implementation file

#include <iostream>
#include <string>
#include "number3.h"
using namespace std;

string sbStr(string str, int pos, int n)
{
    if ((pos + 1) > str.length())
    {
        cout << "Error: Pos outside of string index, returning original string." << "\n";
        return str;
    }
    else if ((pos + 1 + n) > str.length())
    {
        n = str.length() - pos; // maybe -1 too? edit: naaah
    }
    string out("");
    for (int i = 0; i < n; i ++)
    {
        out += str[pos];
        pos ++;
    }
    return out;
}

string sbStr(string str, int pos)
{
    if ((pos + 1) > str.length())
    {
        cout << "Error: Pos outside of string index, returning original string." << "\n";
        return str;
    }
    int n;
    n = str.length() - pos;
    string out("");
    for (int i = 0; i < n; i ++)
    {
        out += str[pos];
        pos ++;
    }
    return out;
}