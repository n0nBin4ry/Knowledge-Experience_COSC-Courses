//
// Created by Richard Flores on 3/16/2017.
//

#include <string>
#include <cctype>
using namespace std;

string capitalize(string in)
{
    int len(in.length());
    string out("");
    char temp;
    for (int i = 0; i < len; i++)
    {
        if (i == 0)
        {
           out += toupper(in[i]);
        }
        else
        {
            out += tolower(in[i]);
        }
    }
    return out;
}