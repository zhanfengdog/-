#include<stdio.h>
int main()
{int num=1024;
int *pa=&num;
char *ps="lyd";
void *pv;
pv=pa;
printf("pa=%p,pv=%p\n",pa,pv);
printf("*(int *)pv= %d\n",*(int *)pv);

pv=ps;
printf("ps=%p,pv=%p\n",ps,pv);
printf("(char *)pv=%s\n",(char *)pv);	
	
	
	
 } 
