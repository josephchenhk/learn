/* sample.c */
#include <math.h>

/* Compute the greatest common divisor */
int gcd(int x, int y);

/* Test if (x0,y0) is in the Mandelbrot set or not */
int in_mandel(double x0, double y0, int n);

/* Divide two numbers */
int divide(int a, int b, int *remainder);

/* Average values in an array */
double avg(double *a, int n);

/* A C data structure */
typedef struct Point {
    double x,y;
} Point;

/* Function involving a C data structure */
double distance(Point *p1, Point *p2);


/* sample.h */

//#include <math.h>
//
//extern int gcd(int, int);
//extern int in_mandel(double x0, double y0, int n);
//extern int divide(int a, int b, int *remainder);
//extern double avg(double *a, int n);
//
//typedef struct Point {
//    double x,y;
//} Point;
//
//extern double distance(Point *p1, Point *p2);
