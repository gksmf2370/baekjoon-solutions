#include <stdio.h>

int main() {
    int numbers[7];      
    int sum = 0;        
    int min = 101;       
    int hasOdd = 0;     

    for (int i = 0; i < 7; i++) {
        scanf("%d", &numbers[i]);
        

        if (numbers[i] % 2 != 0) {
            sum += numbers[i];
            if (numbers[i] < min) {
                min = numbers[i];
            }
            hasOdd = 1;           
        }
    }

    if (hasOdd) {
        printf("%d\n", sum);  
        printf("%d\n", min);  
    } else {
        printf("-1\n");       
    }

    return 0;
}
