//
// Created by Fredrick Park on 1/28/17.
//

/*
 * File: PowersOfTwo.cpp
 * This program generates a list of the powers of
 * two up to an exponent limit entered by the user.
 */


#include <iostream> //iostream library
using namespace std;

/* Function Prototypes */

int raiseToPower(int n, int k);

/* Main Program */

int main() {
    int limit;
    cout << "This program lists powers of two." << endl;
    cout << "Enter exponent limit: ";
    cin >> limit;
    for (int i = 0; i <= limit; i++) {
        cout << "2 to the " << i << " = "
             << raiseToPower(2, i) << endl;
    }
    return 0;
}

/*
 * Function raiseToPower
 * Usage: int p = raiseToPower(n, k);
 * ----------------------------------
 * Returns the integer n raised to the kth power.
 */

int raiseToPower(int n, int k) {
    int result = 1;
    for (int i = 0; i < k; i++) {
        result *= n;
    }
    return result;
}
