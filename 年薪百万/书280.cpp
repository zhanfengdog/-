#include<stdio.h>
int main()
{char *name[]={"i","believe","i","can","fly"};
char **p;
int i;
for(i=0;i<5;i++)
	{p=name+i;
	printf("%s\n",*p);
	}
return 0; 
 } 
