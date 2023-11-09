// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 50000;

// Hash table
node *table[N];

unsigned int count_words;
unsigned int hash_value;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    hash_value = hash(word);
    node *locator = table[hash_value];

    while (locator != 0)
    {
        if (strcasecmp(word, locator->word) == 0)
        {
            return true;
        }
        locator = locator->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned int hash = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        hash = (hash * 2 * 2) ^ tolower(word[i]);
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO

    FILE *infile = fopen(dictionary, "r");

    if (infile == NULL)
    {
        return false;
    }

    char word[LENGTH + 1];
    while (fscanf(infile, "%s", word) != EOF)
    {
        node *new_word = malloc(sizeof(node));

        if (new_word == NULL)
        {
            return false;
        }

        strcpy(new_word->word, word);
        hash_value = hash(word);
        new_word->next = table[hash_value];
        table[hash_value] = new_word;
        count_words++;
    }
    fclose(infile);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (count_words > 0)
    {
        return count_words;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO

    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }

        if (cursor == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}
