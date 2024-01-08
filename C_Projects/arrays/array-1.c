#include<stdio.h>
#include<stdlib.h>

/*Displaying the content of a one dimensional
array using compile-time initialization*/

void main()
{
    int num[10]={0,10,20,30,40,50,60,70,80,90},i;
    printf("The Elements of the 'num' array are: \n\n");
    for(i=0;i<10;i++)
    printf("%d\t",num[i]);
    printf("\n");
}
