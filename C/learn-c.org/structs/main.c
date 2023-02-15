/*
 * Exercise
Define a new data structure, named "person", which contains a string (pointer to char) called name, and an integer
called age.
 */

#include <stdio.h>

struct point {
    int x;
    int y;
};


typedef struct {
    char * name;
    int age;
} person;

/* define the person struct here using the typedef syntax */

int main() {
    struct point p;
    p.x = 1;
    p.y = 2;
//    printf("point(%d, %d)\n", p.x, p.y);

    person john;
    /* testing code */
    john.name = "John";
    john.age = 27;
    printf("%s is %d years old.", john.name, john.age);
}
