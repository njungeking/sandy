#include <stdio.h>

/**
 * main - This program counts the
 * number of blanks, tabs and
 * newlines
 *
 * Return (0): Always Success
 */

int main(void)
{
	int c, nl, t, b;

	for (nl = 0; (c = getchar()) != EOF; ++nl)
		if (c == '\n')
			printf("%d\n", nl)
