#include <stdio.h>

/**
 * main - This program counts lines
 * of code inputed by the user
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	int c, nl;

	nl = 0;

	while ((c = getchar()) != EOF)
		if (c == '\n')
		{
			++nl;
			printf("%d\n", nl);
		}
	return (0);
}
