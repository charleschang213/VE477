#include "graph.h"

int edge_cmp(const void *a,const void *b){
    const edge *x = (edge*)a;
    const edge *y = (edge*)b;
    if (x->val<y->val) return -1;
    if (x->val==y->val) return 0;
    return 1;
}

void graph_init(graph *x,int n,int e){
    x->size = n;
    x->edges = e;
    x->node = (int*)malloc(n*sizeof(int));
    x->edg = (edge*)malloc(e*sizeof(edge));
    for (int i=0;i<n;i++) 
        x->node[i] = i;
}

void graph_clean(graph *x){
    free(x->node);
    free(x->edg);
}