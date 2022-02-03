/*
 * Let's assume we want to dynamically allocate a person structure. The person is defined like this:

typedef struct {
    char * name;
    int age;
} person;

To allocate a new person in the myperson argument, we use the following syntax:

person * myperson = (person *) malloc(sizeof(person));

------------------------------------------------------------------------------------------------------------------------
 Exercise
Use malloc to dynamically allocate a point structure.
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x;
    int y;
} point;

int main() {
    point * mypoint = NULL;

    /* Dynamically allocate a new point
       struct which mypoint points to here */
    mypoint = (point *) malloc(sizeof(point));

    mypoint->x = 10;
    mypoint->y =5 ;
    printf("mypoint coordinates: %d, %d\n", mypoint->x, mypoint->y);

    /*
     * Remember to free the memory
     */
    free(mypoint);
    return 0;
}