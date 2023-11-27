#include<stdio.h>
#include<stdlib.h>

/*The sum of the contents of an array
using a function and run-time initialization*/

void summation(int arr_sum[], int n);

int main()
{
    int arr_sum[100000],i,n;
    printf("Please set the size of your array: \n");
    scanf("%d",&n);
    printf("Please input %d values for your array: \n",n);
    summation(arr_sum,n);
}

void summation(int arr_sum[], int n)
{
    int i,sum=0;
    for(i=0;i<n;i++)
    scanf("%d",&arr_sum[i]);
    printf("The sum of the %d values of your array is: ",n);
    for(i=0;i<n;i++)
    sum=sum+arr_sum[i];
    printf("%d",sum);
    printf("\n");
}
