#include <stdio.h>

/**
 * main - This Program counts the number
 * of characters in a string
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	long nc;

	nc = 0;
	while (getchar() != EOF)
	{
		++nc;
		printf("%ld\n", nc);
	}
	return (0);
}
