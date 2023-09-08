#include <stdio.h>

/**
 * main - This program verifies that the expression:
 * getchar() != EOF is 0 or 1
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	int c;

	while (c = (getchar() != EOF))
	{
		putchar(c);
	}
}
