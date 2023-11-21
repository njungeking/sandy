#include<stdio.h>
#include<stdlib.h>

/*A recap of the gcd function using recursion*/

int gcd(int x, int y);

int main()
{
    int x,y,ans;
    printf("Please put in two numbers to find the GCD: \n\n");
    scanf("%d%d",&x,&y);
    ans=gcd(x,y);
    printf("\nThe GCD of %d and %d is: %d\n",x,y,ans);
}

int gcd(int x,int y)
{
    int i,min,res;
    min=x<y?x:y;
    for(i=1;i<=min;i++)
    {
        if(x%i==0 && y%i==0)
        res=i;
    }
    return res;
}
