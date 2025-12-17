#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
    int *str[3];
    int rows=2;
    for(int i=0;i<3;i++){
        str[i]=(int *)calloc(2,sizeof(int));
        //str[i]=(int *)malloc(rows*sizeof(int));
    }
    for(int i=0;i<3;i++){
        for(int j=0;j<2;j++){
            scanf("%d", &str[i][j]);
        }
    }
    for(int i=0;i<3;i++){
        for(int j=0;j<2;j++){
            printf("%d ",str[i][j]);
        }
    }
    // Cleanup: Free the memory allocated for each row
for(int i = 0; i < 3; i++){
    free(str[i]);
}

// NOTE: You DO NOT free 'str' itself, because it was declared on the stack 
// as an array: int *str[3];
    return 0;
}
