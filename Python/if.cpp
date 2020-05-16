#include <stdio.h>
int main() {
    int number1=20, number2=30;

    if(number1 == number2) {
        printf("Result: %d = %d",number1,number2);
    }

    else if (number1 > number2) {
        printf("Result: %d > %d", number1, number2);
    }

    else {
        printf("Result: %d < %d",number1, number2);
    }
    return 0;
}
