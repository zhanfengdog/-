#include<stdio.h>

struct Student{
		char xingming[20];
		int xuehao;
		float yu;
		float math;
		}student; 
		
	struct Student getinput(struct Student student)
	{
	printf("������������:");
	scanf("%s",student.xingming);
	 
	printf("��������ѧ�ţ�");
	scanf("%d",&student.xuehao);
	 
	printf("�����������ĳɼ���");
	scanf("%f",&student.yu); 
		
	printf("����������ѧ��");
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
	printf("�������һ��ѧ����\n");
	s1=getinput(s1);
	outprint(s1);
	printf("������ڶ���ѧ����\n");
	s2=getinput(s2);
	outprint(s2);
	printf("�����������ѧ����\n");
	s3=getinput(s3);
	outprint(s3);
	printf("��������ĸ�ѧ����\n");
	s4=getinput(s4);
	outprint(s4);
	printf("����������ѧ����\n");
	s5=getinput(s5);
	outprint(s5);
	aver(s1.yu,s2.yu,s3.yu,s4.yu,s5.yu);
	aver(s1.math,s2.math,s3.math,s4.math,s5.math);
	return 0;
}		
