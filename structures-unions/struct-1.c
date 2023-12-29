#include<stdio.h>
#include<stdlib.h>

/*Structures syntax initialization*/

struct employees
{
    int eno;
    char name[50];
    float sal;
};

int main()
{
    struct employees x={25,"Alfred",1500.23};
    printf("Welcome to a structre program!\n\n");
    printf("Employee Roll-number: %d\n\n",x.eno);
    printf("Employee name: %s\n\n",x.name);
    printf("Employee salary: %f\n\n",x.sal);
}

