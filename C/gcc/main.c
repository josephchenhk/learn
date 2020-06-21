#include<stdio.h>
#include <limits.h>
#include <math.h>

int add(int a, int b);
int main()
{
    printf("%d\n", add(1,2));

    printf("int 存储大小 : %lu (2^(4*8)=2^32=%f)\n", sizeof(int), pow(2, sizeof(int)*8));


    return 0;
}