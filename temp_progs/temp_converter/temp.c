#include <stdio.h>
#include <stdlib.h>

/**
 * main - Temperature converter program
 * This program converts degrees celsius
 * to farenheit
 * Return: Always 0.
*/

int main(void)
{
float cels, fahr;
float upper, step, lower;

upper = 100;
step = 10;
lower = 0;

printf("Welcome to the temperature converter program\n");

cels = lower;
while (cels <= upper)
{
	fahr = (cels * 9 / 5) + 32;
	printf("%3.0f\t%6.1f\n", cels, fahr);
	cels = cels + step;
}
return (0);
}
