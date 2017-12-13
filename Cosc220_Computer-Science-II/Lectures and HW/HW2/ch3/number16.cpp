//
// Created by Richard Flores on 3/18/2017.
//

#include <iostream>
using namespace std;

string input();
bool isVowel(char in);
string obenglobish(string in);
void output(string out);

int main()
{
    string in(input());
    string out(obenglobish(in));
    output(out);
    return 0;
}

string input()
{
    cout << "Input a what you want to encode in Obenglobish:\n> ";
    string out;
    getline(cin, out);
    return out;
}

bool isVowel(char in)
{
    switch(in)
    {
        case 'A' : case 'E' : case 'I' : case 'O' : case 'U' : case 'a' : case 'e' : case 'i' : case 'o' : case 'u' :
            return true;
        default:
            return false;
    }
}

string obenglobish(string in)
{
    for (int i = 0; i < in.length(); i++)
    {
        if (isVowel(in[i]))
        {
            if (i == 0 && isupper(in[i]))
            {
                in[i] = tolower(in[i]);
                in.insert(i, "Ob");
                i += 2;
            }
            else if (isVowel(in[i-1]))
            {
                continue;
            }
            else if ((((i + 1) == in.length()) || !isalpha(in[i+1])) && (in[i] == 'e' || in[i] == 'E'))
            {
                continue;
            }
            else
            {
                in.insert(i, "ob");
                i += 2;
            }
        }
    }
    return in;
}

void output(string out)
{
    cout << "Encoding. . . DONE:\n" << out;
}