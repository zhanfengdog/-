#include<stdio.h>
int main()
{int i;

char *cb[]={"Íæ","ºÜºÃ","hh","Ó¢Óï","¾Í"};
char **jia[4];
char **by;
by=&cb[4];
jia[0]=&cb[0];
jia[1]=&cb[1];
jia[2]=&cb[2];
jia[3]=&cb[3];
printf("xiaojiayu:%s\n",*by);
for(i=0;i<4;i++)
{	printf("%s\n",*jia[i]);
 } 
printf("\n");

return 0;
}
