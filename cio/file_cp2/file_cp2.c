#include <stdio.h>

/**
 * main - This program copies input into output
 * Second version
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	int c;

	while ((c = getchar()) != EOF)
	{
		putchar(c);
	}
	return (0);
}
