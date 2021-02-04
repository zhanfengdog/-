#include<stdio.h>
#define N 10
void print(int a[]);

void print(int a[])
{int i;
a[2]=250;
for(i=0;i<N;i++)
	{printf("a[%d]=%d\n",i,a[i]);
	}
}

int main()
{int i;
int a[10]={1,2,3,4,5,6,7,8,9,0};
print(a);
printf("\n");
for(i=0;i<10;i++)
	{printf("a[%d]=%d\n",i,a[i]);
	}
return 0;	
}
