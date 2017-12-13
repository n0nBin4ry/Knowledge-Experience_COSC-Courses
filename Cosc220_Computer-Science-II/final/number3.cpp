//
// Created by Richard Flores on 5/8/2017.
//
/* Doesn't work every time.. But does work. I tried my best to find a way to do it linearly without allocating memory for another vector.
 * If I was able to use another vector then I would've been able to do it with linear complexity, I think.
 * I would've made a second vector the length of N with every value being zero then every time a number in the OG vector
 * was passed in the for loop, the function would increase the value of the the cell of the new vector who's index would
 * match the number from from the OG vector. Right after increasing that value a conditional would check that current cell
 * of the new vector to see if it was => 2, if so the for loop would break and the function would return the value that was
 * selected in the OG vector. I'm not sure if that made sense but I think that would've worked in linear complexity and
 * I just anted to share that to see what you think. */

#include <iostream>
#include "../stanflib/include/vector.h"
#include "../stanflib/include/random.h"
using namespace std;

Vector<int> genVec(int size);
int aDupLinear(Vector<int> & in);
//int aDupeQuad(Vecotr<int> in);

int main() {
    Vector<int> vec = genVec(10);
    cout << vec.toString() << "\n";
    cout << "Dupe: " << aDupLinear(vec);
    return 0;
}

Vector<int> genVec(int size) {
    Vector<int> out;
    for (int i = 0; i < size; i++) {
        out.add(randomInteger(1, size-1));
    }
    return out;
}

int aDupLinear(Vector<int> & in) {
    int temp;
    int v;
    int i = 0;
//    for (i = 0; i < in.size; i++) {
//        if (in[i] < temp) {
//            temp = in[i];
//        }
//    }
    while (in[i] != in[in[i]]) {
        temp = in[i];
        v = in[in[i]];
        //cout << temp << endl;
        //cout << v << endl;
        if (i >= in.size()) {i = 0;}
        i++;
    }
    //temp = v/temp;
    return temp;
}