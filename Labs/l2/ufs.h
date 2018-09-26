#ifndef UFS_H
#define UFS_H
#include <stdlib.h>
typedef struct _ufs_{
    int *arr;
    int *rank;
    int size;
}ufs;
void ufs_init(ufs *x,int n);
void ufs_clean(ufs *x);
int ufs_find(ufs *x,int n);
void ufs_union(ufs* x,int m,int n);
#endif