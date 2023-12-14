#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        {
            for (int j = 0; j < width; j++)
            {
                float red = image[i][j].rgbtRed;
                float green = image[i][j].rgbtGreen;
                float blue = image[i][j].rgbtBlue;

                int gem = round((red + green + blue) / 3);
                image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = gem;
            }
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            int sepiaRed = round(0.393 * red + 0.769 * green + 0.189 * blue);
            int sepiaGreen = round(0.349 * red + 0.686 * green + 0.168 * blue);
            int sepiaBlue = round(0.272 * red + 0.534 * green + 0.131 * blue);

            if (sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = sepiaRed;
            }

            if (sepiaGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = sepiaGreen;
            }

            if (sepiaBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = sepiaBlue;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        {
            for (int j = 0; j < width / 2; j++)
            {
                RGBTRIPLE temp = image[i][j];
                image[i][j] = image[i][width - (j + 1)];
                image[i][width - (j + 1)] = temp;
            }
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        {
            for (int j = 0; j < width; j++)
            {
                temp[i][j] = image[i][j];
            }
        }
    }

    for (int i = 0; i < height; i++)
    {
        {
            for (int j = 0; j < width; j++)
            {
                int totalRed, totalGreen, totalBlue;
                totalRed = totalGreen = totalBlue = 0;
                float counter = 0.00;

                for (int x = -1; x < 2; x++)
                {
                    for (int y = -1; y < 2; y++)
                    {
                        int currentx = i + x;
                        int currenty = j + y;

                        if (currentx < 0 || currentx > (height - 1) || currenty < 0 || currenty > (width - 1))
                        {
                            continue;
                        }

                        totalRed += image[currentx][currenty].rgbtRed;
                        totalGreen += image[currentx][currenty].rgbtGreen;
                        totalBlue += image[currentx][currenty].rgbtBlue;

                        counter++;
                    }

                    temp[i][j].rgbtRed = round(totalRed / counter);
                    temp[i][j].rgbtGreen = round(totalGreen / counter);
                    temp[i][j].rgbtBlue = round(totalBlue / counter);
                }
            }
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }
    return;
}
