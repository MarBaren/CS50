#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])

// Zorg ervoor dat programma werkt met één command line argument en errorcode werkt
{
    if (argc != 2)
    {
        printf("Usage: ./ceasar key\n");
        return 1;
    }

    string key = argv[1];

    // check if input is a digit
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./ceasar key\n");
            return 1;
        }
    }

    // Get plaintext
    string plaintext = get_string("Plaintext: ");

    // convert key to int
    int k = atoi(key);
    printf("Ciphertext: ");

    // Obtain ciphertext
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isupper(plaintext[i]))
        {
            printf("%c", (((plaintext[i] - 'A') + k) % 26) + 'A');
        }
        else if (islower(plaintext[i]))
        {
            printf("%c", (((plaintext[i] - 'a') + k) % 26) + 'a');
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}
