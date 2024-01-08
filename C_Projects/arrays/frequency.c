#include<stdio.h>
#include<stdlib.h>

/*Finding the frequency of a
given element in a sorted array*/

void freq(int a[],int n,int x);

int main()
{
    int a[10000],i,n,x;
    printf("Please set the size of your array: \n");
    scanf("%d",&n);
    printf("Please enter %d values for your array: \n",n);
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    freq(a,n,x);
}

void freq(int a[],int n,int x)
{
    int count=0,i;
    printf("Please type the value you wish to get the frequency of: \n");
    scanf("%d",&x);
    for(i=0;i<n;i++)
    {
        if(x==a[i])
        count++;

        if(a[i]>x)
        break;
    }
    printf("The frequency of %d is: %d in this array.\n",x,count);
}
