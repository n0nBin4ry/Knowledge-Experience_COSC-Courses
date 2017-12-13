//
// Created by Richard Flores on 3/28/2017.
// makefile in stanflib directory

#include "number4.h"
using namespace std;

int main() {
    ifstream in;
    string filename(selectFile(in, "I make a histogram out of integers within a file.\nEnter name of data file:"));
    cout << "Processing. . .\n";
    Vector<int> data(getVector(in, filename));
    histogram(data);
    return 0;
}