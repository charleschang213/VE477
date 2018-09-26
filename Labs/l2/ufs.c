#include "ufs.h"
void ufs_init(ufs *x,int n){
    x->size=n;
    x->arr = (int*)malloc(n*sizeof(int));
    x->rank = (int*)malloc(n*sizeof(int));
    for (int i=0;i<n;i++) {
        x->arr[i]=i;
        x->rank[i]=0;
    }
}

void ufs_clean(ufs *x){
    free(x->arr);
    free(x->rank);
}

int ufs_find(ufs *x,int n){
    if (x->arr[n]==n) return n;
    x->arr[n] = ufs_find(x,x->arr[n]);
    return x->arr[n];
}

void ufs_union(ufs* x,int m,int n){
    int r1 = ufs_find(x,m);
    int r2 = ufs_find(x,n);
    if (x->rank[r1]>x->rank[r2]){
        x->arr[r2] = r1;
    }
    else {
        x->arr[r1] = r2;
        if (x->rank[r1]==x->rank[r2]) x->rank[r2]++;
    }
}