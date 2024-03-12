#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to the head of the list
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t));
listint_t *current = *head;
listint_t *prev = NULL;

if (new_node == NULL)
return (NULL);

new_node->n = number;
new_node->next = NULL;

if (*head == NULL || number < (*head)->n)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}

while (current != NULL && current->n < number)
{
prev = current;
current = current->next;
}

prev->next = new_node;
new_node->next = current;

return (new_node);
}
