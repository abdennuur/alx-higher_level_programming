#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *crnt, *chk;

	if (list == NULL || list->next == NULL)
		return (0);
	crnt = list;
	chk = crnt->next;

	while (crnt != NULL && chk->next != NULL
		&& chk->next->next != NULL)
	{
		if (crnt == chk)
			return (1);
		crnt = crnt->next;
		chk = chk->next->next;
	}
	return (0);
}
