//
// Created by Richard Flores on 3/28/2017.
//

#include <string>
#include <fstream>
#include "number9.h"
using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    string filename(selectFile(in, "I remove comments from documents.\nInput file:"));
    removeComments(in, filename, out);
    cout << "Your new un-commented file is number9_ofile.txt";
    return 0;
}