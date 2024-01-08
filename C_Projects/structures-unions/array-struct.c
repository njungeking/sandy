#include<stdio.h>
#include<stdlib.h>

/*Array of structures during
run-time initialization*/

struct students
{
    int sno;
    char name[30];
    float marks;
};

int main()
{
    struct students x[20];
    int i,n;
    printf("Welcome to an array of structures program!\n\n");
    printf("Please enter the number of students you \n"
           "would like to enter: \n\n");
    scanf("%d",&n);
    printf("\nPlease enter the details of %d students \n"
           "in the order of student no, name and percentage scored: \n\n",n);
    for(i=0;i<n;i++)
    scanf("%d%s%f",&x[i].sno,x[i].name,&x[i].marks);
    for(i=0;i<n;i++)
    printf("\n%d\t%s\t%f\n\n",x[i].sno,x[i].name,x[i].marks);
}

