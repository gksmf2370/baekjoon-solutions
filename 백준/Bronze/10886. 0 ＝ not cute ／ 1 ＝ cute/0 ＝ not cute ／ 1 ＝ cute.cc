#include <stdio.h>

int main() {
    int N, vote, cute = 0, not_cute = 0;

    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &vote);
        if (vote == 1) {
            cute++;
        } else if (vote == 0) {
            not_cute++;
        }
    }

    if (cute > not_cute) {
        printf("Junhee is cute!");
    } else {
        printf("Junhee is not cute!");
    }

    return 0;
}
