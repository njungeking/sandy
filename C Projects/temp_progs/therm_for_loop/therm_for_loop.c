#include <stdio.h>
#include <stdlib.h>

/**
 * main - Temperature is produced as a for loop
 *
 * Return: Always 0 (Success).
*/

int main(void)
	{
		int fahr;

		printf("Welcome to another Temperature-conversion Program!\n\n");

		for (fahr = 0; fahr <= 300; fahr = fahr + 20)
		{
			printf("%3d %6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32.0));
		}
		return (0);
	}
