//
// Created by Richard Flores on 4/16/2017.
//

#ifndef CH6NUMBER1_H
#define CH6NUMBER1_H

#include <string>
#include "../stanflib/include/gtypes.h"

class gRekt {
public:
    gRekt();
    gRekt(double nX, double nY, double nWidth, double nHeight);
    double getRektX();
    double getRektY();
    double getRektWidth();
    double getRektHeight();
    bool isEmpty();
    bool contains(GPoint pt);
    bool contains(double nX, double nY);
    std::string toString();
private:
    double x;
    double y;
    double width;
    double height;
    friend std::string std::to_string(double in);
};


#endif
