//
// Created by Richard Flores on 2/15/2017.
//

#include <iostream>
#include <cmath>
using namespace std;
// func prototypes
void prompt1();
int inpRad();
int inpRect();
double delta(int rad, int rect);
double func1(double delt, int rad, int rect);
void prompt2(double a);
// user inputs radius of circle and number of rectangles used to take area of 1/4 of the circle, program computes
int main()
{
    prompt1();
    int rad = inpRad();
    int rect = inpRect();
    double deltX(delta(rad, rect));
    double out(func1(deltX, rad, rect));
    prompt2(out);
    return 0;
}

void prompt1() // instructs user
{
    cout << "This program will take the radius of a uniform circle and find the area of a quarter of it.\nThe user can"
            " also select how many rectangles to use to find the area." << endl;
}

int inpRad() // returns int for radius
{
    cout << "Input the radius:\n> ";
    int rad;
    cin >> rad;
    return rad;
}

int inpRect() // returns int for rectangles
{
    cout << "Input rectangles:\n> ";
    int rect;
    cin >> rect;
    return rect;
}

double delta(int rad, int rect) // returns delta x; rad/rect
{
    float nRect(rect);
    double a(rad / nRect);
    return a;
}

double func1(double delt, int rad, int rect) // calculates area of quarter circle
{
    double area(0); // initializes output
    double nRad(rad); // makes rad a float
    for (int i = 0; i < rect; i ++)
    {
        double x((delt * i) + (delt/2));
        double y = sqrt(pow(nRad, 2) - pow(x,2));
        area += (delt * y);
    }
    return area;
}

void prompt2(double a) // shows results
{
    cout << "The area of the quarter circle is: " << a;
}