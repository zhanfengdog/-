#include<stdio.h>

struct Student{
		char xingming[20];
		int xuehao;
		float yu;
		float math;
		}student; 
		
	struct Student getinput(struct Student student)
	{
	printf("请你输入姓名:");
	scanf("%s",student.xingming);
	 
	printf("请你输入学号：");
	scanf("%d",&student.xuehao);
	 
	printf("请你输入语文成绩：");
	scanf("%f",&student.yu); 
		
	printf("请你输入数学：");
	scanf("%f",&student.math);
	return student; 	
	};
	
	void outprint(struct Student student)	
	{printf("%s\n",student.xingming);	
	printf("%d\n",student.xuehao); 	
	printf("%5.1f\n",student.yu);
	printf("%5.1f\n",student.math);
	}
void aver(float n1,float n2,float n3,float n4,float n5)
	{float ver;
	ver=(n1+n2+n3+n4+n5)/5;
		printf("aver=%f",ver); 
		}		
int main()
{float n1,n2,n3,n4,n5;

struct Student s1,s2,s3,s4,s5;
	printf("请输入第一个学生：\n");
	s1=getinput(s1);
	outprint(s1);
	printf("请输入第二个学生：\n");
	s2=getinput(s2);
	outprint(s2);
	printf("请输入第三个学生：\n");
	s3=getinput(s3);
	outprint(s3);
	printf("请输入第四个学生：\n");
	s4=getinput(s4);
	outprint(s4);
	printf("请输入第五个学生：\n");
	s5=getinput(s5);
	outprint(s5);
	aver(s1.yu,s2.yu,s3.yu,s4.yu,s5.yu);
	aver(s1.math,s2.math,s3.math,s4.math,s5.math);
	return 0;
}		
