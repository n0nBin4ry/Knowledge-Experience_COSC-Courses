//
// Created by Richard Flores on 3/18/2017.
// note: went through and counted the text myself twice and found there are 252 characters (including line-breaks), not 254

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

string selectFile(ifstream& in, string prompt); // only works if called by reference ???
int countChars(ifstream& in, string filename);
int countLines(ifstream& in, string filename);
int countWords(ifstream& in, string filename);
int maxOf3(int a, int b, int c);

int main()
{
	ifstream infile;
	string filename = selectFile(infile, "Select file name:");
	int chars(countChars(infile, filename));
	int lines(countLines(infile, filename));
	int words(countWords(infile, filename));
    string max(to_string(maxOf3(chars, lines, words)));
    int space(max.length());
    cout << right;
    cout << "Chars: " << setw(space) << chars << endl;
    cout << "Words: " << setw(space) << words << endl;
    cout << "Lines: " << setw(space) << lines << endl;
    return 0;
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

int countChars(ifstream& in, string filename)
{
	int out(0);
	in.open(filename.c_str());
	while ((in.get()) != EOF) // commented area below works if I just use while (true)
	{
//        int ch = in.get();
//        if (in.fail())
//        {
//            break;
//        }

        // guess the question wanted me to include line-break characters too
		//in.unget();
		//if (in.get() == '\n') {continue;}
		out ++;
	}
	in.clear();
	in.close();
	return out;
}

int countLines(ifstream& in, string filename)
{
	int out(0);
	in.open(filename.c_str());
	string line;
	while (true)
	{
		getline(in, line);
		if (in.fail()) {break;}
		out ++;
	}
	in.clear();
	in.close();
	return out;
}

int countWords(ifstream& in, string filename)
{
	int out(0);
	in.open(filename.c_str());
	string line;
	while (true)
	{
		getline(in, line);
        bool word(false);
		if (in.fail()) {break;}
		for (int i = 0; i < line.length(); i++)
		{
            if ((line[i] != ' ') && (!word)) {out++; word = true;}
            else if ((line[i] == ' ') && (word)) {word = false;}
		}
	}
    in.clear();
    in.close();
    return out;
}

int maxOf3(int a, int b, int c)
{
    if (a >= b && a >= c) {return a;}
    else if (b > c) {return b;}
    else {return c;}
}