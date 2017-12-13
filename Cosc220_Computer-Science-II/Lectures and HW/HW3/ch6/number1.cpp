//
// Created by Richard Flores on 4/16/2017.
// need to check negative dimensions when using contains methods

#include "number1.h"

gRekt::gRekt() {
    x = 0;
    y = 0;
    width = 0;
    height = 0;
}
gRekt::gRekt(double nX, double nY, double nWidth, double nHeight) {
    x = nX;
    y = nY;
    width = nWidth;
    height = nHeight;
}
double gRekt::getRektX() {
    return x;
}
double gRekt::getRektY() {
    return y;
}
double gRekt::getRektWidth() {
    return width;
}
double gRekt::getRektHeight() {
    return height;
}
bool gRekt::isEmpty() {
    if ( width == 0 && height == 0 ) {
        return true;
    }
    else {
        return false;
    }
}
bool gRekt::contains(double nX, double nY) {
    if ( (getRektX() <= nX <= getRektX() + getRektWidth()) && (getRektY() <= nY <= getRektY() + getRektHeight()) ) {
        return true;
    }
//    else if ( (x >= nX >= x + width) && (y <= nY <= y + height) ) {
//
//    }
    else {
        return false;
    }
}
bool gRekt::contains(GPoint pt) {
    if ( (getRektX() <= pt.getX() <= getRektX() + getRektWidth()) && (getRektY() <= pt.getY() <= getRektY() + getRektHeight()) ) {
        return true;
    }
    else {
        return false;
    }
}
std::string gRekt::toString() {
    return "( " + std::to_string(getRektX()) + ", " + std::to_string(getRektY()) + ", " + std::to_string(getRektWidth()) + ", " + std::to_string(getRektHeight()) + " )";
}
