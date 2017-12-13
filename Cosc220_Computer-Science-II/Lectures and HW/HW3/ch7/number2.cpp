//
// Created by Richard Flores on 4/19/2017.
//

#include <iostream>
#include <cmath>
using namespace std;

double rPow(double in, int n);
int rPow(int in, int n);
bool isDouble(double in);

int main() {
    cout << "Input number: (float or integer)\n> ";
    double in;
    cin >> in;
    cout << "To what power? (integer only)\n> ";
    int n;
    cin >> n;
    (isDouble(in)) ? in = in : in = (int) in;
    cout << "Calculating. . .\n" << in << " to the " << n << "th power is: " << rPow(in, n);
    return 0;
}
// overloaded function to be usable with floats and integers; because why not
double rPow(double in, int n) {
    if (n == 0) {
        return 1;
    }
    else if (n == 1) {
        return in;
    }
    else {
        return in * rPow(in, n - 1);
    }
}
int rPow(int in, int n) {
    if (n == 0) {
        return 1;
    }
    else if (n == 1) {
        return in;
    }
    else {
        return in * rPow(in, n - 1);
    }
}
// needed extra function to check if input is a double or not.. because why not
bool isDouble(double in) {
    if ( floor(abs(in)) == abs(in) ) {
        return false;
    }
    else return true;
}