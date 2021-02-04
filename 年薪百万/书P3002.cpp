#include<stdio.h>
#include<string.h>
struct Persn
  {char name[20];
  int count;
   } lover[3]={"z",0,"l",0,"g",0,};
int main()
{int i,j;
char lover_name[20];
for(i=1;i<=10;i++)
   {scanf("%s",lover_name);
   for(j=0;j<3;j++)
	  {if(strcmp(lover_name,lover[j].name)==0) lover[j].count++;
	  }
   }
printf("\n Result:\n");
for(i=0;i<3;i++)
	{printf("%5s:%d\n",lover[i].name,lover[i].count);
	   }   
 return 0;  
   
   
   }   
