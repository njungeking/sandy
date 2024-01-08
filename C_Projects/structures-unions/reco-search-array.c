#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*A recap of structures including
comparison during run-time initialization*/

struct food
{
    int num;
    char name[20];
    float price;
};

int main()
{
    struct food x[50];
    int i,n,flag=0;
    char sname[20];
    printf("Welcome to another structure program!\n\n");
    printf("Please enter the number of items that you wish: \n\n");
    scanf("%d",&n);
    printf("\nPlease enter %d items in the order of: \n"
           "number, name and price: \n\n",n);
    for(i=0;i<n;i++)
    scanf("%d%s%f",&x[i].num,x[i].name,&x[i].price);
    printf("\nThe items that you entered are: \n\n");
    for(i=0;i<n;i++)
    printf("%d\t%s\t%f\n",x[i].num,x[i].name,x[i].price);
    printf("\n\n");
    printf("Please enter the item you would like to search for: \n\n");
    scanf("%s",sname);
    for(i=0;i<n;i++)
    {
        if(strcmp(x[i].name,sname)==0)
        {
            flag=1;
            break;
        }
    }
    if(flag==1)
    printf("\n%s is present. Check the details.\n\n",sname);
    else
    printf("\n%s is absent. Restart the program.\n\n",sname);
}

