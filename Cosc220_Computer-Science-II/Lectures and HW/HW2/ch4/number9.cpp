//
// Created by Richard Flores on 3/26/2017.
//

#include <string>
#include <fstream>
#include "number9.h"
using namespace std;

void removeComments(ifstream& in, string filename, ofstream& out)
{
    bool firstLine(1);
    bool astSlash(0);
    string line;
    in.open(filename.c_str());
    out.open("number9_ofile.txt");
    while (true)
    {
        getline(in, line);
        if (in.fail()) {in.clear(); break;}
        if (!firstLine) {out << '\n';} else {firstLine = 0;}
        for (int i = 0; i < line.length(); i++)
        {
            if (astSlash == 1 && (line[i] == '/' && line[i - 1] == '*') ) { astSlash = 0; continue;}
            else if (astSlash == 1) {continue;}
            else
            {
                if (line[i] == '/' && line[i + 1] == '/') {break;}
                else if (line[i] == '/' && line[i + 1] == '*')
                {
                    astSlash = 1;
                    continue;
                }
                else {out << line[i];}
            }
        }
    }
    in.close(); out.close();
}

string selectFile(ifstream& in, string prompt)
{
    while (true)
    {
        cout << prompt << "\n> ";
        string out;
        getline(cin, out);
        in.open(out.c_str());
        if (!in.fail())
        {
            in.close();
            return out;
        }
        in.clear();
        cerr << "Whoops, try again!\n";
    }
}