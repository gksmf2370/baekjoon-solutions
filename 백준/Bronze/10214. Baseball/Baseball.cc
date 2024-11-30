#include <stdio.h>

int main() {
    int T, yonsei, korea;
    
    scanf("%d", &T);
    
    while (T--) {
        int yonsei_total = 0, korea_total = 0;

        for (int i = 0; i < 9; i++) {
            scanf("%d %d", &yonsei, &korea);
            yonsei_total += yonsei;
            korea_total += korea;
        }

        if (yonsei_total > korea_total) {
            printf("Yonsei\n");
        } else if (yonsei_total < korea_total) {
            printf("Korea\n");
        } else {
            printf("Draw\n");
        }
    }

    return 0;
}
