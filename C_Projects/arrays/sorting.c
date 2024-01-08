#include<stdio.h>
#include<stdlib.h>

/*Sorting of the elements of an
array coupled with a before and
after display function*/

int disp(int a[],int n);

int main()
{
    int a[10000],i,n,j,temp;
    printf("Please set the size of your array: \n");
    scanf("%d",&n);
    printf("\nPlease enter %d elements for your array: \n",n);
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    printf("\nBefore sorting of your elements: \n");
    disp(a,n);
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
    printf("\nAfter sorting of your elements: \n");
    disp(a,n);
}

int disp(int a[],int n)
{
    int i;
    for(i=0;i<n;i++)
    printf("%4d",a[i]);
    printf("\n");
}
