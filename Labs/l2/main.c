#include <stdio.h>
#include <time.h>
#include "kruskal.h"
#include "prim.h"

int main(){
    graph g1,g2;
    edge *ans1,*ans2;
    graph_init(&g1,6,10);
    g1.edg[0].x = 0; g1.edg[0].y = 1;g1.edg[0].val=6;
    g1.edg[1].x = 0; g1.edg[1].y = 2;g1.edg[1].val=1;
    g1.edg[2].x = 0; g1.edg[2].y = 3;g1.edg[2].val=5;
    g1.edg[3].x = 1; g1.edg[3].y = 2;g1.edg[3].val=5;
    g1.edg[4].x = 1; g1.edg[4].y = 4;g1.edg[4].val=3;
    g1.edg[5].x = 2; g1.edg[5].y = 3;g1.edg[5].val=5;
    g1.edg[6].x = 2; g1.edg[6].y = 4;g1.edg[6].val=6;
    g1.edg[7].x = 2; g1.edg[7].y = 5;g1.edg[7].val=4;
    g1.edg[8].x = 3; g1.edg[8].y = 5;g1.edg[8].val=2;
    g1.edg[9].x = 4; g1.edg[9].y = 5;g1.edg[9].val=6;
    ans1 = kruskal(&g1);
    for (int i=0;i<g1.size-1;i++) printf("<%d,%d> ",ans1[i].x,ans1[i].y);
    free(ans1);
    graph_clean(&g1);
    return 0;
}