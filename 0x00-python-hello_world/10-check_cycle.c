#include "lists.h"

/**
 * check_cycle - function check if singly linked list has a cycle
 * @list: pnr to beginning of node
 * Return: 0 -> no cycle, 1 -> cycle
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
