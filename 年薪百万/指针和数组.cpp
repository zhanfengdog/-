#include<stdio.h>
int main()
{int a;
int *p=&a;
char str[123];
printf("lyd的生日：");
scanf("%d",&a);
printf("%d\n",a);
printf("zxm的生日：");
scanf("%d",p);
printf("%d\n",*p);
printf("她的名字是");
scanf("%s",str);
printf("jiu shi：%s\n",str) ;
printf("jiu shi：%p\n",str) ;
printf("jiu shi：%p\n",str[0]) ;
return 0;
	
	
	
}
