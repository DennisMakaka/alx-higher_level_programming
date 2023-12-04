#include "lists.h"
#include <stdlib.h>

/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list.
 * @head: Pointer to the head of listint_t.
 * @n: Integer to add in listint_t list.
 * Return: Address of the new element, or NULL if it failed.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node = malloc(sizeof(listint_t)); /* Allocate memory for new node */

	if (!new_node) /* Check if malloc failed */
		return (NULL);

	new_node->n = n; /* Assign value to the new node */
	new_node->next = *head; /* Update the next pointer of the new node */
	*head = new_node; /* Update the head pointer to the new node */

	return (new_node); /* Return the address of the new node */
}

/**
 * is_palindrome - Identifies if a singly linked list is palindrome.
 * @head: Pointer to the head of listint_t.
 * Return: 1 if it is palindrome else 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head;
	listint_t *reversed_list = NULL, *temp = NULL;

	if (!*head || head2->next == NULL)
		return (1); /* An empty list or a list with one element is a palindrome */

	while (head2 != NULL)
	{
		add_nodeint(&reversed_list, head2->n); /* Create a reversed copy of the list */
		head2 = head2->next;
	}

	temp = reversed_list;
	while (*head != NULL)
	{
		if ((*head)->n != temp->n) /* Compare each element of the original list with the reversed copy */
		{
			free_listint(reversed_list); /* Free memory allocated for reversed copy */
			return (0); /* Not a palindrome */
		}
		*head = (*head)->next;
		temp = temp->next;
	}

	free_listint(reversed_list); /* Free memory allocated for reversed copy */
	return (1); /* It is a palindrome */
}
