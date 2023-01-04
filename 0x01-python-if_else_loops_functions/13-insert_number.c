#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - function that inserts a number into a sorted linked list.
 * @head: double pointer that points to the first element of the linked list.
 * @number: number to insert.
 * Return: The new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL, *j = *head;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	if (*head == NULL || j->n >= number)
	{
		node->n = number;
		node->next = *head;
		*head = node;
		return (node);
	}

	while (j->next != NULL && j->next->n < number)
	{
		if (!j)
		{
			free(node);
			return (NULL);
		}
		j = j->next;
	}
	node->n = number;
	node->next = j->next;
	j->next = node;

	return (node);
}
