#include<stdio.h>//Ϊ������д���� 
struct Date
	{char name[10];
	int year;
	int month;
	int day;
	char x;
	 } a={"���ŵ�",2020,12,29,'w'}, b={"zhan",2030,11,28,'m'};
struct Student
	{int num;
	char name[20];
	char sex;
	struct Date a;
	char addr[20];
		 };
int main()
{a.year=2000;				//jia" ,���¸�ֵ 
printf("wedding.name=%s\n wedding.year=%d\n  wedding.month=%d\n   wedding.day=%d\n",a.name,a.year,a.month,a.day);
printf("a.x=%c\n",a.x);
printf("b.x=%c\n",b.x);
 return 0;
}		 	 
