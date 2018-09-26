#include "prim.h"

edge *prim(graph *x){
    qsort(x->edg,x->edges,sizeof(edge),edge_cmp);
    int *connected = malloc(x->size*sizeof(int));
    edge *ans = malloc((x->size-1)*sizeof(edge));
    for (int i=0;i<x->size;i++) connected[i]=0;
    connected[x->edg[0].x] = 1;
    for (int i=0;i<x->size-1;i++){
        for (int j=0;j<x->edges;j++){
            if (connected[x->edg[j].x]+connected[x->edg[j].y]==1){
                ans[i] = x->edg[j];
                connected[ans[i].x]=connected[ans[i].y]=1;
                break;
            }
        }
    }
    free(connected);
    return ans;
}