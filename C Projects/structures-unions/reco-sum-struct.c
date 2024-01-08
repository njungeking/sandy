#include<stdio.h>
#include<stdlib.h>

/*Another recap on arrays
within structures during run-time
initialization*/

struct students
{
    int rollno;
    char name[30];
    int marks[6];
    int sum;
    float per;
};

int main()
{
    struct students x[20];
    int i,j,n;
    printf("Welcome to a student marks program!\n\n");
    printf("Please enter the number of students that you \n"
           "wish to feed into the program: \n\n");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("\nPlease enter the Roll no and the name of %d: \n\n",i+1);
        scanf("%d%s",&x[i].rollno,x[i].name);
        printf("\nPlease enter the marks of %s in the six respective subjects: \n\n",x[i].name);
        for(j=0;j<6;j++)
        scanf("%d",&x[i].marks[j]);
    }
    for(i=0;i<n;i++)
    {
        x[i].sum=0;
        for(j=0;j<6;j++)
        {
            x[i].sum+=x[i].marks[j];
            x[i].per=((float)x[i].marks[j]/6);
        }
    }
    printf("\nRoll No\t\t\t\tName\t\t\t\tTotal Marks\t\t\t\tPercentage scored\n\n");
    for(i=0;i<n;i++)
    printf("%4d\t\t\t\t%s\t\t\t\t%d\t\t\t\t\t%f\n",x[i].rollno,x[i].name,x[i].marks[j],x[i].per);
}

