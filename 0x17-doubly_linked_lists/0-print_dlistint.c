#include "lists.h"
/**
 * print_dlistint - print all the nodes data
 * @h: the head of the list
 *
 * Return: count of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	int i = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		i++;
		h = h->next;
	}
	return (i);
}
