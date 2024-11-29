#include <stdio.h>
#include <string.h>

int main() {
    int t; 
    scanf("%d", &t);
    
    while (t--) {
        int n; 
        scanf("%d", &n);

        char max_university[101] = ""; 
        int max_sul = -1; 
        
        for (int i = 0; i < n; i++) {
            char university[101];
            int sul;
            scanf("%s %d", university, &sul);
            
          
            if (sul > max_sul) {
                max_sul = sul;
                strcpy(max_university, university);
            }
        }
        
        printf("%s\n", max_university);
    }
    
    return 0;
}
