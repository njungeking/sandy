#include<stdio.h>
#include<stdlib.h>

/*Array within structures
during run-time initialization*/

struct students
{
    int rollno;
    char name[20];
    int marks[6];
    int sum;
    float per;
};

int main()
{
    struct students x[10];
    int i,j,n;
    printf("Welcome to an student percentage calculator!\n\n");
    printf("Please enter the number of students that you would \n"
           "to enter: \n\n");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("\nPlease enter the roll no. and name of student %d:\n\n",i+1);
        scanf("%d%s",&x[i].rollno,x[i].name);
        printf("\nPlease enter the marks scored by %s in six subjects: \n\n",x[i].name);
        for(j=0;j<6;j++)
        scanf("%d",&x[i].marks[j]);
    }
    for(i=0;i<n;i++)
    {
        x[i].sum=0;
        for(j=0;j<6;j++)
        x[i].sum += x[i].marks[j];
        x[i].per=((float)x[i].sum/6);
    }
    printf("\nRoll no\t\tName\t\tSum\t\tPercentage\n\n");
    for(i=0;i<n;i++)
    printf("%d\t\t%s\t\t%d\t\t%f\n",x[i].rollno,x[i].name,x[i].marks[j],x[i].per);
}

