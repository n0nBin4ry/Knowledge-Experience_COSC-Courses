//
// Created by Richard Flores on 2/10/2017.
//

#include <iostream>
using namespace std;
// func prototypes
int input();
int length(int a);
long long int flip(int a, int b);
void output(int a, long long int b);
long long int powOfTen(int a);

// the main function of this program is to invert an integer the user inputs
int main()
{
    int in = input();
    // I let the user know their input exceeds the memory limitation if int, since it'll automatically go down to its max or min
    int lim(2147483647);
    int negLim(-2147483647);
    if (in == lim) {cout << "Your input was reduced to 2,147,483,647." << endl;}
    if (in == negLim) {cout << "Your input was increased to -2,147,483,648." << endl;}
    int inLen = length(in);
    long long int out = flip(in, inLen);
    output(in, out);
    return 0;
}
// user inputs integer
int input()
{
    cout << "Input an integer of up to 10 digits (greater than -2,147,483,647 and less than 2,147,483,647) to reverse: ";
    int a;
    cin >> a;
    return a;
}
// gets the length of the arg
int length(int a)
{
    int i = 10;
    while (true)
    {
        if ((a % powOfTen(i)) != a)
        {
            return (i + 1);
        }
        i --;
    }
}
// uses an algorithm to invert an integer using (a)the integer and (b)its length as the args
long long int flip(int a, int b)
{
    long long int part1, part2, part3, part4;
    long long int out = 0, oldPart1 = 0;
    for (int i = 0; i < b; i++)
    {
        part1 = a % powOfTen(i + 1);
        part2 = part1 - oldPart1;
        part3 = part2 / powOfTen(i);
        part4 = part3 * powOfTen(b - (i + 1));
        out = out + part4;
    }
    return out;
}
// reminds user of (a)the number they input and shows them (b) the new inverted number
void output(int a, long long int b)
{
    cout << "The reverse of " << a << " is: " << b << endl;
}
// calculates 10 to the power of arg
long long int powOfTen(int a)
{
    long long int x = 1;
    for (int i = a; i >= 1; i--)
    {
        x = x * 10;
    }
    return x;
}