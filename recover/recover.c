#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open memory card file
    FILE *file = fopen(argv[1], "r");

    // Check if file is valid
    if (file == NULL)
    {
        printf("Could not open file");
        return 2;
    }

    int BLOCK_SIZE = 512;
    unsigned char buffer[BLOCK_SIZE];
    int count_image = 0;
    FILE *output_file = NULL;

    char *filename = malloc(8 * sizeof(char));

    // Look for beginning of JPEG (three bytes: 0xff 0xd8 0xff) (fread(data, size, number, inptr))
    // Repeat until end of card
    while (fread(buffer, sizeof(char), BLOCK_SIZE, file))
    {
        // Read 512 bytes into a buffer
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (count_image > 0)
            {
                fclose(output_file);
            }

            // make JPEG file
            sprintf(filename, "%03i.jpg", count_image);

            // When JPEG found, open a new JPEG file
            output_file = fopen(filename, "w");

            // Count images found
            count_image++;
        }

        // Write 512 bytes until a new JPEG is found
        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), BLOCK_SIZE, output_file);
        }
    }
    free(filename);
    fclose(output_file);
    fclose(file);

    return 0;
}