#include<stdio.h>
#include<stdlib.h>

/*Structure within another structure*/

struct admin
{
    int day;
    int month;
    int year;
};

struct students
{
    int rollno;
    char name[50];
    float per;
    struct admin doa;
};

int main()
{
    struct students x;
    printf("Welcome to a student details program!\n\n");
    printf("Please enter the roll no, name, percentage scored \n"
           "and date of admission of the student: \n\n");
    scanf("%d%s%f%d%d%d",&x.rollno,&x.name,&x.per,&x.doa.day,&x.doa.month,&x.doa.year);
    printf("\nThe student's roll no is: %d\n",x.rollno);
    printf("The student's name is: %s\n",x.name);
    printf("The student's percentage score is: %f\n",x.per);
    printf("The student's date of admission was: %d/%d/%d\n\n",x.doa.day,x.doa.month,x.doa.year);
}

