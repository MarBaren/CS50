#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get size of pyramide
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1 || n > 8);

    // Print pyramide
    for (int i = 0; i < n; i++)
    {
        // Loop voor space
        for (int s = n - i; s > 1; s--)
        {
            printf(" ");
        }
        // Loop voor linker #
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        // Loop voor gat tussenin
        {
            printf("  ");
        }
        // Loop voor rechter #
        for (int r = 0; r <= i; r++)
        {
            printf("#");
        }
        printf("\n");
    }
}