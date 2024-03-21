#include "lists.h"

/**
 * dlistint_len - Function to return the number of elements in a linked list.
 * @h: Pointer to the head of the list.
 * Return: count.
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		h = h->next;
		count++;
	}

	return (count);
}
