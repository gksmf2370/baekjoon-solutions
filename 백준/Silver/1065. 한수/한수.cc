#include <stdio.h>


int is_han(int num) {
    if (num < 100) {
        return 1; 
    }
    int hundreds = num / 100;
    int tens = (num / 10) % 10;
    int ones = num % 10;

    // 등차수열
    if ((hundreds - tens) == (tens - ones)) {
        return 1; // 한수
    }
    return 0; 
}

int main() {
    int n, count = 0;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        if (is_han(i)) {
            count++;
        }
    }

    printf("%d\n", count);
    return 0;
}
