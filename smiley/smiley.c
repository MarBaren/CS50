#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            if (red == 0 && green == 0 && blue == 0)
            {
                image[i][j].rgbtRed = 33;
                image[i][j].rgbtGreen = 103;
                image[i][j].rgbtBlue = 94;
            }
        }
    }
    return;
}
