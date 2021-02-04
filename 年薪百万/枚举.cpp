#include<stdio.h>
int main()
{enum colorname{red,yellow,white,black};
enum colorname color;
for(color=red;color<=black;color=(enum colorname)(color+1))
	switch(color)
	{case red:printf("ºì²¨\n");break; 
	case yellow:printf("»Æ²¨ÕÖ\n");break;
	case white:printf("°Ù²¨\t");break;
	case black:printf("ºÚÕÖ\n");break;
	}





}
