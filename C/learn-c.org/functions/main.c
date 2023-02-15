/*
 * Exercise
Write a function called print_big which receives one argument (an integer) and prints the line x is big (where x is the
argument) if the argument given to the function is a number bigger than 10.

Important: Don't forget to add a newline character \n at the end of the printf string.
 */

#include <stdio.h>

/* function declaration */
void print_big(int number);

int main() {
    int array[] = { 1, 11, 2, 22, 3, 33 };
    int i;
    for (i = 0; i < 6; i++) {
        print_big(array[i]);
    }
    return 0;
}

/* write your function here */
void print_big(int number){
    if (number > 10){
        printf("%d is big\n", number);
    }
}
