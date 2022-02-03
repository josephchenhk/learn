/*
 * Pointers to structures
Let's say we want to create a function which moves a point forward in both x and y directions, called move. Instead of
sending two pointers, we can now send only one pointer to the function of the point structure:

void move(point * p) {
    (*p).x++;
    (*p).y++;
}

However, if we wish to dereference a structure and access one of it's internal members, we have a shorthand syntax for
that, because this operation is widely used in data structures. We can rewrite this function using the following syntax:

void move(point * p) {
    p->x++;
    p->y++;
}

------------------------------------------------------------------------------------------------------------------------
Exercise
Write a function called birthday, which adds one to the age of a person.
 */

#include <stdio.h>

typedef struct {
    char * name;
    int age;
} person;

/* function declaration */
void birthday(person * p);

/* write your function here */
void birthday(person * p){
    // dereference
//    p->age += 1;
    
    // anotherway to dereference
    (*p).age += 1;
}

int main() {
    person john;
    john.name = "John";
    john.age = 27;

    printf("%s is %d years old.\n", john.name, john.age);
    birthday(&john);
    printf("Happy birthday! %s is now %d years old.\n", john.name, john.age);

    return 0;
}