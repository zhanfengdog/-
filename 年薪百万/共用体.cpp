#include<stdio.h>
int main()
{  union exx
	{int b;
	int  a;
	struct Rnn
	 {int c;
	 int d;
	 }lpp;
	}e={10};
e.b=e.a+20;
e.lpp.c=e.a+e.b;
e.lpp.d	=e.a*e.b;
printf("e.a=%d\n",e.a);
printf("e.b=%d,e.lpp.c=%d,e.lpp.d=%d\n",e.b,e.lpp.c,e.lpp.d); 
	
 } 
