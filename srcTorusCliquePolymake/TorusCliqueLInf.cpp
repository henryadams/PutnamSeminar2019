#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include <math.h>

// Returns the "L infinity" distance between vertices i and j on the torus grid graph which is the product of two cyclic graphs, each with n vertices.
int distance(int i, int j, int n) {
    int i1 = i % n;
    int i2 = (i-i1) / n;
    int j1 = j % n;
    int j2 = (j-j1) / n;
    return std::max(std::min(abs(i1-j1), n-abs(i1-j1)), std::min(abs(i2-j2), n-abs(i2-j2)));
}

// Prints the edges of the "L infinity" k-th graph power of torus grid graph which is the product of two cyclic graphs, each with n vertices.
void PowerOfTorusGridGraph(int n, int k) {
    int first=1;
    for (int i=0; i<pow(n,2); i++) {
        for (int j=i+1; j<pow(n,2); j++) {
            if (distance(i,j,n) <= k) {
                if (!first) printf(","); else first=0;
                printf("[%d,%d]", i,j); }
        }
    }
}

int main(int argc, char **argv) {
    // The below two lines are used to input using a bash script
    int n = atoi(argv[1]);
    int k = atoi(argv[2]);
    PowerOfTorusGridGraph(n,k);
    return 0;
}

