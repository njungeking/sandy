#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*Structure syntax initialization
during compile-time initialization*/

struct workers
{
    int wno;
    char name[30];
    float sal;
};

int main()
{
    struct workers x;
    x.wno=3445;
    strcpy(x.name,"Ronald");
    x.sal=970.34;
    printf("Welcome to a structure program!\n\n");
    printf("Worker number: %d\n\n",x.wno);
    printf("Worker name: %s\n\n",x.name);
    printf("Worker salary: %f\n\n",x.sal);
}

