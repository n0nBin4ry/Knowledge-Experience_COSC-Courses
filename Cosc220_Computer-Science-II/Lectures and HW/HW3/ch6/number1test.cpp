//
// Created by Richard Flores on 4/18/2017.
// need to link the stanford library because of the use of the gPoint class in my contains method for gRekt

#include "number1.h"
#include <iostream>
using namespace std;

int main() {
    cout << "I am testing my class gRekt.\nFirst I will make an empty instance.\n";
    gRekt emptyRekt;
    cout << "Is it really empty?\n> ";
    string out( emptyRekt.isEmpty() ? "Yes.\n" : "No.\n" );
    cout << out;
    cout << "Now input your own dimensions for another gRekt instance.\nx = ";
    float nX;
    cin >> nX;
    cout << "y = ";
    float nY;
    cin >> nY;
    cout << "Width = ";
    float nW;
    cin >> nW;
    cout << "Height = ";
    float nH;
    cin >> nH;
    gRekt newRekt(nX,nY, nW, nH);
    cout << "Does your new rectangle contain the point (5,5)?\n> ";
    out = newRekt.contains(5,5) ? "Yes!\n" : "No!\n";
    cout << out;
    cout << "Does it contain the GPoint pt(5,5)?\n> ";
    GPoint pt(5,5);
    out = newRekt.contains(pt) ? "Yes!" : "No!";
    cout << out;
    return 0;
}