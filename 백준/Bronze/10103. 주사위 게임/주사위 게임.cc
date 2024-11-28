#include <stdio.h>

int main() {
    int N; 
    scanf("%d", &N);

    int A_score = 100, B_score = 100; 

    for (int i = 0; i < N; ++i) {
        int a, b; 
        scanf("%d %d", &a, &b);

        if (a > b) {
            B_score -= a; 
        } else if (a < b) {
            A_score -= b;
        }
      
    }

    printf("%d %d\n", A_score, B_score); 

    return 0;
}
