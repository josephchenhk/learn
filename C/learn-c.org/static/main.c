/*
 * static is a keyword in the C programming language. It can be used with variables and functions.

What is a static variable?
By default, variables are local to the scope in which they are defined. Variables can be declared as static to increase
their scope up to file containing them. As a result, these variables can be accessed anywhere inside a file.

What is a static function?
By default, functions are global in C. If we declare a function with static, the scope of that function is reduced to
the file containing it.

Exercise
In this exercise, try to find the sum of some numbers by using the static keyword. Do not pass any variable representing
the running total to the sum() function.
 */

#include <stdio.h>
int sum (int num) {
    /**
    * find sum to n numbers
    */
    static int _sum = 0;
    _sum += num;
    return _sum;
}

int main() {
    printf("%d ",sum(55));
    printf("%d ",sum(45));
    printf("%d ",sum(50));
    return 0;
}