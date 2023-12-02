#include<stdio.h>
#include<stdlib.h>

/*This is a recap on the count of
an element within an array combined
with sorting and display*/

void disp(int a[],int n);

void count(int a[],int n,int x);

int main()
{
    int a[10000],i,n,j,temp,x;
    printf("Please set the size of your array: \n");
    scanf("%d",&n);
    printf("Please enter %d values for your array: \n",n);
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    printf("The values you put in random order are: \n");
    disp(a,n);
    count(a,n,x);
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(a[i]>a[j])
            {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
    printf("After sorting of the elements: \n");
    disp(a,n);
}

void disp(int a[],int n)
{
    int i;
    for(i=0;i<n;i++)
    printf("%d\t",a[i]);
    printf("\n");
}

void count(int a[],int n,int x)
{
    int i,count=0;
    printf("Please input the value you want a count for: \n");
    scanf("%d",&x);
    for(i=0;i<n;i++)
    {
        if(x==a[i])
        count++;
    }
    printf("\nThe value %d is present: %d times.\n\n",x,count);
}
