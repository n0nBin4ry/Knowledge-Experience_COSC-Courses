//
// Created by Richard Flores on 4/19/2017.
//

#include <iostream>
#include "../stanflib/include/grid.h"
#include "../stanflib/include/vector.h"
using namespace std;

void reshape(Grid<int> & grid, int nCols, int nRows);

int main() {
    Grid<int> OG{{1,2,3,4},{5,6,7,8},{9,10,11,12}}; // using original grid from example
    cout << "First we have this original grid:\n" << OG.toString2D() << "\nNow let's reshape it!\n";
    cout << "New column dimension (x) as integer:\n> ";
    int nC;
    cin >> nC;
    cout << "New row dimension (y) as integer:\n> ";
    int nR;
    cin >> nR;
    cout << "Processing. . .\n";
    reshape(OG, nC, nR);
    cout << "New grid:\n" << OG.toString2D();
    return 0;
}

void reshape(Grid<int> & grid, int nCols, int nRows) {
    int length = grid.size();
    Vector<int> holder;
    for (int j = 0; j < grid.height(); j++) {
        for (int i = 0; i < grid.width(); i++) {
            holder.add(grid[j][i]);
        }
    }
    //cout << holder.toString();
    Grid<int> newGrid(nRows, nCols);
    int v = 0;
    for (int j = 0; j < newGrid.height(); j++) {
        for (int i= 0; i < newGrid.width(); i++) {
            if (v >= holder.size()) {
                newGrid[j][i] = 0;
            }
            else {
                newGrid[j][i] = holder[v];
            }
            v++;
        }
    }
    grid = newGrid;
}