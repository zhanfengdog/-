#include<stdio.h>
int isleapyear(int year)
{return (year%400==0||(year%4==0)&&(year%100!=0));
}
int main()
{int isleapyear(int year);
int n,t;
printf("��������:");
scanf("%d",&n);
t=isleapyear(n);
if(t==1)
	{printf("���ˣ����");
	} 
	else
	{printf("��һ��������");
	}	 
	
	return 0;
}




