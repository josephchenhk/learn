#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "sample.h"


int main( int argc, char *argv[] ) /* 带参数形式 */
{
    Point *a, *b;
    double dis;

    a = (Point *) malloc(sizeof(Point));
    b = (Point *) malloc(sizeof(Point));

    a->x = 1.0;
    a->y = 2.0;

    b->x = 2.0;
    b->y = 4.0;

    dis = mydistance(a, b);
    printf("Mydistance=%lf",dis);
    return 0;
}