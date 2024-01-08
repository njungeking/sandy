#include<stdio.h>
#include<stdlib.h>

/*Displaying the content of an array
using run-time initialization by calling
another function*/

void disp(int arr[],int n);

int main()
{
    int arr[1000],i,n;
    printf("Please set the size of your array: \n");
    scanf("%d",&n);
    printf("Please input %d values for your array: \n",n);
    disp(arr,n);
}

void disp(int arr[],int n)
{
    int i;
    for(i=0;i<n;i++)
    scanf("%d",&arr[i]);
    printf("The %d contents of your array are: \n",n);
    for(i=0;i<n;i++)
    printf("%d\t",arr[i]);
}

