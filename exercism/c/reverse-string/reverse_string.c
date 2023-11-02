#include "reverse_string.h"


char *reverse(const char *value) {
    int len = strlen(value);
    char *rs;
    rs  = (char *) malloc(sizeof(value) * len + 1);

    for (int i = 0; i < len; i++) {
        rs[i] = value[len-1-i];
    }
    rs[len] = '\0';

    return rs;
}
