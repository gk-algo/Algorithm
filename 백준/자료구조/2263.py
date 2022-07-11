import sys
sys.setrecursionlimit(10000000)
def find(instart, inend, poststart, postend):
    if (instart>inend or poststart>postend):
        return
    root=postorder[postend]
    left=position[root]-instart
    right=inend-position[root]
    print(root,end=" ")
    find(instart, instart+left-1, poststart, poststart+left-1)
    find(inend-right+1,inend,postend-right,postend-1)

n=int(input())
# left root right
inorder=list(map(int,input().split()))
# left right root
postorder=list(map(int,input().split()))
root=postorder[-1]
position=[0]*(n+1)
for x in range(n):
    position[inorder[x]]=x
find(0,n-1,0,n-1)
