#include <iostream>
#include "../stanflib/include/random.h"
using namespace std;

void genArray(int *ptr, int *length);
void mergeSort(int array[], int *n);
void merge(int array[], int ar1[], int ar2[], int *lA, int *l1, int *l2);
void printArray(int array[], int *length);

int main() {
    cout << "Input length of array:\n> ";
    int length;
    cin >> length;
    int intArray[length];
    int *arrayPtr = intArray;
    genArray(arrayPtr, &length);
    cout << "Original Array: ";
    printArray(intArray, &length);
    mergeSort(intArray, &length);
    cout << "Sorted Array:   ";
    printArray(intArray, &length);
}

// generates array of random integers the size of length and user inputs max range
// later realized I didn't need a pointer to the array but it was good practice and still works exactly the same
void genArray(int *ptr, int *length) {
    cout << "Input max range of integers:\n> ";
    int range;
    cin >> range;
    for (int i = 0; i < *length; i++) {
        *(ptr++) = randomInteger(1, range);
        //ptr++;
    }
}
// merge-sort
void mergeSort(int array[], int *n) {
    if (*n <= 1) {return;}
    int l1 = 0;
    int l2 = 0;
    int ar1[*n / 2];
    int ar2[(*n / 2) + 1]; // added 1 in case the number is odd, if not then the extra spot wont even go into final array
    for (int i = 0; i < *n; i++) {
        if (i < *n / 2) {
            ar1[l1++] = array[i];
        }
        else {
            ar2[l2++] = array[i];
        }
    }
    mergeSort(ar1, &l1);
    mergeSort(ar2, &l2);
    merge(array, ar1, ar2, n, &l1, &l2);
}
//merging part of merge-sort
void merge(int array[], int ar1[], int ar2[], int *lA, int *l1, int *l2) {
    int p1 = 0;
    int p2 = 0;
    for (int i = 0; i < *lA; i++) {
        if (p1 < *l1 && p2 < *l2) {
            if (ar1[p1] < ar2[p2]) {
                array[i] = ar1[p1++];
            }
            else {
                array[i] = ar2[p2++];
            }
        }
        else if (p1 < *l1) {
            array[i] = ar1[p1++];
        }
        else {
            array[i] = ar2[p2++];
        }
    }
}
// outputs array with brakets and commas
void printArray(int array[], int *length) {
    for (int i = 0; i < *length; i++)
    {
        if (i == 0) {cout << "{ ";}
        cout << array[i];
        if (i == *length - 1) {cout << " }\n";}
        else {cout << ", ";}
    }
}
