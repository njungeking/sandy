#include<stdio.h>
#include<stdlib.h>

/*The addition of three values
by passing on pointers as parameters
to a function(call by reference) during
run-time initialization*/

void sum(int *p,int *q,int *r);

int main()
{
    int a,b,c;
    printf("Welcome to a sum addition program!\n\n");
    printf("Please enter three values you would "
           "wish to add: \n\n");
    scanf("%d%d%d",&a,&b,&c);
    sum(&a,&b,&c);
}

void sum(int *p,int *q,int *r)
{
    int ans;
    ans=*p+*q+*r;
    printf("\nThe final result is: %d\n\n",ans);
}

