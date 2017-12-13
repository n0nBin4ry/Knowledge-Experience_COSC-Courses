//
// Created by Richard Flores on 3/16/2017.
//

#include <iostream>
#include <cctype>
using namespace std;

string input();
int score(string in);
void output(int out);

int main()
{
    string in(input());
    int out(score(in));
    output(out);
    return 0;
}

string input()
{
    cout << "Input your word:\n> ";
    string out;
    cin >> out;
    return out;
}

int score(string in)
{
    int out(0);
    for (int i = 0; i < in.length(); i++)
    {

        if (tolower(in[i]) == 'a' || tolower(in[i]) == 'e' || tolower(in[i]) == 'i' || tolower(in[i]) == 'l' ||
            tolower(in[i]) == 'n' || tolower(in[i]) == 'o' || tolower(in[i]) == 'r' || tolower(in[i]) == 's' ||
            tolower(in[i]) == 't' || tolower(in[i]) == 'u')
        {
            out += 1;
        }
        else if (tolower(in[i]) == 'd' || tolower(in[i]) == 'g')
        {
            out += 2;
        }
        else if (tolower(in[i]) == 'b' || tolower(in[i]) == 'c' || tolower(in[i]) == 'm' || tolower(in[i]) == 'p')
        {
            out += 3;
        }
        else if (tolower(in[i]) == 'f' || tolower(in[i]) == 'h' || tolower(in[i]) == 'v' || tolower(in[i]) == 'w' ||
                tolower(in[i]) == 'y')
        {
            out += 4;
        }
        else if (tolower(in[i]) == 'k')
        {
            out += 5;
        }
        else if (tolower(in[i]) == 'j' || tolower(in[i]) == 'x')
        {
            out += 8;
        }
        else if (tolower(in[i]) == 'q' || tolower(in[i]) == 'z')
        {
            out += 10;
        }
    }
    return out;
}
void output(int out)
{
    cout << "Your score is: " << out;
}