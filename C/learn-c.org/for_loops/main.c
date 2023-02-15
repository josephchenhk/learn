/*
 * Exercise
Calculate the factorial (multiplication of all items array[0] to array[9], inclusive), of the variable array.
 */

#include <stdio.h>

int main() {
    int array[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int factorial = 1;
    int i;

    /* calculate the factorial using a for loop  here*/
    for (i=0; i<10; i++){
        factorial *= array[i];
    }

    printf("10! is %d.\n", factorial);
}
