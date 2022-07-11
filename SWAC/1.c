#include <stdio.h>
#include <stdlib.h>
int metrix[101][101];
int vis[101][101] = {
    0,
};
struct data
{
    int x;
    int y;
};
struct node
{
    struct node *next;
    struct data numdata;
};
struct queue
{
    struct node *front;
    struct node *rear;
    int count;
};
void init_queue(struct queue *q)
{
    q->count = 0;
    q->front = q->rear = NULL;
}
void enqueue(struct queue *q, struct data d)
{
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    newnode->numdata = d;
    newnode->next = NULL;
    if (q->front == NULL)
    {
        q->front = newnode;
    }
    else
    {
        q->rear->next = newnode;
    }
    q->rear = newnode;
    q->count++;
}
struct data dequeue(struct queue *q)
{
    struct data d;
    struct node *tmp;
    if (q->count > 0)
    {

        tmp = q->front;
        q->front = tmp->next;
        d = tmp->numdata;
        q->count--;
    }
    return d;
}
int bfs(int x, int y, int n, int height)
{
    struct queue q;
    struct data d;
    struct data tmp;
    int i = 0;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    int X, Y;
    if (vis[x][y] == 0 && metrix[x][y] > height)
    {
        d.x = x;
        d.y = y;
        init_queue(&q);
        enqueue(&q, d);
        while (q.count > 0)
        {
            d = dequeue(&q);
            vis[d.x][d.y] = 1;
            for (i = 0; i < 4; i++)
            {
                X = d.x + dx[i];
                Y = d.y + dy[i];
                if (0 <= X < n && 0 <= Y < n && vis[X][Y] == 0 && metrix[X][Y] > height)
                {
                    tmp.x = X;
                    tmp.y = Y;
                    enqueue(&q, tmp);
                }
            }
        }
        return 1;
    }
    return 0;
}
int main(void)
{
    int T, x, n, i, y, j, v, w;
    int top = 0;
    int cnt = 0;
    int topcount = 0;
    setbuf(stdout, NULL);
    scanf("%d", &T);
    for (i = 0; i < T; i++)
    {
        scanf("%d", &n);
        for (x = 0; x < n; x++)
        {

            for (y = 0; y < n; y++)
            {
                scanf("%d", &metrix[x][y]);
                vis[x][y] = 0;
                if (metrix[x][y] > top)
                {
                    top = metrix[x][y];
                }
            }
        }
        for (j = 0; j <= top; j++)
        {
            for (v = 0; v < n; v++)
            {
                for (w = 0; w < n; w++)
                {
                    vis[v][w] = 0;
                }
            }
            cnt = 0;
            for (x = 0; x < n; x++)
            {
                for (y = 0; y < n; y++)
                {
                    if (bfs(x, y, n, j) == 1)
                    {
                        cnt++;
                    }
                }
            }
            if (topcount < cnt)
            {
                topcount = cnt;
            }
        }
        printf("#%d %d\n", i + 1, topcount);
    }
    return 0;
}