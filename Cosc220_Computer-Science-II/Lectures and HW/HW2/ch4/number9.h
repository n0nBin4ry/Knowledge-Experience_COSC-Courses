//
// Created by Richard Flores on 3/26/2017.
//

#ifndef NUMBER9_H
#define NUMBER9_H

#include <fstream>
#include <iostream>
using namespace std;

void removeComments(ifstream& in, string filename, ofstream& out);

string selectFile(ifstream& in, string prompt);

#endif
