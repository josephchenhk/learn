#include<stdio.h>
#include <limits.h>
#include <math.h>
#include "add.h"





int main()
{
    printf("%d\n", add(1,2));

    // 用sizeof函数获取字节数
    printf("int 存储大小 : %lu (2^(4*8)=2^32=%f)\n", sizeof(int), pow(2, sizeof(int)*8));


    // 遍历枚举元素
    for (day = MON; day <= SUN; day++) {
        printf("枚举元素：%d \n", day);
    }

    // 类型转换
    int a = 1;
    enum DAY weekend;
    weekend = ( enum DAY ) a;
    printf("weekday=%d \n", weekend);

    return 0;
}