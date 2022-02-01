/*
 * Exercise
Define the string first_name with the value John using the pointer notation, and define the string last_name with the
value Doe using the local array notation.
 */

#include <stdio.h>
#include <string.h>
int main() {
    /* define first_name */
    /* define last_name */
    char name[100];
    char * first_name = "John";
    char last_name[] = "Doe";  // you can't use single quote!

    // clear name to a zero-length string
    name[0]='\0';
    strncat(name,first_name,4);
    strncat(name, " ", 1);
    strncat(name,last_name,20);
    printf("name = %s\n",name);
    printf("strlen(name) = %d\n",strlen(name));
    if (strncmp(name, "John Nash", 10) == 0) {
        printf("Name is John Nash now. Done!\n");
    }

    name[5] = '\0';
    printf("name = %s\n",name);
    printf("strlen(name) = %d\n",strlen(name));

    strncat(name, "Nash", 4);

    printf("name = %s\n",name);
    printf("strlen(name) = %d\n",strlen(name));

    if (strncmp(name, "John Nash", 10) == 0) {
        printf("Name is John Nash now. Done!\n");
    }
    return 0;
}