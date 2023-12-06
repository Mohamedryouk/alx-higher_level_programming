#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to reverse a linked list */
listint_t *reverse_list(listint_t *head) {
    listint_t *prev = NULL, *current = head, *next = NULL;
    
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    
    return prev;
}

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL) {
        return 1; // Empty list or single element is considered a palindrome
    }

    listint_t *slow = *head, *fast = *head, *second_half = NULL;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    if (fast != NULL) { // List has odd number of elements
        slow = slow->next;
    }

    second_half = reverse_list(slow);
    slow = *head;

    while (second_half != NULL) {
        if (slow->n != second_half->n) {
            return 0; // Not a palindrome
        }
        slow = slow->next;
        second_half = second_half->next;
    }

    return 1; // Palindrome
}

/* Function to print a linked list */
void print_list(listint_t *head) {
    while (head != NULL) {
        printf("%d -> ", head->n);
        head = head->next;
    }
    printf("NULL\n");
}

/* Function to add a new node to the linked list */
void push(listint_t **head, int data) {
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    new_node->n = data;
    new_node->next = *head;
    *head = new_node;
}

/* Function to free the memory allocated for the linked list */
void free_list(listint_t *head) {
    listint_t *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}
