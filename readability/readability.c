#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Vraag user om tekst
    string text = get_string("Text: ");
    printf("%s\n", text);

    // Tel de hoeveelheid letters
    int letterstext = count_letters(text);
    printf("%i letters\n", letterstext);

    // Tel de hoeveelheid woorden
    int wordstext = count_words(text);
    printf("%i words\n", wordstext);

    // Tel de hoeveelheid zinnen
    int sentencestext = count_sentences(text);
    printf("%i sentences\n", sentencestext);

    // Grade berekenen
    float L = ((float) letterstext / (float) wordstext) * 100;
    float S = ((float) sentencestext / (float) wordstext) * 100;
    int grade = round(0.0588 * L - 0.296 * S - 15.8);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 15)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int count_letters(string text)
{
    int letters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int count_words(string text)
{
    int words = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isblank(text[i]))
        {
            words++;
        }
    }
    return words;
}

int count_sentences(string text)
{
    int sentences = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }
    return sentences;
}