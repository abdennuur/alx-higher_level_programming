#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - Checks if singly linked list is palindrome
  * @head: head of the singly linked ls
  *
  * Return: 0 -> not palindrome, 1 -> palindrome
  */
int is_palindrome(listint_t **head)
{
    listint_t *strt = NULL, *end = NULL;
    unsigned int ix = 0, ln = 0, ln_cyc = 0, ln_list = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    strt = *head;
    ln = listint_ln(strt);
    ln_cyc = ln * 2;
    ln_list = ln_cyc - 2;
    end = *head;

    for (; ix < ln_cyc; ix = ix + 2)
    {
        if (strt[ix].n != end[ln_list].n)
            return (0);

        ln_list = ln_list - 2;
    }

    return (1);
}

/**
  * get_nodeint_at_index - Get node frm linked list
  * @head: head of linked list
  * @index: idx to find in linked list
  *
  * Return: specific node of linked list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *crrnt = head;
	unsigned int itr_times = 0;

	if (head)
	{
		while (crrnt != NULL)
		{
			if (itr_times == index)
				return (crrnt);

			crrnt = crrnt->next;
			++itr_times;
		}
	}

	return (NULL);
}

/**
  * slistint_len - Count the nmbr of elements in  linked list
  * @h: linked list to count
  *
  * Return: Nbr of elements in linked list
  */
size_t listint_len(const listint_t *h)
{
	int len = 0;

	while (h != NULL)
	{
		++len;
		h = h->next;
	}

	return (len);
}
