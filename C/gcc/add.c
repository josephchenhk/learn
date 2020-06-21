#include <stdlib.h>
#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int max(int x, int y)
{
    return x > y ? x : y;
}

// 回调函数
void populate_array(int *array, size_t arraySize, int (*getNextValue)(void))
{
    for (size_t i=0; i<arraySize; i++)
        array[i] = getNextValue();
}

// 获取随机值
int getNextRandomValue(void)
{
    return rand();
}