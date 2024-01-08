#include <stdio.h>

/**
 * main - this copies input into output
 * first version
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	int c;

	c = getchar();
	while (c != EOF)
	{
		putchar(c);
		c = getchar();
	}
	return (0);
}
