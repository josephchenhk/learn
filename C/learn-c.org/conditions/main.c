/*
 * Exercise
In this exercise, you must construct an if statement inside the guessNumber function statement that checks if the
number guess is equal to 555. If that is the case, the function must print out using printf "Correct. You guessed it!".
If guess is less than 555, the function must print out using printf "Your guess is too low." If guess is greater than
 555, the function must print out using printf "Your guess is too high."

Important: Don't forget to add a newline character \n at the end of the printf string.
 */

#include <stdio.h>

void guessNumber(int guess) {
    // TODO: write your code here
    int correct_guess = 555;
    if (guess == correct_guess){
        printf("Correct. You guessed it!\n");
    }else if (guess < correct_guess){
        printf("Your guess is too low.\n");
    }else{
        printf("Your guess is too high.\n");
    }
}

int main() {
    guessNumber(500);
    guessNumber(600);
    guessNumber(555);
}
