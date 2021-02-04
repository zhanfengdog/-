#include<stdio.h>
int main()
{char *p[2]={"梁雅迪","卢颖因"}; //她们是地址 
int i;
for(i=0;i<2;i++)
{	printf("%s\n",p[i]);//取她们的一床，而不是一个手地址 
}
	
	return 0;
}
