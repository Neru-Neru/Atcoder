class Node:
    def __init__(self):
        self.parent = -1
        self.children = []
def cal_depth(node_id, d = 0):
    Tree[node_id].depth = d
    for child in Tree[node_id].children:
        cal_depth(child, d+1)

n=int(input())
p=list(map(int, input().split()))
q=int(input())
Tree = [Node() for _ in range(n + 1)]
Tree[1].parent = 0
for i in range(len(p)):
    Tree[i + 2].parent = p[i]
    Tree[p[i]].children.append(i + 2)
cal_depth(1)
for i in range(q):
    u, d=map(int, input().split())
    