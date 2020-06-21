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


    /* p 是函数指针 */
    int (* p)(int, int) = & max; // &可以省略
    int a1, b, c, d;
    printf("请输入三个数字:");
//    scanf("%d %d %d", & a, & b, & c);
    a1 = 1;
    b = 2;
    c = 6;
    /* 与直接调用函数等价，d = max(max(a, b), c) */
    d = p(p(a1, b), c);
    printf("最大的数字是: %d\n", d);


    // 回调函数指针
    int myarray[10];
    populate_array(myarray, 10, getNextRandomValue);
    for(int i = 0; i < 10; i++) {
        printf("%d ", myarray[i]);
    }

    return 0;
}