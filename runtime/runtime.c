#include<stdio.h>
#include<stdlib.h>

/*Another one on displaying an
array using run-time initialization*/

void main()
{
    int digs[1000],i,n;
    printf("Please set the size of your array:\n");
    scanf("%d",&n);
    printf("\nPlease input %d values for your array.\n",n);
    for(i=0;i<n;i++)
    scanf("%d",&digs[i]);
    printf("\nThe %d contents of your array are: \n",n);
    for(i=0;i<n;i++)
    printf("%d\t",digs[i]);
    printf("\n");
}
