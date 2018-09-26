#include <stdio.h>
#include <time.h>
#include "kruskal.h"
#include "prim.h"

int main(){
    srand(time(NULL));
    printf("###Part I: Checking for correctness###\n");
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
    printf("Kruskal: ");
    for (int i=0;i<g1.size-1;i++) printf("<%d,%d> ",ans1[i].x,ans1[i].y);
    printf("\n");
    free(ans1);
    graph_init(&g2,6,10);
    g2.edg[0].x = 0; g2.edg[0].y = 1;g2.edg[0].val=6;
    g2.edg[1].x = 0; g2.edg[1].y = 2;g2.edg[1].val=1;
    g2.edg[2].x = 0; g2.edg[2].y = 3;g2.edg[2].val=5;
    g2.edg[3].x = 1; g2.edg[3].y = 2;g2.edg[3].val=5;
    g2.edg[4].x = 1; g2.edg[4].y = 4;g2.edg[4].val=3;
    g2.edg[5].x = 2; g2.edg[5].y = 3;g2.edg[5].val=5;
    g2.edg[6].x = 2; g2.edg[6].y = 4;g2.edg[6].val=6;
    g2.edg[7].x = 2; g2.edg[7].y = 5;g2.edg[7].val=4;
    g2.edg[8].x = 3; g2.edg[8].y = 5;g2.edg[8].val=2;
    g2.edg[9].x = 4; g2.edg[9].y = 5;g2.edg[9].val=6;
    ans2 = prim(&g2);
    printf("Prim: ");
    for (int i=0;i<g2.size-1;i++) printf("<%d,%d> ",ans2[i].x,ans2[i].y);
    printf("\n");
    free(ans2);
    graph_clean(&g2);
    graph_clean(&g1);
    printf("######################################\n\n");
    printf("######Part II: Large Sparse Graph######\n");
    graph_init(&g1,10000,10000);
    graph_init(&g2,10000,10000);
    for (int i=0;i<9999;i++){
        g1.edg[i].x = g2.edg[i].x = i;
        g1.edg[i].y = g2.edg[i].y = i+1;
        g1.edg[i].val = g2.edg[i].val = rand()%1000;
    }
    g1.edg[9999].x = g2.edg[9999].x = 0;
    g1.edg[9999].y = g2.edg[9999].y = 2;
    g1.edg[9999].val = g2.edg[9999].val = rand()%1000;
    long  now = clock();
    ans1 = kruskal(&g1);
    long duration = clock()-now;
    printf("Kruskal: %fms\n",((double)duration)/((double)CLOCKS_PER_SEC)*1000);
    now = clock();
    ans2 = prim(&g2);
    duration = clock()-now;
    printf("Prim: %fms\n",((double)duration)/((double)CLOCKS_PER_SEC)*1000);
    free(ans2);
    free(ans1);
    graph_clean(&g2);
    graph_clean(&g1);
    printf("#######################################\n\n");

    printf("######Part III: Large Dense Graph######\n");
    graph_init(&g1,10000,49995000);
    graph_init(&g2,10000,49995000);
    int flag = 0;
    for (int i=0;i<9999;i++)
        for (int j=i+1;j<10000;j++){
            g1.edg[flag].x = g2.edg[flag].x = i;
            g1.edg[flag].y = g2.edg[flag].y = j;
            g1.edg[flag].val = g2.edg[flag].val = rand()%1000;
            flag++;
        }
    now = clock();
    ans1 = kruskal(&g1);
    duration = clock()-now;
    printf("Kruskal: %fms\n",((double)duration)/((double)CLOCKS_PER_SEC)*1000);
    now = clock();
    ans2 = prim(&g2);
    duration = clock()-now;
    printf("Prim: %fms\n",((double)duration)/((double)CLOCKS_PER_SEC)*1000);
    free(ans2);
    free(ans1);
    graph_clean(&g2);
    graph_clean(&g1);
    printf("#######################################\n\n");
    return 0;
}