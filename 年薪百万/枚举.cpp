#include<stdio.h>
int main()
{enum colorname{red,yellow,white,black};
enum colorname color;
for(color=red;color<=black;color=(enum colorname)(color+1))
	switch(color)
	{case red:printf("�첨\n");break; 
	case yellow:printf("�Ʋ���\n");break;
	case white:printf("�ٲ�\t");break;
	case black:printf("����\n");break;
	}





}
