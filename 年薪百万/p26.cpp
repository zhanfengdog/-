#include<stdio.h>
int main()
{int num=102;
int *p=&num;
int **pp=&p;
printf("num=%d\n",num);
printf("*p=%d\n",*p);	
printf("**pp=%d\n",**pp);	
printf("&num=%p,p=%p\n",&num,p);	
printf("&p=%p,pp=%p\n",&p,pp);	
return 0;
 } 
