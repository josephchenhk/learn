int add(int a, int b);

int max(int x, int y);

enum DAY
{
      MON=1, TUE, WED, THU, FRI, SAT, SUN
} day;


void populate_array(int *array, size_t arraySize, int (*getNextValue)(void));

int getNextRandomValue(void);