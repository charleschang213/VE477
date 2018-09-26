#include "kruskal.h"
edge *kruskal(graph *x){
    qsort(x->edg,x->edges,12,edge_cmp);
    edge *ans = (edge*)malloc((x->size-1)*sizeof(edge));
    ufs newset;
    ufs_init(&newset,x->size);
    int flag = 0;
    for (int i=0;i<x->size-1;i++){
        while ((flag<x->edges)&&(ufs_find(&newset,x->edg[flag].x)==ufs_find(&newset,x->edg[flag].y))) flag++;
        ans[i]=x->edg[flag];
        ufs_union(&newset,ans[i].x,ans[i].y);
    }
    ufs_clean(&newset);
    return ans;
}