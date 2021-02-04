#include<stdio.h>
#include<string.h>
int main()
{struct Student
	{long num;
	char name[20];
	char sex;
	float score;
	};
struct Student stu_1,stu_2;

struct Student *p;
p=&stu_2;
stu_1.num=10101;
strcpy(stu_1.name,"li lin");
stu_1.sex='M';
stu_1.score=89.5;
stu_2.num=23;
printf("No.%ld\nname:%s\nsex:%c\nscore:%5.1f\n",stu_1.num,stu_1.name,stu_1.sex,stu_1.score);

//printf("\nNo.%ld\nname:%s\nsex:%c\nscore:%5.1f\n",p->num,p->name,p->sex,(*p).score);
printf("%d",p->num);
return 0;
	
	
 } 
