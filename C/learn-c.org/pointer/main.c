/*
 * Dereferencing
Dereferencing is the act of referring to where the pointer points, instead of the memory address. We are already using
dereferencing in arrays - but we just didn't know it yet. The brackets operator - [0] for example, accesses the first
item of the array. And since arrays are actually pointers, accessing the first item in the array is the same as
dereferencing a pointer. Dereferencing a pointer is done using the asterisk operator *.

Exercise
Create a pointer to the local variable n called pointer_to_n, and use it to increase the value of n by one.
 */

#include <stdio.h>

int main() {
    int n = 10;

    /* your code goes here */
    int * pointer_to_n = &n;
    *pointer_to_n += 1;

    /* testing code */
    if (pointer_to_n != &n) return 1;
    if (*pointer_to_n != 11) return 1;

    printf("Done!\n");
    return 0;
}