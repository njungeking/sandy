#include<stdio.h>
#include<stdlib.h>

/*Another recap of a structure
within another structure during
run-time initialization*/

struct doa
{
    int day;
    char month[20];
    int year;
};

struct students
{
    int rollno;
    char name[20];
    float per;
    struct doa y;
};

int main()
{
    struct students x;
    printf("Welcome to a structure within structure program!\n\n");
    printf("Please enter the details of the student in order of \n"
           "roll no, name, percentage scored and date of admission: \n\n");
    scanf("%d%s%f%d%s%d",&x.rollno,x.name,&x.per,&x.y.day,x.y.month,&x.y.year);
    printf("\n\nStudent's roll number is: %d.\n\n",x.rollno);
    printf("Student's name is: %s.\n\n",x.name);
    printf("Student's percentage score is: %f.\n\n",x.per);
    printf("Student's date of admission is: %d/%s/%d.\n\n",x.y.day,x.y.month,x.y.year);
}

