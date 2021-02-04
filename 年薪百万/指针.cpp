#include<stdio.h>
int main()
{int a=3;
char b='h';//多了的话，只会输出最后一个hang-g 
int *pa=&a;
char *pb=&b;
printf("*pa=%d\n",*pa);
printf("*pb=%c\n",*pb);
*pa+=3;
*pb='t';
printf("now,*pa=%d\n",*pa);
printf("now,*pb=%c\n",*pb);
printf("sizeof pa=%d\n",sizeof(pa));//测试的是地址长度8个字节 
printf("sizeof pb=%d\n",sizeof(pb));
printf("dizhi b is %p\n",pb);
printf("dizhi a is %p\n",pa);
return 0;
}
