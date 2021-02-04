#include  <STDIO.H>
#include<string.h>
int fun(int x,int y)
{   static int m=0,i=2;
     i=i+m+1;
     m=i+x+y;
     return m;
}
main()
{   int j=4,m=1,k;
	char ste[]="i love lyd";
	printf("%d\n",strlen(ste));
     k=fun(j,m); 
     printf("%d,",k);
     k=fun(j,m); 
     printf("%d£¬",k);
     k=fun(j,m); 
     printf("%d\n",k);
}


