//
// Created by Richard Flores on 3/28/2017.
//

#ifndef NUMBER4_H
#define NUMBER4_H

#include "stanflib/include/vector.h"
#include "../ch4/number9.h"
#include <iostream>
using namespace std;

Vector<int> getVector(ifstream& in, string filename);
string printAsterisks(int a);
void histogram(Vector<int> in);

#endif
