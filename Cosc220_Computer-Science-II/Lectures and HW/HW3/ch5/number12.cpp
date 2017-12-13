//
// Created by Richard Flores on 4/19/2017.
//

#include <iostream>
#include "../stanflib/include/stack.h"
using namespace std;

const int SENTINEL(0);

int main() {
    Stack<int> out;
    cout << "Input integers. When you are done, input " << SENTINEL << ".\n"
            "I will then output your integers in reverse order.\n";
    while(true) {
        cout << "> ";
        int in;
        cin >> in;
        if (in == SENTINEL) {break;}
        else {
            out.push(in);
        }
    }
    cout << "Flipping. . .\n";
    cout << out.size() << "\n";
    for (int i = 0; i < out.size(); i++) {
        cout << out.pop() << "\n";
        i --;
    }
    return 0;
}