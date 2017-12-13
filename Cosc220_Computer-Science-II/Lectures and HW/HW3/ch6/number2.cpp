//
// Created by Richard Flores on 4/18/2017.
// the problem wants: n_across = 50, n_across = 30, delta = 67; but I made a user input section.

#include "../stanflib/include/gwindow.h"
#include <iostream>
using namespace std;

void createPegs(int across, int down, int delta, Vector<GPoint> & in);
void drawLines(int delta, Vector<GPoint> & in, GWindow & screen);

int main() {
    cout << "How many pegs across?\n> ";
    int n_Across;
    cin >> n_Across;
    cout << "How many pegs down?\n> ";
    int n_Down;
    cin >> n_Down;
    cout << "Input Delta:\n> ";
    int delta;
    cin >> delta;
    cout << "Loading. . .\n";
    Vector<GPoint> rektPegs;
    createPegs(n_Across, n_Down, delta, rektPegs);
    //cout << rektPegs.toString();
    // creates screen
    GWindow screen(500,500);
    screen.setColor("#210132"); // sets drawing color
    // for background color because why not
    screen.fillRect(0,0,700,700);
    // changes drawing color
    screen.setColor("#013208");
    drawLines(delta, rektPegs, screen);
    // makes screen visible
    screen.setVisible(true);
    cout << "Complete!";
    return 0;
}
// creates all the pegs from the inputted values and places the, into the in GPoint vector
void createPegs(int across, int down, int delta, Vector<GPoint> & in) {
    int m = 10;
    for (int i = 0; i < across; i++) {
        in.add(GPoint(i * m, 0));
    }
    for (int j = 1; j < down; j++) {
        in.add(GPoint((across - 1) * m, j * m));
    }
    for (int i = across - 2; i >= 0; i--) {
        in.add(GPoint(i * m, (down - 1) * m));
    }
    for (int j = down - 2; j > 0; j--) {
        in.add(GPoint(0, j * m));
    }
}
// takes the GPoints from the in vector and uses those to draw the lines the way the problem specifies
void drawLines(int delta, Vector<GPoint> & in, GWindow & screen) {
    bool out(true);
    int start(0);
    int tempStart;
    while (out) {
        if ((start + delta) >= in.size()) {
            tempStart = (start + delta) % in.size();
            screen.drawLine(in[start], in[tempStart]);
            start = tempStart;
        }
        else {
            screen.drawLine(in[start], in[start + delta]);
            start += delta;
        }
        if (start == 0) {
            out = false;
        }
    }
}