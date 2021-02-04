#include<stdio.h>
#include<string.h>
int main()
{char a[]="wo xihuan lyd";
char *str="i love zxm.";
int len,i;
char *p=a;
printf("*p=%c,*(p+1)=%c,*p+1=%c\n",*p,*(p+1),*p+1);/* p+1=x */
len=strlen(str); 
for(i=0;i<len;i++)

	{
	printf("%c",str[i]);
	}
printf("\n");	
	

return 0; 
 } 
