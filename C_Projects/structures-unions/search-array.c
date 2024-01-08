#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*Search operation in an array
of structures*/

struct shoes
{
    int size;
    char name[30];
    float price;
};

int main()
{
    struct shoes x[100];
    int i,n,flag=0;
    char sname[50];
    printf("Welcome to a search & structure program!\n\n");
    printf("Please enter the number of shoe items that you \n"
           "wish: \n\n");
    scanf("%d",&n);
    printf("\nPlease enter the details of %d items in \n"
           "the order of size, name and price: \n\n",n);
    for(i=0;i<n;i++)
    scanf("%d%s%f",&x[i].size,x[i].name,&x[i].price);
    printf("\nThe details of your items are: \n\n");
    for(i=0;i<n;i++)
    printf("%d\t%s\t%f\n",x[i].size,x[i].name,x[i].price);
    printf("\nPlease enter the item you would like to search for: \n\n");
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
    printf("\n%s is absent. Check the details.\n\n",sname);
}

