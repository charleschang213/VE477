#ifndef GRAPH_H
#define GRAPH_H
#include <stdlib.h>
typedef struct _edge_{
    int x,y,val;
}edge;
typedef struct _graph_{
    int size,edges;
    int *node;
    edge *edg;
}graph;
int edge_cmp(const void *a,const void *b);
void graph_init(graph *x,int n,int e);
void graph_clean(graph *x);
#endif