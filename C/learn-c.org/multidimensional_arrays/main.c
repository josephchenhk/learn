#include <stdio.h>

int main() {
    /* TODO: declare the 2D array grades here */
    float average;
    int i;
    int j;
    float grades[2][5];
    size_t n;
    size_t m;

    n = sizeof(grades)/sizeof(grades[0]);
    m = sizeof(grades[0])/sizeof(grades[0][0]);
    printf("The dimension of grades is (%d, %d)\n", n, m);

    grades[0][0] = 80;
    grades[0][1] = 70;
    grades[0][2] = 65;
    grades[0][3] = 89;
    grades[0][4] = 90;

    grades[1][0] = 85;
    grades[1][1] = 80;
    grades[1][2] = 80;
    grades[1][3] = 82;
    grades[1][4] = 87;



    /* TODO: complete the for loop with appropriate terminating conditions */
    for (i = 0; i < n; i++) {
        average = 0;
        for (j = 0; j < m; j++) {
            average += grades[i][j];
        }

        /* TODO: compute the average marks for subject i */
        average /= m;
        printf("The average marks obtained in subject %d is: %.2f\n", i, average);
    }

    return 0;
}
