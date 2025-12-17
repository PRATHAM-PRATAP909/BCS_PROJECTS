#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
    char *temp;
int k=100; char *line, *s; /* the line to be returned */
s = fgets(temp, 512, stdin );
if (s!=NULL) {
line = (char *)calloc( k+1, sizeof(char)); /* add 1 for ‘\0’ */
strcpy(line, temp);
printf("%s",line);
}
}