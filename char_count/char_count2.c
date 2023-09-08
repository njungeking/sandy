#include <stdio.h>

/**
 * main - This program counts the
 * number of chars in a string
 * second version
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	double nc;

	for (nc = 0; getchar() != EOF; ++nc)
	{
		printf("%.0f\n", nc);
	}
	return (0);
}
