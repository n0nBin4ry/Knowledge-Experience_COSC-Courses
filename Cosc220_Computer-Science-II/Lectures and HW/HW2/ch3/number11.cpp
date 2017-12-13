//
// Created by Richard Flores on 3/17/2017.
//

#include <iostream>
using namespace std;

string flip(string in);
void killWhite(string &in);
bool isPalen(string in);

int main()
{
    cout << "Enter phrase/word:\n> ";
    string in;
    getline(cin,in);
    killWhite(in);
    if (isPalen(in) == 1) {cout << "Your phrase/word is a palindrome!";}
    else {cout << "Your phrase/word is not a palindrome!";}
    return 0;
}

string flip(string in)
{
    string out("");
    for (int i = 1; i <= in.length(); i ++)
    {
        out += in[in.length() - i];
    }
    return out;
}

void killWhite(string &in)
{
    for (int i = 0; i < in.length(); i++)
    {
        if (isalpha(in[i]) != 2 && isalpha(in[i]) != 1)
        {
            in.erase(i,1); i--;
        }
        else if (isalpha(in[i]) == 1)
        {
            in[i] = tolower(in[i]);
        }
    }
}

bool isPalen(string in)
{
    if (in.compare(flip(in)) == 0) {return true;}
    else {return false;}
}