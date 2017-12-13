//
// Created by Richard Flores on 3/28/2017.
//

#include "number4.h"
using namespace std;

Vector<int> getVector(ifstream& in, string filename) {
    Vector<int> out;
    in.open(filename.c_str());
    string line;
    //int counter(0);
    bool nothing(1);
    string holder("");
    while (true) {
        getline(in, line);
        if (in.fail()) {in.clear(); break;}
        //cout << "line: " << line << '\n';
        for (int i = 0; i < line.length(); i++) {
            //cout << "holder: " << holder << '\n';
            //cout << "counter: " << counter << '\n';
            //cout << "nothing: " << nothing << '\n';
            //cout << "is digit? " << isdigit(line[i]) << '\n';
            if (!nothing && isdigit(line[i])) {holder += line[i];}
            else if (nothing && isdigit(line[i])) {
                nothing = 0;
                holder += line[i];
            }
            else if (!nothing && !isdigit(line[i])) {
                nothing = 1;
                //cout << holder << '\n';
                out.add(stoi(holder));
                holder = "";
                //counter ++;
            }
        }
        if (!nothing) {
            nothing = 1;
            //cout << holder << '\n';
            out.add(stoi(holder));
            holder = "";
        }
    }
    in.close();
    return out;
}

string printAsterisks(int a) {
    string out("");
    for (int i = 0; i < a; i++) {
        out += "*";
    }
    return out;
}

void histogram(Vector<int> in) {
    int zeros(0); int tens(0); int twenties(0); int thirties(0); int forties(0);int fifties(0);
    int sixties(0); int seventies(0); int eighties(0); int nineties(0); int hunned(0);
    for (int i = 0; i < in.size(); i++) {
        //cout << in[i] << '\n';
        if (0 <= in[i] && in[i] < 10) {zeros++;}
        else if (in[i] < 20) {tens++;}
        else if (in[i] < 30) {twenties++;}
        else if (in[i] < 40) {thirties++;}
        else if (in[i] < 50) {forties++;}
        else if (in[i] < 60) {fifties++;}
        else if (in[i] < 70) {sixties++;}
        else if (in[i] < 80) {seventies++;}
        else if (in[i] < 90) {eighties++;}
        else if (in[i] < 100) {nineties++;}
        else if (in[i] == 100) {hunned++;}
    }
    cout << "00s: " << printAsterisks(zeros) << '\n';
    cout << "10s: " << printAsterisks(tens) << '\n';
    cout << "20s: " << printAsterisks(twenties) << '\n';
    cout << "30s: " << printAsterisks(thirties) << '\n';
    cout << "40s: " << printAsterisks(forties) << '\n';
    cout << "50s: " << printAsterisks(fifties) << '\n';
    cout << "60s: " << printAsterisks(sixties) << '\n';
    cout << "70s: " << printAsterisks(seventies) << '\n';
    cout << "80s: " << printAsterisks(eighties) << '\n';
    cout << "90s: " << printAsterisks(nineties) << '\n';
    cout << "100: " << printAsterisks(hunned);
}