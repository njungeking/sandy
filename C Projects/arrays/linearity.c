#include<stdio.h>
#include<stdlib.h>

/*This program searches linearly
for a value within an array using
run-time initialization*/

void lin(int a[],int n,int key);

int main()
{
    int a[10000],i,n,key;
    printf("Please set the size of your array: \n");
    scanf("%d",&n);
    printf("Please input %d values for your array: \n",n);
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    lin(a,n,key);
}

void lin(int a[],int n,int key)
{
    int flag=0,i;
    printf("Please type the value that you wish to search for: \n");
    scanf("%d",&key);
    for(i=0;i<n;i++)
    {
        if(a[i]==key)
        {
            flag=1;
            break;
        }
    }
    if(flag==1)
    printf("The value: %d is present.\n",key);
    else
    printf("The value: %d is absent. Try again please.\n",key);
}
