#include<stdio.h>
int main()
{int i,j;
int a[][3]={0};	
for(i=0;i<3;i++)
{	for(j=0;j<3;j++)
		{scanf("%d,",&a[i][j]);
		
		}
	}	
printf("shujinqu:\n");
for(i=0;i<3;i++)
{	for(j=0;j<3;j++)
		{printf("%5d",a[i][j]);
		
		}
	printf("\n");	
}	
printf("shujinqu:\n");
for(i=0;i<3;i++)
{	for(j=0;j<3;j++)
		{printf("%5d",a[j][i]);
	}
	printf("\n");	
}	
return 0;
 } 
