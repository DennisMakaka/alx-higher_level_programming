#include "lists.h"

/**
*check_cycle - checks if a linked list contains a cycle
*@list: pointer to the head of the linked list
*
*Return: 1 if the list has a cycle, 0 if it doesn't
*/

int check_cycle(listint_t *list)
{
/*Initialize two pointers, slow and fsat, to the head of the list */
listint_t *slow = list;
listint_t *fast = list;

/* Check if the list is empty */
if (!list)
	return (0);

/* Traverse the list using slow and fast pointers */
while (slow && fast && fast->next)
{
	/*move slow pointer one step at a time */
	slow = slow->next;

	/*Move fast pointer two steps at a time */
	fast = fast->next->next;

	/* Check if slow and fast pointers meet, indicatin a cycle */
	if (slow == fast)
		return (1);
}

	/* If the loop completes, there is no cycle in the list */
	return (0);
}
