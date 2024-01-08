#include <stdio.h>
#include <stdlib.h>

/**
 * main - This program converts temperature from
 * Farenheit to celsius in a descending order
 * in steps of 20.
 *
 * Return: Always 0 (Success)
*/

int main(void)
{
	 int fahr;
	printf("Welcome to the Reverse Temperature-Conversion Program!\n\n");
	for (fahr = 300; fahr >= 0; fahr = fahr - 20)

	{
		printf("%3d %6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));
	}
	return (0);
}
