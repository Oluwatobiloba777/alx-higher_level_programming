#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is palindrome
 *@head: head
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int cont = 0, buff[2048], idx = 0;

	if (!(*head) || !aux->next)
		return (1);
	while (aux)
	{	buff[cont] = aux->n;
		aux = aux->next;
		cont++;
	}
	while (cont > idx)
	{
		if (buff[idx] != buff[cont - 1])
			return (0);
		cont--;
		idx++;
	}
	return (1);
}
