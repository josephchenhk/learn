#include<stdio.h>
#include <errno.h>
#include <string.h>
#include <limits.h>
#include <math.h>
#include <stdlib.h>
#include "add.h"


#define  message_for(a, b)  \
    printf(#a " and " #b ": We love you!\n")

#define tokenpaster(n) printf("token" #n " = %d", token##n)  //一个#号将变量变成字符串；两个#号将粘贴成新变量


extern int errno;

int main(int argc, char *argv[])
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
    printf("\n");



    // 字符串终止（ null 字符 '\0' 终止的一维字符数组）
    char greeting1[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
    char greeting2[] = "World"; // 您不需要把 null 字符放在字符串常量的末尾。C 编译器会在初始化数组时，自动把 '\0' 放在字符串的末尾
    printf("Greeting message: %s %s\n", greeting1, greeting2 );

    /*
    序号	函数 & 目的
    1	strcpy(s1, s2);
    复制字符串 s2 到字符串 s1。
    2	strcat(s1, s2);
    连接字符串 s2 到字符串 s1 的末尾。
    3	strlen(s1);
    返回字符串 s1 的长度。
    4	strcmp(s1, s2);
    如果 s1 和 s2 是相同的，则返回 0；如果 s1<s2 则返回小于 0；如果 s1>s2 则返回大于 0。
    5	strchr(s1, ch);
    返回一个指针，指向字符串 s1 中字符 ch 的第一次出现的位置。
    6	strstr(s1, s2);
    返回一个指针，指向字符串 s1 中字符串 s2 的第一次出现的位置。
    */



    // 预定义宏
    printf("File :%s\n", __FILE__ );
    printf("Date :%s\n", __DATE__ );
    printf("Time :%s\n", __TIME__ );
    printf("Line :%d\n", __LINE__ );
    printf("ANSI :%d\n", __STDC__ );



    // 字符串常量化运算符（#）一个#号将参数变成字符串
    message_for(Carole, Debra);
    int token34 = 119;
    tokenpaster(34);



    // 错误处理
    FILE * pf;
    int errnum;
    pf = fopen ("unexist.txt", "rb");
    if (pf == NULL)
    {
        errnum = errno;
        fprintf(stderr, "错误号: %d\n", errno);
        perror("通过 perror 输出错误");
        fprintf(stderr, "打开文件错误: %s\n", strerror( errnum ));
    }
    else
    {
        fclose (pf);
    }



    // 可变数量的参数
    printf("\n");
    printf("Average of 2, 3, 4, 5 = %f\n", average(4, 2,3,4,5)); // 第一个参数是变量个数，4个变量
    printf("Average of 5, 10, 15 = %f\n", average(3, 5,10,15));  // 第一个参数是变量个数，3个变量




    // 内存分配
    char name[100];
    char *description;

    strcpy(name, "Zara Ali");

    /* 动态分配内存 */
    printf("sizeof(char)=%lu\n", sizeof(char));
    description = (char *)malloc( 30 * sizeof(char) );
    if( description == NULL )
    {
        fprintf(stderr, "Error - unable to allocate required memory\n");
    }
    else
    {
        strcpy( description, "Zara ali a DPS student.");
    }
    /* 假设您想要存储更大的描述信息 */
    description = (char *) realloc( description, 100 * sizeof(char) );
    if( description == NULL )
    {
        fprintf(stderr, "Error - unable to allocate required memory\n");
    }
    else
    {
        strcat( description, "She is in class 10th");
    }

    printf("Name = %s\n", name );
    printf("Description: %s\n", description );

    /* 使用 free() 函数释放内存 */
    free(description);



    // 命令行参数
    if( argc == 2 )
    {
        printf("The argument supplied is %s\n", argv[1]);
    }
    else if( argc > 2 )
    {
        printf("Too many arguments supplied.\n");
    }
    else
    {
        printf("One argument expected.\n");
    }

    return 0;
}