#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - print all elements of  listint_t list
 * @h: ptr to head of list
 * Return: nbr of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *curr;
    unsigned int ne;

    curr = h;
    n = 0;
    while (curr != NULL)
    {
        printf("%i\n", curr->n);
        curr = curr->next;
        n++;
    }

    return (ne);
}

/**
 * add_nodeint_end - add new node at end of a listint_t list
 * @head: ptr to ptr of first node of listint_t list
 * @n: int to be included in new node
 * Return: address of new element or NULL if fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *curr;

    curr = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (curr->next != NULL)
            curr = curr->next;
        curr->next = new;
    }

    return (new);
}

/**
 * free_listint - frees listint_t list
 * @head: ptr to list to be free
 * Return: nothing
 */
void free_listint(listint_t *head)
{
    listint_t *curr;

    while (head != NULL)
    {
        curr = head;
        head = head->next;
        free(curr);
    }
}
