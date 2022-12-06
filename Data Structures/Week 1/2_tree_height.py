# python3

import sys
import threading


def compute_height(n, parents):
    nodes = [[] for _ in range(n)]
    heights = [0] * n
    root = -1

    for child in range(n):
        parent = parents[child]
        if parent == -1:
            root = child
        else:
            nodes[parent].append(child)
    max_height = 0
    q = [root]
    while q:
        curr = q.pop(0)
        for v in nodes[curr]:
            heights[v] = heights[curr] + 1
            q.append(v)
        max_height = heights[curr] + 1
    # print(nodes)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
