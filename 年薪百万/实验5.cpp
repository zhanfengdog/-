//��5��ѧ����ÿ��ѧ�������ĺ���ѧ2���ɼ���
//�Ӽ���¼��ѧ��ѧ�źͳɼ��������ƽ���ɼ���
//����ѧ����Ϣ��ƽ���ɼ����浽�ļ�stud�С�
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
printf("������������:");
scanf("%s",pt.xingming); 
printf("��������ѧ�ţ�");
scanf("%d",&student1.xuehao); 
printf("�����������ĳɼ���");
scanf("%f",&student1.yu); 	
printf("����������ѧ��");
scanf("%f",&student1.math); 	
 	
printf("%s\n",student1.xingming);	
printf("%d\n",student1.xuehao); 	
printf("%5.1f\n",student1.yu);
printf("%5.1f\n",student1.math);	
	return 0;
}		
