#include "lists.h"
/**
 * check_cycle - check linked lists for cycles
 * @list: head list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast != NULL && slow != NULL)
	{
		slow = slow->next;
		if (fast != NULL)
		{
			fast = fast->next->next;
			if (fast == NULL)
			{
				continue;
			}
			else if (fast == slow)
			{
				return (1);
			}
		}
	}
	return (0);
}
