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

    // 指针取地址
    int  var1;
    char var2[10];
    printf("var1 变量的地址： %p\n", &var1  );
    printf("var2 变量的地址： %p\n", &var2  );

    // 指针变量的声明
    int  *ip;
    ip = &var1;
    printf("var1 变量的地址： %p\n", ip  );

    return 0;
}