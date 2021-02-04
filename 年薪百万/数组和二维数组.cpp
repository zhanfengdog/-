#include<stdio.h>
int main()//节应用就是取值， 
{int a[3][3]={0};
int i,j,k=0;
for(i=0;i<3;i++) 
{  for(j=0;j<3;j++)
		{a[i][j]=k++;
		}
}
//012 345 678 
printf("*(a+1)= %p\n",*(a+1));
printf("a+1= %p\n",a+1);
printf("&a[1][0]= %p\n",&a[1][0]);	

printf("*(*(a+1))= %d\n",*(*(a+1)));
printf("**(a+1)= %d\n",**(a+1));
printf("*(&a[1][0])= %d\n",*(&a[1][0]));
return 0;
 } 
