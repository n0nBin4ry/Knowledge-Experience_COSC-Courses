//
// Created by Richard Flores on 4/15/2017.
//

#include <iostream>
#include "../stanflib/include/vector.h"
using namespace std;

Vector<short> createArray(short n);
void sortPrimes(Vector<short> & in);
void showVector(Vector<short> in);

int main() {
    cout << "Input a positive integer. I will find all the primes from 1 to that number.\n> ";
    short n;
    cin >> n;
    Vector<short> array(createArray(n));
    sortPrimes(array);
    cout << "All the primes from 0 to " << n << " are: ";
    showVector(array);
    return 0;
}

// creates vector of all integers from 2 to n
Vector<short> createArray(short n) {
    Vector<short> out;
    for (short i = 2; i <= n; i++) {
        out.add(i);
    }
    return out;
}
// removes all non-prime numbers from vector in
void sortPrimes(Vector<short> & in) {
    short length = in.size();
    for (short i = 0; i < length; i++) {
        if (in[i] == -1) {
            continue;
        }
        else {
            for (short j = i + 1; j < length; j++) {
                if (in[j] == -1) {
                    continue;
                }
                if ((in[j] % in[i]) == 0) {
                    in[j] = -1;
                }
            }
        }
        // why won't this last loop work?
//        if (i == (length - 1) ) {
//            for (short k = 0; k < length; k++) {
//                if (in[k] == -1) {
//                    in.remove(k);
//                }
//            }
//        }
    }
    // okay, instead of trying to be fancy I will do this
    for (int i = length; i > 0; i--) {
        if (in[i - 1] == -1) {
            in.remove(i - 1);
        }
    }
}
// outputs vector in to console
void showVector (Vector<short> in) {
    cout << "{ ";
    for (int i = 0; i < in.size(); i++) {
        if ( i == (in.size() - 1) ) {
            cout << in[i] << " }";
        }
        else {
            cout << in[i] << ", ";
        }
    }
}