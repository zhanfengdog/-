#include<stdio.h>
int main()
{int a;
int *p=&a;
char str[123];
printf("lyd�����գ�");
scanf("%d",&a);
printf("%d\n",a);
printf("zxm�����գ�");
scanf("%d",p);
printf("%d\n",*p);
printf("����������");
scanf("%s",str);
printf("jiu shi��%s\n",str) ;
printf("jiu shi��%p\n",str) ;
printf("jiu shi��%p\n",str[0]) ;
return 0;
	
	
	
}
