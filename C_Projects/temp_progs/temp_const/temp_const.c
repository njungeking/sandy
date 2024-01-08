#include <stdio.h>

/**
 * main - Temperature conversion using constants
 *
 * Return: Always 0 (Success)
 */

#define LOWER 0 /* lower limit of table */
#define UPPER 300 /* upper limit of table */
#define STEP 20 /* step size */

int main(void)
{
	printf("Welcome to the Temperature Conversion Program!\n");

	int fahr;

	for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
	{
		printf("%3d %6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));
	}
	return (0);
}
