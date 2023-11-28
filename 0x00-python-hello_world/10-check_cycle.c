#include "lists.h"
/**
 * check_cycle - check linked lists for cycles
 * @list: head list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
