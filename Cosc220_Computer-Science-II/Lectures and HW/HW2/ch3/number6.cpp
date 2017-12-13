//
// Created by Richard Flores on 3/17/2017.
//

#include "number6.h"
using namespace std;

string acronym(string in)
{
    string out("");
    for (int i = 0; i < in.length(); i++)
    {
        if (i == 0 && isalpha(in[i]))
        {
            out += toupper(in[i]);
        }
        else if (!isalpha(in[i- 1]) && isalpha(in[i]))
        {
            out += toupper(in[i]);
        }
    }
    return out;
}