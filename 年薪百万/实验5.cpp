//有5个学生，每个学生有语文和数学2个成绩，
//从键盘录入学生学号和成绩，计算出平均成绩，
//并将学生信息和平均成绩保存到文件stud中。
#include<stdio.h>
struct Student{
		char xingming[20];
		int xuehao;
		float yu;
		float math;
		}student1;
int main()
{struct Student *pt;
*pt=&student1;
printf("请你输入姓名:");
scanf("%s",pt.xingming); 
printf("请你输入学号：");
scanf("%d",&student1.xuehao); 
printf("请你输入语文成绩：");
scanf("%f",&student1.yu); 	
printf("请你输入数学：");
scanf("%f",&student1.math); 	
 	
printf("%s\n",student1.xingming);	
printf("%d\n",student1.xuehao); 	
printf("%5.1f\n",student1.yu);
printf("%5.1f\n",student1.math);	
	return 0;
}		
