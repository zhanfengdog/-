#include<stdio.h>
int main()
{int a[10],i,*p;
printf("������10�����֣�");
for(i=0;i<10;i++)
	{scanf("%d",&a[i]);
	}
for(p=a,i=1;p<(a+10);p++,i++)
	{printf("a[%d]=%d\n",i,*p);
	}
	return 0;
 } 
