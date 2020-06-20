/* sample.c */
#include <math.h>

/* Compute the greatest common divisor */
extern int gcd(int, int);

/* Test if (x0,y0) is in the Mandelbrot set or not */
extern int in_mandel(double x0, double y0, int n);

/* Divide two numbers */
extern int divide(int a, int b, int *remainder);

/* Average values in an array */
extern double avg(double *a, int n);

/* A C data structure */
typedef struct Point {
    double x,y;
} Point;

/* Function involving a C data structure */
extern double mydistance(Point *p1, Point *p2);