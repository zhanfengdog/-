#include<stdio.h>
int isleapyear(int year)
{return (year%400==0||(year%4==0)&&(year%100!=0));
}
int main()
{int isleapyear(int year);
int n,t;
printf("请输入年:");
scanf("%d",&n);
t=isleapyear(n);
if(t==1)
	{printf("对了，真棒");
	} 
	else
	{printf("换一个，加油");
	}	 
	
	return 0;
}




