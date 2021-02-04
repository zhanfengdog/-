#include<stdio.h>
struct Stud
	{int num;
	char name[20];
	int age;
	}stu[3]={{1,"aa",2},{2,"bb",3},{3,"cc",4}};

int main()
{struct Stud *p;
printf("No		  NAME	sex age\n");
for(p=stu;p<stu+3;p++)
	{printf("%d%20s %4d\n",p->num,p->name,p->age);
	}
p=stu;	
printf("%d\n",(++p)->num);				//第二个 
p=(++p);								//第三个 
printf("%d",p[0].num);
return 0;
}
	
