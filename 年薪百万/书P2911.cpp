#include<stdio.h> 
void swap(int*,int*);
void swap(int *p1,int *p2)
{int temp;
temp=*p1;*p1=*p2;*p2=temp;
}
int main()
{int a,b,c;
int *p1,*p2,*p3;
printf("请输入三个数:");
scanf("%d%d%d",&a,&b,&c);
p1=&a;p2=&b;p3=&c;
if(a>b) swap(p1,p2);
if(a>c) swap(p1,p3);
if(b>c) swap(p2,p3);
printf("%5d%5d%5d",*p1,*p3,*p2);//p3代表是最大的，内部在变	
	return 0;
}
